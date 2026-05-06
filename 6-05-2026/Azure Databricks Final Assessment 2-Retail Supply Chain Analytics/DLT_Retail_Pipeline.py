import dlt
from pyspark.sql.functions import col, to_date, when, sum

# 88 bronze
@dlt.table(name="bronze_orders")
def bronze_orders():
    data = [
        (301,101,201,"2024-04-01",20,"Delivered",24000,"UPI","Paid","Rice Bag","Groceries","Hyderabad","Reddy Traders"),
        (302,102,201,"2024-04-01",35,"Delivered",31500,"Credit Card","Paid","Wheat Flour","Groceries","Bengaluru","Reddy Traders"),
        (303,111,204,"2024-04-02",2,"Delivered",90000,"Bank Transfer","Paid","LED TV","Electronics","Delhi","Elite Electronics"),
        (304,114,208,"2024-04-02",5,"Pending",125000,"UPI","Pending","Mobile Phone","Electronics","Hyderabad","Smart Electronics"),
        (305,115,204,"2024-04-03",3,"Delivered",186000,"Bank Transfer","Paid","Laptop","Electronics","Pune","Elite Electronics"),
        (306,104,202,"2024-04-03",50,"Delivered",3000,"Cash","Paid","Milk Pack","Dairy","Chennai","Fresh Dairy Ltd"),
        (307,105,202,"2024-04-04",18,"Cancelled",8100,"UPI","Cancelled","Cheese Block","Dairy","Delhi","Fresh Dairy Ltd"),
        (308,117,206,"2024-04-04",7,"Delivered",24500,"Debit Card","Paid","Mixer Grinder","Home Appliances","Kolkata","HomeNeeds Pvt Ltd"),
        (309,118,206,"2024-04-05",4,"Pending",48000,"UPI","Pending","Water Purifier","Home Appliances","Delhi","HomeNeeds Pvt Ltd"),
        (310,119,206,"2024-04-05",12,"Delivered",33600,"Cash","Paid","Ceiling Fan","Home Appliances","Ahmedabad","HomeNeeds Pvt Ltd")
    ]
    columns = ["order_id","product_id","supplier_id","order_date","quantity","order_status",
               "bill_amount","payment_mode","payment_status","product_name","category",
               "inventory_city","supplier_name"]
    return spark.createDataFrame(data, columns)

# 89 ,90 ,91 silver
@dlt.table(name="silver_orders")
@dlt.expect_or_drop("valid_order_id",  "order_id IS NOT NULL")
@dlt.expect_or_drop("valid_bill",      "bill_amount > 0")
@dlt.expect_or_drop("no_cancelled",    "order_status != 'Cancelled'")
def silver_orders():
    return (
        dlt.read("bronze_orders")
        .withColumn("order_date", to_date(col("order_date"), "yyyy-MM-dd"))
        .withColumn("order_status",
            when(col("order_status").isNull(), "Unknown")
            .otherwise(col("order_status")))
        .withColumn("total_revenue", col("bill_amount") + col("quantity") * 100)
    )

# 92  gold1
@dlt.table(name="gold_city_revenue")
def gold_city_revenue():
    return (
        dlt.read("silver_orders")
        .groupBy("inventory_city")
        .agg(sum("total_revenue").alias("total_revenue"))
    )

# 93 gold2
@dlt.table(name="gold_category_revenue")
def gold_category_revenue():
    return (
        dlt.read("silver_orders")
        .groupBy("category")
        .agg(sum("total_revenue").alias("total_revenue"))
    )