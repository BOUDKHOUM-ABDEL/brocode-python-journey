# Dictionary = a collection of {"key":"value"} pairs
#             ordered & changeable. No duplicates

capitales = {"usa":"washigton", 
             "Italy": "Rome",
             "Germany": "Berlin",
             "Japan": "Tokyo",
             "Canada": "Ottawa",}

# Add key-value pairs
capitales["France"] = "Paris"
capitales["Spain"] = "Madrid"
capitales["Morocco"] = "Rabat"

# Access a value
print("Capital of France:", capitales["France"]) # prints "Paris"
print("Capital of Japan:", capitales.get("Japan")) # prints "Tokyo"


# Update a value
capitales["Spain"] = "Barcelona"
capitales.update({"Italy": "Milan"})
print("Updated capital of Spain:", capitales["Spain"]) # prints "Barcelona"
print("Updated capital of Italy:", capitales["Italy"]) # prints "Milan"


# Remove a key-value pair
del capitales["Morocco"] # removes the key "Morocco" and its value
capitales.pop("Germany") # removes the key "Germany" and its value
capitales.popitem() # removes the last inserted key-value pair
print("After removals:", capitales) 

# Display all capitals
print("All capitals:", capitales) # prints the entire dictionary



