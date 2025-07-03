import pandas as pd

planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planet_temp = ["167C", "464C", "15C", "65C", "-110C", "-140C", "-195C", "-200C"]
planet_size = ["2440km", "6052km", "6371km", "3390km", "69911km", "58232km", "25362km", "24622km"]
planet_colour = ["Grey", "White", "Blue", "Red", "Beige", "Beige", "Blue", "Blue"]
planet_feature = ["Smallest Planet", "Hottest Planet", "Supports Life!", "Iron Soil", "Giant Storm", "Rings", "Extreme Seasons", "Icy"]

df = pd.DataFrame({
    "Planet Name": planet_names,
    "Average Temp": planet_temp,
    "Radius": planet_size,
    "Colour": planet_colour,
    "Notable Feature": planet_feature
})

print(df)

df.loc[3.5] = [1,2,3,4,5]
df = df.set_index("Planet Name")
print(df)

planet_selected = input("Which Planet would you like to see?    > ")
print("Which column would you like to see?")
for column in df.columns:
    print(column)
print("or type 'All' to see all information ")
info_selected = input("    > ").capitalize()

if info_selected=="All":
    print(df.loc[f'{planet_selected}'])
else:
    print(df.loc[f'{planet_selected}', f"{info_selected}"])

