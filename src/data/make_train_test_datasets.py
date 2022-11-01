# Collin Hough
# 2023 Baseball Analytics Trainee Take Home
# PART 1

import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
#from pandasql import sqldf

df = pd.read_excel('../../data/raw/2023 Analytics Internship Problem Dataset.xlsx')

# Get data for training and testing the model
train = df[~df["INDUCED_VERTICAL_BREAK"].isna()]
train.to_csv('../../data/processed/train.csv')

# Split data into features and results
X = train.loc[:,train.columns != "INDUCED_VERTICAL_BREAK"]
y = train.loc[:,train.columns == "INDUCED_VERTICAL_BREAK"]

# Create training and testing datasets
X_train,X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
X_train.to_csv('../../data/processed/X_train.csv')
y_train.to_csv('../../data/processed/y_train.csv')
X_test.to_csv('../../data/processed/X_test.csv')
y_test.to_csv('../../data/processed/y_test.csv')