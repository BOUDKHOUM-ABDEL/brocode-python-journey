

#Addregate function = Reduces a set of value intp summary value 
#                     Used to summarize and analyse data 
#                     often used with the groupby() function

import pandas as pd

# Load the dataset
df = pd.read_csv("pandas/data.csv")

# Example 1: Count how many Pokémon per Type1
type_counts = df.groupby("Type1")["Name"].count()
print("\n📊 Number of Pokémon per Type1:")
print(type_counts)

# Example 2: Average Height and Weight per Type1
avg_stats = df.groupby("Type1")[["Height", "Weight"]].mean()
print("\n📏 Average Height and Weight per Type1:")
print(avg_stats)

# Example 3: Maximum Weight per Type1
max_weight = df.groupby("Type1")["Weight"].max()
print("\n🏋️ Maximum Weight per Type1:")
print(max_weight)

# Example 4: Total number of Legendary Pokémon per Type1
legendary_count = df[df["Legendary"] == 1].groupby("Type1")["Legendary"].count()
print("\n🧠 Number of Legendary Pokémon per Type1:")
print(legendary_count)

# Example 5: Aggregating multiple stats at once
multi_agg = df.groupby("Type1").agg({
    "Height": ["mean", "max"],
    "Weight": ["mean", "max"],
    "Legendary": "sum"
})
print("\n📊 Multiple Aggregations per Type1:")
print(multi_agg)