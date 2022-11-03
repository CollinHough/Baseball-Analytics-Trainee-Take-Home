# Collin Hough
# 2023 Baseball Analytics Trainee Take Home
# PART 2

import pandas as pd
from sklearn import linear_model
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Define features to train model with
features = ["PLATE_X",
            "PLATE_Z",
            "VERTICAL_APPROACH_ANGLE"]

# Load in feature and results data
X_train = pd.read_csv('../../data/processed/part2/X_train.csv')
X_test = pd.read_csv('../../data/processed/part2/X_test.csv')
y_train = pd.read_csv('../../data/processed/part2/y_train.csv')
y_test = pd.read_csv('../../data/processed/part2/y_test.csv')

# Clean data before training model
X_train = X_train[features]
X_test = X_test[features]

# Encode y vectors
y_train = y_train["PITCH_RESULT_KEY"]
le = LabelEncoder()
le.fit(y_train)
y_train_encoded = le.transform(y_train)
y_test = y_test["PITCH_RESULT_KEY"]
y_test_encoded = le.transform(y_test)

# Create classification model and fit data
reg = make_pipeline(StandardScaler(),
                    linear_model.SGDClassifier(max_iter=1000, tol=1e-3))
reg.fit(X_train, y_train_encoded)

# Check score
r_squared = reg.score(X_test,y_test_encoded)
print("R_squared = " + str(r_squared))

# Make prediction for Player A PITCH_RESULT_KEY
X_predict_A = pd.read_csv('../../data/processed/part2/X_predict_A.csv')
y_pred = reg.predict(X_predict_A[["PLATE_X","PLATE_Z","VERTICAL_APPROACH_ANGLE"]])
df = pd.DataFrame(y_pred,columns=["PITCH_RESULT_PRED"])
df.to_csv('../../data/processed/part2/pitch_result_pred_A.csv')

# # Make prediction for Player B PITCH_RESULT_KEY
X_predict_B = pd.read_csv('../../data/processed/part2/X_predict_B.csv')
y_pred = reg.predict(X_predict_B[["PLATE_X","PLATE_Z","VERTICAL_APPROACH_ANGLE"]])
df = pd.DataFrame(y_pred,columns=["PITCH_RESULT_PRED"])
df.to_csv('../../data/processed/part2/pitch_result_pred_B.csv')
