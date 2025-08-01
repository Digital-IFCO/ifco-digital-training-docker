import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp
from pyspark import SparkConf

conf = SparkConf()
conf.set("spark.hadoop.hadoop.security.authentication", "simple")

# 📌 JDBC configuración para PostgreSQL
POSTGRES_URL = "jdbc:postgresql://pg:5432/visits_db"
POSTGRES_PROPERTIES = {
    "user": "demo",
    "password": "demo",
    "driver": "org.postgresql.Driver"
}

# 🚀 Crea SparkSession con configuración robusta
spark = SparkSession.builder \
    .appName("VisitProcessor") \
    .config("spark.jars", "/opt/spark/jars/postgresql-42.2.5.jar") \
    .config("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.LocalFileSystem") \
    .getOrCreate()

# 📄 Carga archivo CSV local desde volumen montado
df = spark.read.option("header", True).csv("/data/input.csv")

# 🧹 Transforma columnas
df = df.withColumn("duration_seconds", col("duration_seconds").cast("int"))
df = df.withColumn("visit_timestamp", to_timestamp("visit_timestamp"))

# 🛢️ Escribe en PostgreSQL
df.write.jdbc(
    url=POSTGRES_URL,
    table="raw_visits",
    mode="overwrite",
    properties=POSTGRES_PROPERTIES
)

print("✅ Datos cargados en PostgreSQL → tabla: raw_visits")

# 🧼 Limpia recursos
spark.stop()