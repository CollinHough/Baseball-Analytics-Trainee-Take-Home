# Collin Hough
# 2023 Baseball Analytics Trainee Take Home
# PART 2

import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split

df = pd.read_excel('../../data/raw/2023 Analytics Internship Problem Dataset.xlsx')

# Discard empty data
train = df[~df["INDUCED_VERTICAL_BREAK"].isna()]
train = df[~df["PITCH_RESULT_KEY"].isna()]
print(train.head())
train.drop(['B','S','O','BU','FB','GB','LD','PU','1BO','2BO','3BO'],axis=1,inplace=True)

# Split data into features and results
X = train.loc[:,train.columns != "PITCH_RESULT_KEY"]
y = train.loc[:,train.columns == "PITCH_RESULT_KEY"]

# Create training and testing datasets
X_train,X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

# Fill in missing data values using interpolation and discard strings/chars
X_train = X_train.select_dtypes(include='number')
X_train.interpolate(method='linear',limit_direction='backward',inplace=True)
X_test = X_test.select_dtypes(include='number')
X_test.interpolate(method='linear',limit_direction='backward',inplace=True)

# Output as csv files
X_train.to_csv('../../data/processed/part2/X_train.csv')
y_train.to_csv('../../data/processed/part2/y_train.csv')
X_test.to_csv('../../data/processed/part2/X_test.csv')
y_test.to_csv('../../data/processed/part2/y_test.csv')
