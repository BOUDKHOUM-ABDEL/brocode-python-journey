
#Data cleaning = The process of fixing /removing :
#                incomplete ,incorrect or irrelevant data.
#                -75% of work done with pandas is data cleaning 
import pandas as pd

df = pd.read_csv("pandas/data-clean.csv")

# 1.Drop irrelevant columns
# df = df.drop(columns =["Legendary" , "No"])
# print(df)
# 2.Handle missing data

#df = df.dropna(subset=["Type2"])
df = df.fillna({"Type2": "None"})
print(df)


# 3. Fix inconsistent value
df["Type1"] = df["Type1"].replace({"Grass" : "GRASS","Fire" : "FIRE"})
print(df)

# 4.Stansardize text
df["Name"] =df["Name"].str.lower()
print(df)

# 5.fix data type
df["Legendary"] = df["Legendary"].astype(bool)
print(df)


