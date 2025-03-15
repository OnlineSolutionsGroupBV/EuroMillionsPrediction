from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Initialize Spark session
spark = SparkSession.builder.appName("EuroMillionsPrediction").getOrCreate()

# Define the path to the data folder
data_path = "EuroMillionsData/*.csv"  # Update with your actual folder path

# Define schema
schema = StructType([
    StructField("Datum", StringType(), True),
    StructField("Nummer_1", IntegerType(), True),
    StructField("Nummer_2", IntegerType(), True),
    StructField("Nummer_3", IntegerType(), True),
    StructField("Nummer_4", IntegerType(), True),
    StructField("Nummer_5", IntegerType(), True),
    StructField("Ster_1", IntegerType(), True),
    StructField("Ster_2", IntegerType(), True)
])

# Load all CSV files
df = spark.read.csv(data_path, header=True, sep=";", schema=schema)

# Opslaan als Parquet
df.write.mode("overwrite").parquet("data/euromillions.parquet")

# Show sample data
df.show(10)

