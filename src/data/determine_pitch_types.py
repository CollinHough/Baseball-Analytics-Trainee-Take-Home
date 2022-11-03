# Collin Hough
# 2023 Baseball Analytics Trainee Take Home
# PART 2

import pandas as pd

data = pd.read_excel('../../data/raw/2023 Analytics Internship Problem Dataset.xlsx')

# Separate data into pitcher A set and pitcher B set
pitcher_A_data = data[data["PITCHER_KEY"] == "A"]
pitcher_B_data = data[data["PITCHER_KEY"] == "B"]
pitcher_A_data.to_csv('../../data/processed/part2/pitcher_A_data.csv')
pitcher_B_data.to_csv('../../data/processed/part2/pitcher_B_data.csv')

# Determine types of pitches each pitcher has
pitch_types_A = pitcher_A_data.PITCH_TYPE_KEY.unique()
pitch_types_B = pitcher_B_data.PITCH_TYPE_KEY.unique()
print("Player A has pitch types: " + str(pitch_types_A))
print("Player B has pitch types: " + str(pitch_types_B))

# Player A Pitch Types:
# 1. FB = Fastball - Two-Seam Fastball?
# 2. CU = Curveball
# 3. SL = Slider
# 4. CH = Changeup
# 5. FF = Four-Seam Fastball
# 6. UN = Unknown?

# Player B Pitch Types:
# 1. FB = Fastball - Two-Seam Fastball?
# 2. CB = Curveball
# 3. SL = Slider
# 4. CH = Changeup
# 5. FF = Four-Seam Fastball
# 6. UN = Unknown?
# 7. SI = Sinker


