# Euro Millions Prediction
EuroMillionsPrediction

That’s my Saturday morning project—I’d like to explore different projects and frameworks to understand how they work, particularly in predicting certain numbers. This example is quite simple and fun, in my opinion, because if you manage to "hack" something like this, it could be highly profitable. For instance, the EuroMillions jackpot currently stands at 178 million euros.

It's exciting to spend a Saturday studying different technologies and prediction algorithms. I'll start with Apache Spark and then add other frameworks and examples if I find them interesting. I'll see how it goes based on my first experience. I don't come across many projects that are both educational and enjoyable, but this kind of research can expand knowledge and potentially be useful for more practical applications.

Regarding Python, which of these examples would be the most suitable for calculating and predicting a EuroMillions winning combination, where 5 numbers are selected from 1 to 50 and 2 lucky stars from 1 to 12? 

# EuroMillions Prediction Using Apache Spark

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

Type "help", "copyright", "credits" or "license" for more information.
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
25/03/15 12:52:56 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 3.5.5
      /_/

Using Python version 3.9.6 (default, Feb  3 2024 15:58:28)
Spark context Web UI available at http://mbp-van-sergej:4040
Spark context available as 'sc' (master = local[*], app id = local-1742039577457).
SparkSession available as 'spark'.


    ```
   If Spark is not installed, refer to [Apache Spark's installation guide](https://spark.apache.org/docs/latest/) for setup instructions.

## Data Preparation
1. Obtain historical EuroMillions draw results from an official source or dataset.
2. Save the dataset in a CSV file (`data/euromillions_history.csv`).
3. Run the data preprocessing script:
   ```sh
   python preprocess_data.py
   ```

## Running the Prediction Model
To train and test the model, execute:
```sh
spark-submit predict_numbers.py
```
This will train the ML model and generate predictions.

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

