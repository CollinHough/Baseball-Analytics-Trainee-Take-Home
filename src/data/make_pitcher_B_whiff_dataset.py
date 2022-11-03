# Collin Hough
# 2023 Baseball Analytics Trainee Take Home
# PART 2

import pandas as pd
import numpy as np
import math

# Load in pitcher B data
pitcher_B_data = pd.read_csv("../../data/processed/part2/pitcher_B_data.csv")

# Isolate PLATE_X, PLATE_Z, AND VERTICAL_APPROACH_ANGLE
pitcher_B_data = pitcher_B_data[pitcher_B_data["PITCH_TYPE_KEY"].isin(["CB","CH","SL"])]
plate_x = pitcher_B_data.loc[:,pitcher_B_data.columns == "PLATE_X"]
plate_z = pitcher_B_data.loc[:,pitcher_B_data.columns == "PLATE_Z"]
vertical_approach_angle = pitcher_B_data.loc[:,pitcher_B_data.columns == "VERTICAL_APPROACH_ANGLE"]

# Define statistical parameters
confidence = 0.95
sample_size = len(plate_x.index)

# Determine confidence interval for PLATE_X
plate_x_mean = plate_x["PLATE_X"].mean()
plate_x_std = plate_x["PLATE_X"].std()
plate_x_confidence_interval = [(plate_x_mean - confidence * (plate_x_std/math.sqrt(sample_size))),
                                (plate_x_mean + confidence * (plate_x_std/math.sqrt(sample_size)))]

# Determine confidence interval for PLATE_Z
plate_z_mean = plate_z["PLATE_Z"].mean()
plate_z_std = plate_z["PLATE_Z"].std()
plate_z_confidence_interval = [(plate_z_mean - confidence * (plate_z_std/math.sqrt(sample_size))),
                                (plate_z_mean + confidence * (plate_z_std/math.sqrt(sample_size)))]

# Determine confidence interval for VERTICAL_APPROACH_ANGLE
vaa_mean = vertical_approach_angle["VERTICAL_APPROACH_ANGLE"].mean()
vaa_std = vertical_approach_angle["VERTICAL_APPROACH_ANGLE"].std()
vaa_confidence_interval = [(vaa_mean - confidence * (vaa_std/math.sqrt(sample_size))),
                            (vaa_mean + confidence * (vaa_std/math.sqrt(sample_size)))]

# Create columns of randomized values that fall within confidence intervals of each parameter
plate_x_predict = np.random.uniform(plate_x_confidence_interval[0],
                                    plate_x_confidence_interval[1],
                                    size=(sample_size,1))
plate_z_predict = np.random.uniform(plate_z_confidence_interval[0],
                                    plate_z_confidence_interval[1],
                                    size=(sample_size,1))
vaa_predict = np.random.uniform(vaa_confidence_interval[0],
                                vaa_confidence_interval[1],
                                size=(sample_size,1))

# Concatenate data and save
data = np.append(plate_x_predict,plate_z_predict,axis=1)
data = np.append(data,vaa_predict,axis=1)
df = pd.DataFrame(data,columns=["PLATE_X","PLATE_Z","VERTICAL_APPROACH_ANGLE"])
print(df.head())
df.to_csv('../../data/processed/part2/X_predict_B.csv')