import pandas as pd
import numpy as np

# languages = pd.Series(["Python","JavaScript","HTML","SQL"])
# # print(languages)
# popularity = pd.Series([3,1,2,4])
# # print(popularity)

# df = pd.DataFrame({
#     "Languages": languages,
#     "Ranking": popularity
# })
# print(df)

# df.loc[4] = ["PHP", 11]
# print(df)

# df.loc[3.5] = ["KESL", 20]
# print(df)

# df = df.sort_index()
# print(df)

# df = df.reset_index(drop=True)
# print(df)

# data_to_be_added = pd.DataFrame(
#     {
#     "Languages":["PHP"],
#     "Ranking": [11]
# }
#     )

# # df = pd.concat([df, data_to_be_added])
# df = pd.concat([df, data_to_be_added], ignore_index=True)
# print(df)

# # df.loc[6] = ["Java", 7]
# # df.loc[7] = ["TypeScript", 5]
# # print(df)

# additional_languages = pd.DataFrame({
#     "Languages": ["Java", "TypeScript"],
#     "Ranking": [7,5]
# })
# df = pd.concat([df, additional_languages], ignore_index=True)
# print(df)

#Reset df
languages = pd.Series(["Python","JavaScript","HTML","SQL","PHP","Java","TypeScript"])
popularity = pd.Series([3,1,2,4,11,7,5])
df = pd.DataFrame({
    "Languages": languages,
    "Ranking": popularity
})
# print(df)

df["Ranking 2022"] = [4,1,2,3,10,6,5]
# print(df)

#Reset df again
languages = pd.Series(["Python","JavaScript","HTML","SQL","PHP","Java","TypeScript"])
popularity = pd.Series([3,1,2,4,11,7,5])
df = pd.DataFrame({
    "Languages": languages,
    "Ranking": popularity
})

new_column = pd.DataFrame({"Ranking 2022": [4,1,2,3,10,6,5]})
df = pd.concat([df, new_column], axis=1)
# print(df)

df["Ranking 2020"] = [4,1,2,3,8,5,9]
df["Ranking 2019"] = [4,1,2,3,8,5,10]
# print(df)

# # OR
# # Reset df again
# languages = pd.Series(["Python","JavaScript","HTML","SQL","PHP","Java","TypeScript"])
# popularity = pd.Series([3,1,2,4,11,7,5])
# df = pd.DataFrame({
#     "Languages": languages,
#     "Ranking": popularity
# })
# new_column = pd.DataFrame({"Ranking 2022": [4,1,2,3,10,6,5]})
# df = pd.concat([df, new_column], axis=1)
# new_column = pd.DataFrame({"Ranking 2020": [4,1,2,3,8,5,9]})
# df = pd.concat([df, new_column], axis=1)
# new_column = pd.DataFrame({"Ranking 2019": [4,1,2,3,8,5,10]})
# df = pd.concat([df, new_column], axis=1)
# print(df)

# df.insert(3,"Ranking 2021", [3,1,2,4,11,5,7])
# print(df)

df.insert(2,"Ranking 2023", [3,1,2,4,11,5,7])
print(df)
# print(df.columns.get_loc("Languages"))

df.rename(columns={"Ranking": "Ranking 2024"}, inplace=True)
print(df)

# df2 = df.rename(columns={"Ranking": "Ranking 2024"}, inplace=False)
# print(df)
# print(df2)

df.loc[2]= ["PHP", 11, 10, 9, 8, 7]

df = df.set_index("Languages")
print(df)

# # OR
# # df.set_index("Languages",inplace=True)
# # print(df)