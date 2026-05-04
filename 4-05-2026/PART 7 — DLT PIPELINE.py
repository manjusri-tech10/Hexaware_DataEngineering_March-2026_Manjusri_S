import dlt
from pyspark.sql.functions import col, when, sum, count

# Bronze layer
@dlt.table(name="bronze_hospital", comment="Raw hospital visit data")
def bronze_hospital():
    data = [
        (101,"Arjun Reddy","Hyderabad","Cardiology",5000,1),
        (102,"Sneha Kapoor","Delhi","Orthopedics",3000,2),
        (103,"Rahul Sharma","Mumbai","Dermatology",1500,1),
        (104,"Priya Nair","Bangalore","Cardiology",5000,2),
        (105,"Vikram Singh","Chennai","Neurology",7000,1),
        (106,"Ananya Das","Kolkata","Orthopedics",3000,3),
        (107,"Karan Patel","Ahmedabad","Cardiology",5000,1),
        (108,"Meera Iyer","Bangalore","Dermatology",1500,2)
    ]
    columns = ["visit_id","patient_name","city","department","consultation_fee","tests_count"]
    return spark.createDataFrame(data, columns)

# Silver layer
@dlt.table(name="silver_hospital", comment="Cleaned and enriched data")
@dlt.expect("valid_fee", "consultation_fee > 0")
def silver_hospital():
    return (
        dlt.read("bronze_hospital")
           .withColumn("total_bill",
               col("consultation_fee") + col("tests_count") * 500)
           .withColumn("patient_category",
               when(col("consultation_fee") >= 5000, "High")
              .when(col("consultation_fee") >= 3000, "Medium")
              .otherwise("Low"))
           .filter(col("consultation_fee") > 0)
    )

# Gold layer
@dlt.table(name="gold_department_summary", comment="Department aggregations")
def gold_department_summary():
    return (
        dlt.read("silver_hospital")
           .groupBy("department")
           .agg(
               count("visit_id").alias("patient_count"),
               sum("consultation_fee").alias("total_revenue"),
               sum("total_bill").alias("total_billing")
           )
    )