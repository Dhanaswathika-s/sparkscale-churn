from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Data Transformation") \
    .getOrCreate()

# Read input
df = spark.read.csv("/data/sample.csv", header=True, inferSchema=True)

# Transformation
df_filtered = df.filter(df.age > 23)

# Show result
df_filtered.show()

# Save output to folder
df_filtered.write.mode("overwrite").csv("/data/output", header=True)

spark.stop()
