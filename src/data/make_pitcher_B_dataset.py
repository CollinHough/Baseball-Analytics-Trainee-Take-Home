# Collin Hough
# 2023 Baseball Analytics Trainee Take Home
# PART 1

import pandas as pd

hit_types = ["single","double","triple","home_run"]

# Load pitcher B data
pitcher_B_data = pd.read_csv('../../data/processed/part2/pitcher_B_data.csv')

# Determine types of pitches pitcher has
pitch_types_B = pitcher_B_data.PITCH_TYPE_KEY.unique()

# Determine swing and miss rate of each pitch for player B
pitch_df = pd.DataFrame(columns=['PITCHER_KEY','PITCH_TYPE','TIMES_THROWN','SWINING_STRIKES','SWING_AND_MISS_RATE','USAGE_RATE','HIT_RATE','BASES_PER_HIT'])
for i, pitch in enumerate(pitch_types_B):

    # Find total amount of times pitch was thrown and total amount of swinging strikes
    pitch_data = pitcher_B_data[pitcher_B_data["PITCH_TYPE_KEY"] == pitch]
    times_thrown = len(pitch_data.index)
    swinging_strikes = pitch_data[pitch_data["PITCH_RESULT_KEY"] == "StrikeSwinging"]
    swinging_strikes_count = len(swinging_strikes.index)
    hits = pitch_data[pitch_data["EVENT_RESULT_KEY"].isin(hit_types)]
    hit_count = len(hits.index)

    # Calculate statistics and record data
    swing_and_miss = (swinging_strikes_count/times_thrown)*100
    usage = (times_thrown/len(pitcher_B_data.index))*100
    at_bats = pitch_data["BATTER_IN_INNING_KEY"]
    hit_rate = (len(hits.index)/times_thrown) * 100
    singles = hits[hits["EVENT_RESULT_KEY"] == "single"]
    doubles = hits[hits["EVENT_RESULT_KEY"] == "double"]
    triples = hits[hits["EVENT_RESULT_KEY"] == "triple"]
    home_runs = hits[hits["EVENT_RESULT_KEY"] == "home_run"]
    if hit_count:
        bases_per_hit = (len(singles.index) + 
                                2*len(doubles.index) + 
                                3*len(triples.index) + 
                                4*len(home_runs.index))/hit_count
    else:
        bases_per_hit = 0

    #slugging_percentage = pass
    pitch_df.loc[i] = ["B",
                        pitch,str(times_thrown),
                        str(swinging_strikes_count),
                        str(swing_and_miss),
                        str(usage),
                        str(hit_rate),
                        str(bases_per_hit)]
# Save data
pitch_df.to_csv('../../data/processed/part2/pitcher_B_stats.csv')