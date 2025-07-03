import pandas as pd
import numpy as np

languages = pd.Series(["Python","JavaScript","HTML","SQL"])
print(languages)
popularity = pd.Series([3,1,2,4])
print(popularity)

df = pd.DataFrame([("Anne",30),("Bill", 27),("Charlie", 55)])
print(df)

df = pd.DataFrame([("Anne",30),("Bill", 27),("Charlie", 55)],
                  columns=["Name","Age"])
print(df)

df = pd.DataFrame({
    "Languages": languages,
    "Ranking": popularity
})
print(df)

df = pd.concat([languages,popularity],axis=1)
df.columns = ["Languages", "Ranking"]
print(df)

df=pd.read_csv("speeds.csv")
print(df)

df=pd.read_excel("speeds.xlsx")
print(df)