import pandas as pd

# Load CSV and set 'Name' as index
df = pd.read_csv("pandas/data.csv", index_col="Name")

# Print entire DataFrame
print("Full DataFrame:")
print(df)
print(df.to_string())

# Selection by column (excluding 'Name' since it's now the index)
print("\nHeight column:")
print(df["Height"].to_string())

print("\nSelected columns (Height, Weight):")
print(df[["Height", "Weight"]].to_string())

# Select by row
print("\nRow for Charmeleon:")
print(df.loc["Charmeleon"])

print(df.iloc[0:11])
print(df.iloc[0:11:2 , 0:3])
