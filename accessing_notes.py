import pandas as pd
import numpy as np

# Reset df 
languages = pd.Series(["Python","JavaScript","HTML","SQL","PHP","Java","TypeScript"])
popularity = pd.Series([3,1,2,4,11,7,5])
df = pd.DataFrame({
    "Languages": languages,
    "Ranking 2024": popularity
})
df = df.set_index("Languages")
df.insert(1,"Ranking 2023", [3,1,2,4,11,7,5])
df.insert(2,"Ranking 2022", [4,1,2,3,10,6,5])
df.insert(3,"Ranking 2021", [3,1,2,4,11,5,7])
df.insert(4,"Ranking 2020", [4,1,2,3,8,5,9])
df.insert(5,"Ranking 2019", [4,1,2,3,8,5,10])
print(df)

print(df[["Ranking 2019"]])
print(df[["Ranking 2020", "Ranking 2019"]])

print(df.loc["Java"])

print("*********************")
print(df.loc[::,::])

#Activity 1
print(df.loc[:"HTML":1,"Ranking 2023"::2])

#Slide 16
print(df.iloc[:3:,1::2])

#Slide 20
print(df.loc["HTML", "Ranking 2024"])
print(df.iloc[2,0])
print(df.at["HTML", "Ranking 2024"])

print(df.head(1))

#try
print(df.head(0))

print(df.head())