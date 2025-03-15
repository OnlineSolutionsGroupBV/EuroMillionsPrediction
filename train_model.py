from pyspark.sql import SparkSession
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# Start Spark session
spark = SparkSession.builder.appName("TrainEuroMillionsModel").getOrCreate()

# Laad de voorbereide data
df = spark.read.parquet("data/euromillions_prepared.parquet")

# Train-test split
train_data, test_data = df.randomSplit([0.8, 0.2], seed=42)

# Functie om een model te trainen voor een bepaalde kolom
def train_and_save_model(label_col, model_name):
    rf = RandomForestClassifier(featuresCol="features", labelCol=label_col, numTrees=50, maxDepth=5)
    model = rf.fit(train_data)
    model.write().overwrite().save(f"models/{model_name}")
    return model

# Train een model voor elk van de 7 kolommen
model_columns = ["Nummer_1", "Nummer_2", "Nummer_3", "Nummer_4", "Nummer_5", "Ster_1", "Ster_2"]
models = {col: train_and_save_model(col, f"euromillions_rf_{col}") for col in model_columns}

print("Alle modellen getraind en opgeslagen.")

