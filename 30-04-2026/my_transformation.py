import dlt
from pyspark.sql.functions import col, sum, count, upper

@dlt.table(
    name="bronze_sales_inline"
)
def bronze_sales_inline():
    data = [
        (1, "Amit Sharma", "Hyderabad", "Laptop", 1, 75000),
        (2, "Priya Reddy", "Bangalore", "Mobile", 2, 30000),
        (3, "Rohan Mehta", "Mumbai", "Tablet", 1, 25000),
        (4, "Sneha Iyer", "Chennai", "Laptop", 1, 72000),
        (5, "Kiran Patel", "Hyderabad", "Mouse", 5, 600),
        (6, "Ananya Das", "Kolkata", "Keyboard", 3, 1500),
        (7, "Vikram Singh", "Delhi", "Monitor", 2, 12000),
        (8, "Meera Nair", "Bangalore", "Mobile", 1, 28000)
    ]

    columns = [
        "order_id",
        "customer_name",
        "city",
        "product",
        "quantity",
        "price"
    ]

    return spark.createDataFrame(data, columns)


@dlt.table(
    name="silver_sales_cleaned"
)
def silver_sales_cleaned():
    df = dlt.read("bronze_sales_inline")

    return df.select(
        col("order_id"),
        upper(col("customer_name")).alias("customer_name"),
        upper(col("city")).alias("city"),
        upper(col("product")).alias("product"),
        col("quantity").cast("int"),
        col("price").cast("int"),
        (col("quantity") * col("price")).alias("revenue")
    ).filter(
        (col("quantity") > 0) & (col("price") > 0)
    )

@dlt.table(
    name="gold_city_sales_summary"
)
def gold_city_sales_summary():
    df = dlt.read("silver_sales_cleaned")

    return df.groupBy("city").agg(
        count("*").alias("total_orders"),
        sum("quantity").alias("total_quantity"),
        sum("revenue").alias("total_revenue")
    )