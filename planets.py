import pandas as pd
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planet_temp = ["167C", "464C", "15C", "65C", "-110C", "-140C", "-195C", "-200C"]
planet_size = ["2440km", "6052km", "6371km", "3390km", "69911km", "58232km", "25362km", "24622km"]
planet_colour = ["Grey", "White", "Blue", "Red", "Beige", "Beige", "Blue", "Blue"]
planet_feature = ["Smallest Planet", "Hottest Planet", "Supports Life!", "Iron Soil", "Giant Storm", "Rings", "Extreme Seasons", "Icy"]
# Create the DataFrame
df = pd.DataFrame({
   "Name": planet_names,
   "Temp": planet_temp,
   "Size": planet_size,
   "Colour": planet_colour,
   "Feature": planet_feature
})
print(df)
# Save to Excel (index=False means don't include the row numbers)
df.to_excel("planets.xlsx", index=False)
print("Excel file 'planets.xlsx' has been saved.")