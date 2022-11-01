# Collin Hough
# 2023 Baseball Analytics Trainee Take Home
# PART 1
import pandas as pd
from sklearn import linear_model
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# Define features to train model with
features = ["RELEASE_SPEED",
            "SPIN_DIRECTION",
            "VERTICAL_APPROACH_ANGLE"]

# Load in feature and results data
X_train = pd.read_csv('../../data/processed/X_train.csv')
X_test = pd.read_csv('../../data/processed/X_test.csv')
y_train = pd.read_csv('../../data/processed/y_train.csv')
y_test = pd.read_csv('../../data/processed/y_test.csv')

# Clean data before training model
X_train = X_train[features]
X_test = X_test[features]
y_train = y_train["INDUCED_VERTICAL_BREAK"]
y_test = y_test["INDUCED_VERTICAL_BREAK"]

reg = make_pipeline(StandardScaler(),
                    linear_model.SGDRegressor(max_iter=1000, tol=1e-3))
reg.fit(X_train, y_train)

# Check score
r_squared = reg.score(X_test,y_test)
print("R_squared = " + str(r_squared))


# Make prediction for INDUCED_VERTICAL_BREAK
X_predict = pd.read_csv('../../data/processed/X_predict.csv')
y_pred = reg.predict(X_test)
df = pd.DataFrame(y_pred,columns=["INDUCED_VERTICAL_BREAK_PRED"])
df.to_csv('../../data/processed/break.csv')
