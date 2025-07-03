import pandas as pd

df = pd.read_csv("epd_202504.csv")
print(df.head())  # Display the first few rows of the DataFrame
print(df.columns)
print(df.shape)  # Display the shape of the DataFrame
print(df.info())    # Display information about the DataFrame
print(df.describe())  # Display summary statistics of the DataFrame        
print(df.tail())