# Collin Hough
# 2023 Baseball Analytics Trainee Take Home
# PART 1

import pandas as pd

df = pd.read_excel('../../data/raw/2023 Analytics Internship Problem Dataset.xlsx')

# Get data for making predictions with the model
data = df[df["INDUCED_VERTICAL_BREAK"].isna()]
data.to_csv("../../data/processed/check.csv")
x_predict = data.loc[:,data.columns != "INDUCED_VERTICAL_BREAK"]
x_predict.to_csv("../../data/processed/x_predict.csv")
