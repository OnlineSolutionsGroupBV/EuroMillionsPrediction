# Euromillion prediction
EuroMillionsPrediction

That’s my Saturday morning project—I’d like to explore different projects and frameworks to understand how they work, particularly in predicting certain numbers. This example is quite simple and fun, in my opinion, because if you manage to "hack" something like this, it could be highly profitable. For instance, the EuroMillions jackpot currently stands at 178 million euros.

It's exciting to spend a Saturday studying different technologies and prediction algorithms. I'll start with Apache Spark and then add other frameworks and examples if I find them interesting. I'll see how it goes based on my first experience. I don't come across many projects that are both educational and enjoyable, but this kind of research can expand knowledge and potentially be useful for more practical applications.

Regarding Python, which of these examples would be the most suitable for calculating and predicting a EuroMillions winning combination, where 5 numbers are selected from 1 to 50 and 2 lucky stars from 1 to 12? 

# EuroMillion Prediction Using Apache Spark

## Overview
This project aims to predict potential EuroMillions winning number combinations using Apache Spark's Machine Learning (ML) capabilities. The EuroMillions lottery consists of selecting 5 numbers from 1 to 50 and 2 lucky stars from 1 to 12. While the lottery is inherently random, this project attempts to identify patterns and trends using historical data and machine learning models.

## Features
- Data preprocessing and analysis of historical EuroMillions draws
- Machine Learning (ML) model training using Apache Spark's `pyspark.ml`
- Exploratory Data Analysis (EDA) to detect trends and patterns
- Model evaluation and validation

## Technologies Used
- **Apache Spark (`pyspark`)**
- **Python**

### Setup
1. Clone the repository:
   ```sh
    git clone git clone https://github.com/OnlineSolutionsGroupBV/EuroMillionsPrediction.git
    cd EuroMillionsPrediction
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   python3 -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   pip3 install pyspark
   ```
3. Ensure Spark is installed and configured correctly:
   ```sh
    pyspark
   ```

   If Spark is not installed, refer to [Apache Spark's installation guide](https://spark.apache.org/docs/latest/) for setup instructions.

## Data Preparation
1. Obtain historical EuroMillions draw results from an official source or dataset.
2. Save the dataset in a CSV file (`EuroMillionsData/euromillions-gamedata-NL-****.csv`).
3. Prepare Data for Machine Learning. We need to convert the numbers into a format suitable for a Random Forest Classifier. Feature Engineering. We combine the 5 drawn numbers and 2 lucky stars into a single feature vector.
4. Run the data preprocessing scripts:
   ```sh
   spark-submit load_data.py # Read the CSV File in PySpark
   spark-submit prepare_data.py
   ```

**train_model.py (Train Multi-Output Random Forest Model)**  

**Objective:**  
- Train 7 separate models (one for each digit).  
- Save all trained models.
  
```sh
spark-submit train_model.py
```

## Running the Prediction Model

```sh
spark-submit predict.py
```
This will train the ML model and generate predictions.

**What’s Happening?**  
The model is relying too much on the input values, causing its predictions to closely resemble the input. This could be due to overfitting or the model struggling to identify meaningful patterns in the historical lottery data.  

### 🎯 What We Want  
Instead of generating predictions that mirror the input, we want the model to independently produce a full prediction without being influenced by a predefined draw sequence.  

### ✅ Solution: Predict Fully Random Numbers  
Rather than using an existing draw as input, we can have the model generate predictions without any input.  

### 🔹 Our Approach:  
- Provide an empty input (zero values) and ask the model to generate a completely new set of numbers.  
- This prevents the model from simply copying the input.  
- The model will rely on underlying patterns in the dataset to create a more realistic combination.

... 
🎰 Voorspelde EuroMillions Nummers:
🔢 Nummers: 4, 10, 13, 23, 43
⭐ Sterren: 5, 9

## Example ML Models Used
- **Logistic Regression**: Used for binary classification of number occurrences.
- **Random Forest Classifier**: Used for predicting number frequencies.
- **Gradient Boosted Trees**: Enhances prediction accuracy by combining multiple weak classifiers.

## Results and Visualization
Once the model runs successfully, the predicted number combinations will be saved in `output/predictions.txt`. Visualization scripts are included for analyzing draw patterns.

## Disclaimer
This project is for educational and experimental purposes only. Lottery outcomes are inherently random, and no prediction model guarantees success.

## License
This project is open-source under the **MIT License**. Contributions are welcome!

