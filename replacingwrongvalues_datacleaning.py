import pandas as pd

df= pd.read_csv('data.csv')

df.loc[7, 'Duration'] = 45 #replacing a value inside the 'Duration' column with value 45

print(df.to_string()) 

# method working only on small datasets
