import pandas as pd

# Load CSV and set 'Name' as index
df = pd.read_csv("pandas/data.csv", index_col="Name")

pokemon = input("Enter a name of a pokemon").capitalize()

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"the {pokemon} not found")
