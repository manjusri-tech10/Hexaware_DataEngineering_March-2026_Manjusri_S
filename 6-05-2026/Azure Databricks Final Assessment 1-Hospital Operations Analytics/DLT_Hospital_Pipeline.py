import dlt
from pyspark.sql.functions import col, to_date, when, sum

# 88
@dlt.table(name="bronze_patient_visits")
def bronze_patient_visits():
    data = [
        (1,1001,201,"2024-03-01","Completed",2,5200,"UPI","Paid","Aarav Khan","Hyderabad","Cardiology"),
        (2,1002,202,"2024-03-01","Completed",1,2800,"Credit Card","Paid","Priya Reddy","Bengaluru","Dermatology"),
        (3,1003,203,"2024-03-02","Completed",3,7500,"Cash","Paid","Rahul Mehta","Mumbai","Orthopedics"),
        (4,1004,204,"2024-03-02","Pending",1,2900,"UPI","Pending","Sneha Kapoor","Delhi","Pediatrics"),
        (5,1005,206,"2024-03-03","Completed",2,5300,"Debit Card","Paid","Kiran Patel","Ahmedabad","Cardiology"),
        (6,1006,205,"2024-03-03","Completed",4,10000,"Credit Card","Paid","Ananya Das","Kolkata","Neurology"),
        (7,1007,207,"2024-03-04","Cancelled",1,2850,"Cash","Cancelled","Vikram Singh","Chennai","Dermatology"),
        (8,1008,208,"2024-03-04","Completed",2,5400,"UPI","Paid","Meera Nair","Kochi","Orthopedics"),
        (9,1009,201,"2024-03-05","Completed",1,3200,"UPI","Paid","Farhan Ali","Hyderabad","Cardiology"),
        (10,1010,202,"2024-03-05","Completed",2,4800,"Credit Card","Paid","Divya Menon","Bengaluru","Dermatology")
    ]
    columns = ["visit_id","patient_id","doctor_id","visit_date","visit_status",
               "tests_conducted","bill_amount","payment_mode","payment_status",
               "patient_name","city","specialization"]
    return spark.createDataFrame(data, columns)

# 89 ,90 ,91 — silver 
@dlt.table(name="silver_patient_visits")
@dlt.expect_or_drop("valid_visit_id",  "visit_id IS NOT NULL")
@dlt.expect_or_drop("valid_bill",      "bill_amount > 0")
@dlt.expect_or_drop("no_cancelled",    "visit_status != 'Cancelled'")
def silver_patient_visits():
    return (
        dlt.read("bronze_patient_visits")
        .withColumn("visit_date",
            to_date(col("visit_date"), "yyyy-MM-dd"))
        .withColumn("visit_status",
            when(col("visit_status").isNull(), "Unknown")
            .otherwise(col("visit_status")))
        .withColumn("total_bill",
            col("bill_amount") + col("tests_conducted") * 500)
    )

# 92 gold1
@dlt.table(name="gold_city_revenue")
def gold_city_revenue():
    return (
        dlt.read("silver_patient_visits")
        .groupBy("city")
        .agg(sum("total_bill").alias("total_revenue"))
    )

# 93 gold2
@dlt.table(name="gold_specialization_revenue")
def gold_specialization_revenue():
    return (
        dlt.read("silver_patient_visits")
        .groupBy("specialization")
        .agg(sum("total_bill").alias("total_revenue"))
    )