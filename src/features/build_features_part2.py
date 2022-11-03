# Collin Hough
# 2023 Baseball Analytics Trainee Take Home
# PART 2

import pandas as pd
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn import preprocessing

# Load data
X_train = pd.read_csv('../../data/processed/part2/X_train.csv')
y_train = pd.read_csv('../../data/processed/part2/y_train.csv')
selector = SelectKBest(mutual_info_classif, k=3)

# Encode pitch results
y_train = y_train["PITCH_RESULT_KEY"]
le = preprocessing.LabelEncoder()
le.fit(y_train)
print(le.classes_)
y_train_encoded = le.transform(y_train)

# Find best numeric columns for estimating PITCH_RESULT_KEY == "StrikeSwinging"
selector.fit(X_train,y_train_encoded)
print(X_train.columns[selector.get_support()])

# After running this, our 3 best features are:
# 1. PLATE_X
# 2. PLATE_Z
# 3. VERTICAL_APPROACH_ANGLE