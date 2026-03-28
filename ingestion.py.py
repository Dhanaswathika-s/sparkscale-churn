from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Data Ingestion") \
    .getOrCreate()

df = spark.read.csv("/data/sample.csv", header=True, inferSchema=True)

df.show()

spark.stop()
