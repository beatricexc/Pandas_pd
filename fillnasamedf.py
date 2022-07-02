import pandas as pd

df = pd.read_csv('data.csv')

df['Calories'].fillna(130, inplace=True) # replace NULL values with 130 only in the 'Calories' column
                                         # Reminder: the fillna argument returns the df with the alterations we made but does not create a new df,
                                         # meaning it performs the method on the original df

print(df.to_string()) #returns full df, usually it is truncated to display just 5 rows with .head or .tail
