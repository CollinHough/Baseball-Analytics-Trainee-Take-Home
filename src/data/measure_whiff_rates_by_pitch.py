# Collin Hough
# 2023 Baseball Analytics Trainee Take Home
# PART 1

import pandas as pd

# Load pitcher A data and pitcher B data
pitcher_A_data = pd.read_csv('../../data/processed/pitcher_A.csv')
pitcher_B_data = pd.read_csv('../../data/processed/pitcher_B.csv')

# Determine types of pitches each pitcher has
pitch_types_A = pitcher_A_data.PITCH_TYPE_KEY.unique()
pitch_types_B = pitcher_B_data.PITCH_TYPE_KEY.unique()

pitch_df = pd.DataFrame(columns=['PITCHER_KEY','PITCH_TYPE','TIMES_THROWN','SWINING_STRIKES','SWING_AND_MISS_RATE','USAGE_RATE'])
# Determine swing and miss rate of each pitch for player A
for i, pitch in enumerate(pitch_types_A):
    # Find total amount of times pitch was thrown and total amount of swinging strikes
    pitch_data = pitcher_A_data[pitcher_A_data["PITCH_TYPE_KEY"] == pitch]
    times_thrown = len(pitch_data.index)
    swinging_strikes = pitch_data[pitch_data["PITCH_RESULT_KEY"] == "StrikeSwinging"]
    swinging_strikes_count = len(swinging_strikes.index)
    # Record all data into new dataframe
    swing_and_miss = (swinging_strikes_count/times_thrown)*100
    usage = (times_thrown/len(pitcher_A_data.index))*100
    pitch_df.loc[i] = ["A",pitch,str(times_thrown),str(swinging_strikes_count),str(swing_and_miss),str(usage)]

for i, pitch in enumerate(pitch_types_B):
    # Find total amount of times pitch was thrown and total amount of swinging strikes
    pitch_data = pitcher_B_data[pitcher_B_data["PITCH_TYPE_KEY"] == pitch]
    times_thrown = len(pitch_data.index)
    swinging_strikes = pitch_data[pitch_data["PITCH_RESULT_KEY"] == "StrikeSwinging"]
    swinging_strikes_count = len(swinging_strikes.index)
    # Record all data into new dataframe
    swing_and_miss = (swinging_strikes_count/times_thrown)*100
    usage = (times_thrown/len(pitcher_B_data.index))*100
    pitch_df.loc[i+len(pitch_types_A)] = ["B",pitch,str(times_thrown),str(swinging_strikes_count),str(swing_and_miss),str(usage)]

# Save data
pitch_df.to_csv('../../data/processed/pitch_data.csv')
