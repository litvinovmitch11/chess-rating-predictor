import pandas as pd

files_name = ["first_240.csv", "from_240_to_360.csv", "from_360_480.csv", "from_480_to_1000.csv",
              "from_1000_to_1240.csv", "from_1240_to_2280.csv", "from_2280_to_3320.csv", "from_3320_to_4360.csv", "from_4360_to_4696.csv",
              "from_4696_to_4702.csv"]
all_df = []
for file in files_name:
    all_df.append(pd.read_csv(file))
df_moves = pd.concat(all_df)

df_moves.to_csv(f"all_processed_moves.csv", encoding='utf-8', index=False)
