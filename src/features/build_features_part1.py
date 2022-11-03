# Collin Hough
# 2023 Baseball Analytics Trainee Take Home
# PART 1

import pandas as pd
from sklearn.feature_selection import SelectKBest, mutual_info_regression

# Load data
X_train = pd.read_csv('../../data/processed/part1/X_train.csv')
y_train = pd.read_csv('../../data/processed/part1/y_train.csv')
selector = SelectKBest(mutual_info_regression, k=3)
y_train = y_train["INDUCED_VERTICAL_BREAK"]

# Find best numeric columns for estimating INDUCED_VERTICAL_BREAK
selector.fit(X_train,y_train)
print(X_train.columns[selector.get_support()])
# After running this, our 3 best features are:
# 1. RELEASE_SPEED
# 2. SPIN_DIRECTION
# 3. VERTICAL_APPROACH_ANGLE