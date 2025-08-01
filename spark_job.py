import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp
from pyspark import SparkConf

conf = SparkConf()
conf.set("spark.hadoop.hadoop.security.authentication", "simple")

# 📌 JDBC configuration for PostgreSQL
POSTGRES_URL = "jdbc:postgresql://pg:5432/visits_db"
POSTGRES_PROPERTIES = {
    "user": "demo",
    "password": "demo",
    "driver": "org.postgresql.Driver"
}

# 🚀 Create SparkSession with robust configuration
spark = SparkSession.builder \
    .appName("VisitProcessor") \
    .config("spark.jars", "/opt/spark/jars/postgresql-42.2.5.jar") \
    .config("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.LocalFileSystem") \
    .getOrCreate()

# 📄 Load local CSV file from mounted volume
df = spark.read.option("header", True).csv("/data/input.csv")

# 🧹 Transform columns
df = df.withColumn("duration_seconds", col("duration_seconds").cast("int"))
df = df.withColumn("visit_timestamp", to_timestamp("visit_timestamp"))

# 🛢️ Write to PostgreSQL
df.write.jdbc(
    url=POSTGRES_URL,
    table="raw_visits",
    mode="overwrite",
    properties=POSTGRES_PROPERTIES
)

print("✅ Data loaded to PostgreSQL → table: raw_visits")

# 🧼 Clean up resources
spark.stop()