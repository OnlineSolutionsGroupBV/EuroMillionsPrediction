from pyspark.sql import SparkSession
from pyspark.ml.classification import RandomForestClassificationModel
from pyspark.ml.linalg import Vectors
import random

# Start Spark session
spark = SparkSession.builder.appName("PredictEuroMillions").getOrCreate()

# Laad alle getrainde modellen
model_paths = {
    "Nummer_1": "models/euromillions_rf_Nummer_1",
    "Nummer_2": "models/euromillions_rf_Nummer_2",
    "Nummer_3": "models/euromillions_rf_Nummer_3",
    "Nummer_4": "models/euromillions_rf_Nummer_4",
    "Nummer_5": "models/euromillions_rf_Nummer_5",
    "Ster_1": "models/euromillions_rf_Ster_1",
    "Ster_2": "models/euromillions_rf_Ster_2"
}

models = {key: RandomForestClassificationModel.load(path) for key, path in model_paths.items()}

# Aantal voorspellingen die we willen genereren
num_predictions = 10

# Lijst om voorspelde kaarten op te slaan
predicted_tickets = []

for _ in range(num_predictions):
    # Genereer een random startwaarde voor het model
    random_input = Vectors.dense([
        random.randint(1, 50),  # Nummer 1
        random.randint(1, 50),  # Nummer 2
        random.randint(1, 50),  # Nummer 3
        random.randint(1, 50),  # Nummer 4
        random.randint(1, 50),  # Nummer 5
        random.randint(1, 12),  # Ster 1
        random.randint(1, 12)   # Ster 2
    ])

    # Voorspel alle getallen zonder bestaande invoer te kopiëren
    predictions = {col: models[col].transform(spark.createDataFrame([(random_input,)], ["features"])).select("prediction").collect()[0][0]
                   for col in model_paths.keys()}

    # Sla de voorspelling op als een tuple
    predicted_tickets.append([
        int(predictions["Nummer_1"]),
        int(predictions["Nummer_2"]),
        int(predictions["Nummer_3"]),
        int(predictions["Nummer_4"]),
        int(predictions["Nummer_5"]),
        int(predictions["Ster_1"]),
        int(predictions["Ster_2"])
    ])

# Print alle voorspelde EuroMillions tickets
print("\n🎰 10 Voorspelde EuroMillions Nummers 🎰\n")
for i, ticket in enumerate(predicted_tickets, start=1):
    print(f"📜 Ticket {i}: 🔢 {ticket[:5]} ⭐ {ticket[5:]}")

