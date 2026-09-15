# Execute in a Fabric PySpark notebook with the target Lakehouse attached.
from pyspark.sql import SparkSession, functions as F, types as T

spark = SparkSession.builder.getOrCreate()
schema = T.StructType([
    T.StructField("sale_id", T.IntegerType(), False),
    T.StructField("sale_date", T.DateType(), False),
    T.StructField("region", T.StringType(), False),
    T.StructField("quantity", T.IntegerType(), False),
    T.StructField("unit_price", T.IntegerType(), False),
])
sales = spark.read.option("header", True).schema(schema).csv("Files/sales/sales.csv")
invalid = sales.filter(F.col("sale_id").isNull() | F.col("sale_date").isNull() | F.col("region").isNull() | F.col("quantity").isNull() | F.col("unit_price").isNull() | (F.col("quantity") <= 0) | (F.col("unit_price") < 0))
if invalid.limit(1).count():
    raise ValueError("Invalid sales input; Delta table was not changed")
if sales.select("sale_id").distinct().count() != sales.count():
    raise ValueError("Duplicate sale IDs; Delta table was not changed")
sales.withColumn("revenue", F.col("quantity") * F.col("unit_price")).write.format("delta").mode("overwrite").saveAsTable("sales")
