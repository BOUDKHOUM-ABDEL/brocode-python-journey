import csv
import os

csv_path = "part_9/stuff/data.csv"

# Ensure the directory exists
os.makedirs(os.path.dirname(csv_path), exist_ok=True)

# ✅ Write initial CSV data
csv_data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "London"],
    ["Charlie", 35, "Paris"]
]

with open(csv_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

print(f"✅ CSV file '{csv_path}' was created with initial data.")

# 🔄 Append new rows
new_rows = [
    ["Diana", 28, "Berlin"],
    ["Ethan", 40, "Tokyo"]
]

with open(csv_path, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(new_rows)

print(f"🔄 New rows were appended to '{csv_path}'.")

# 📖 Read and display CSV content
print("\n📋 Reading CSV content:")
with open(csv_path, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 🧾 Write CSV using dictionaries
dict_data = [
    {"Name": "Fiona", "Age": 22, "City": "Madrid"},
    {"Name": "George", "Age": 33, "City": "Rome"}
]
dict_path = "part_9/stuff/data_dict.csv"

with open(dict_path, "w", newline="") as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(dict_data)

print(f"\n🧾 Dictionary-based CSV file '{dict_path}' was created.")