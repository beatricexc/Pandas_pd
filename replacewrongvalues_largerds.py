import pandas as pd

df = pd.read_csv('data.csv')

for x in df.index: #replaces any values > 120 with 120
    if df.loc[x, "Duration"]> 120:
              df.loc[x, "Duration"] = 120

              #setting boundraies for legal values in case of larger datasets

print(df.to_string())
