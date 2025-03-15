from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler

# Start Spark session
spark = SparkSession.builder.appName("PrepareEuroMillionsData").getOrCreate()

# Laad de dataset
df = spark.read.parquet("data/euromillions.parquet")

# Feature Engineering: combineer de datum (optioneel)
assembler = VectorAssembler(inputCols=["Nummer_1", "Nummer_2", "Nummer_3", "Nummer_4", "Nummer_5", "Ster_1", "Ster_2"],
                            outputCol="features")

df_prepared = assembler.transform(df).select("features", "Nummer_1", "Nummer_2", "Nummer_3", "Nummer_4", "Nummer_5", "Ster_1", "Ster_2")

# Opslaan van voorbereide data
df_prepared.write.mode("overwrite").parquet("data/euromillions_prepared.parquet")

print("Data voorbereid en opgeslagen.")

