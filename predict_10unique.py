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
    predicted_numbers = set()
    predicted_stars = set()

    # Gebruik een lege of random feature vector met de juiste grootte (7 getallen)
    random_features = Vectors.dense([
        random.randint(1, 50),  # Nummer 1
        random.randint(1, 50),  # Nummer 2
        random.randint(1, 50),  # Nummer 3
        random.randint(1, 50),  # Nummer 4
        random.randint(1, 50),  # Nummer 5
        random.randint(1, 12),  # Ster 1
        random.randint(1, 12)   # Ster 2
    ])

    feature_df = spark.createDataFrame([(random_features,)], ["features"])

    # Voorspel alle 5 nummers
    for i in range(1, 6):
        prediction = int(models[f"Nummer_{i}"].transform(feature_df).select("prediction").collect()[0][0])
        while prediction in predicted_numbers:
            prediction = random.randint(1, 50)  # Zorg voor unieke nummers
        predicted_numbers.add(prediction)

    # Voorspel beide sterren
    for i in range(1, 3):
        prediction = int(models[f"Ster_{i}"].transform(feature_df).select("prediction").collect()[0][0])
        while prediction in predicted_stars:
            prediction = random.randint(1, 12)  # Zorg voor unieke sterren
        predicted_stars.add(prediction)

    # Voeg de voorspelling toe aan de lijst
    predicted_tickets.append((sorted(predicted_numbers), sorted(predicted_stars)))

# Print alle voorspelde EuroMillions tickets
print("\n🎰 10 Voorspelde EuroMillions Nummers 🎰\n")
for i, (numbers, stars) in enumerate(predicted_tickets, start=1):
    print(f"📜 Ticket {i}: 🔢 {numbers} ⭐ {stars}")

