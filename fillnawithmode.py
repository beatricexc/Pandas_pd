import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mode() #mode is the value that appears most frequently

df["Calories"].fillna(x, inplace = True)

print(df.to_string())
