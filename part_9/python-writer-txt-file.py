import os

txt_data = "I like Pizza!\n"
file_path = "part_9/stuff/test.txt"


# 'w' mode: overwrite if file exists
with open(file_path, "w") as file:
    file.write(txt_data)
    file.write("Here are some numbers:\n")
    for i in range(10):
        file.write(f"{i}\n")

print(f"Text file '{file_path}' was created with 'w' mode.")

# 'a' mode: append new content
with open(file_path, "a") as file:
    file.write("\n--- Appended Section ---\n")
    file.write("I also like Pasta!\n")

print(f"Text file '{file_path}' was updated with 'a' mode.")

# 'x' mode: create new file, error if exists
new_file_path = "part_9/stuff/new_file.txt"
try:
    with open(new_file_path, "x") as file:
        file.write("This file was created with 'x' mode.\n")
except FileExistsError:
    print(f"File '{new_file_path}' already exists. Skipping creation.")