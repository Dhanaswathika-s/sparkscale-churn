from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Save Output") \
    .getOrCreate()

# Read data
df = spark.read.csv("/data/sample.csv", header=True, inferSchema=True)

# Transformation
df_filtered = df.filter(df.age > 23)

# Save output
df_filtered.coalesce(1).write.mode("overwrite").csv("/data/output", header=True)

print("Output saved successfully!")

spark.stop()
