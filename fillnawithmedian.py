import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True)

print(df.to_string())


#in row 18 and 28, the empty values from "Calories" was replaced with
#the median: 291.2
