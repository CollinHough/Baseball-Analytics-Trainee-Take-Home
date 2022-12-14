# Collin Hough
# 2023 Baseball Analytics Trainee Take Home
# PART 1

import pandas as pd

df = pd.read_excel('../../data/raw/2023 Analytics Internship Problem Dataset.xlsx')

# Get data for making predictions with the model
data = df[df["INDUCED_VERTICAL_BREAK"].isna()]
X_predict = data.loc[:,data.columns != "INDUCED_VERTICAL_BREAK"]
X_predict.to_csv("../../data/processed/part1/X_predict.csv")
