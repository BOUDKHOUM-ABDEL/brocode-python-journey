
#filtering = keeping the rows that match a condition

import pandas as pd

# Load CSV 
df = pd.read_csv("pandas/data.csv")

# Show full DataFrame
print("📋 Full DataFrame:")
print(df.to_string())

#Filter: All Fire-type Pokémon
fire_type = df[df["Type1"] == "Fire"]
print("\nFire-type Pokémon:")
print(fire_type.to_string())

#Filter: Electric-type Pokémon with Weight < 10
light_electric = df[(df["Type1"] == "Electric") & (df["Weight"] < 10)]
print("\n⚡ Light Electric-type Pokémon (Weight < 10):")
print(light_electric.to_string())

# Filter: All Dragon-type Pokémon
dragon_type = df[df["Type1"] == "Dragon"]
print("\n🐉 Dragon-type Pokémon:")
print(dragon_type.to_string())

# Filter: Pokémon with dual types (Type2 not null)
dual_type = df[df["Type2"].notnull()]
print("\n🧬 Pokémon with dual types:")
print(dual_type.to_string())

# Filter: Legendary Pokémon
legendary = df[df["Legendary"] == 1]
print("\n🧠 Legendary Pokémon:")
print(legendary.to_string())

# Filter: Pokémon taller than 2 meters
tall_pokemon = df[df["Height"] > 2]
print("\n📏 Pokémon taller than 2 meters:")
print(tall_pokemon.to_string())

#  Filter: Flying-type Pokémon with Weight > 50
heavy_flyers = df[(df["Type2"] == "Flying") & (df["Weight"] > 50)]
print("\n Flying-type Pokémon with Weight > 50:")
print(heavy_flyers.to_string())

# Filter: Pokémon whose name contains "char" (case-insensitive)
char_names = df[df["Name"].str.contains("char", case=False)]
print("\n🔍 Pokémon with 'char' in their name:")
print(char_names.to_string())