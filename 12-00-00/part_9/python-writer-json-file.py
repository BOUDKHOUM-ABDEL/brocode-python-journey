import json
import os

json_path = "part_9/stuff/data.json"

# Initial data
json_data = {
    "name": "Alice",
    "age": 30,
    "likes": ["Pizza", "Coding", "Travel"]
}

# Write JSON data (overwrite mode)
with open(json_path, "w") as file:
    json.dump(json_data, file, indent=4)

print(f"✅ JSON file '{json_path}' was created with initial data.")

# Read and update JSON data
if os.path.exists(json_path):
    with open(json_path, "r") as file:
        data = json.load(file)

    # Update age and add a new hobby
    data["age"] += 1
    data["likes"].append("Photography")

    with open(json_path, "w") as file:
        json.dump(data, file, indent=4)

    print(f"🔄 JSON file '{json_path}' was updated with new age and hobby.")

# Write a list of dictionaries (e.g., multiple users)
users = [
    {"name": "Alice", "age": 31},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

users_path = "part_9/stuff/users.json"
with open(users_path, "w") as file:
    json.dump(users, file, indent=4)

print(f"📂 JSON file '{users_path}' was created with a list of users.")