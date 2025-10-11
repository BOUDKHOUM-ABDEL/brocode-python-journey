

name=input("Enter your name: ")
phone_number=input("Enter your phone number: ")

result=len(name) # length of string 
result=name.find("a") # find the index of a specific character (returns -1 if not found)
result=name.rfind("a") # find the last occurrence of a specific character
result=name.upper() # convert to uppercase
result=name.lower() # convert to lowercase
result=name.title() # convert to title case (first letter of each word capitalized)
result=name.count("a") # count occurrences of a specific character
result=name.isalpha() # check if all characters are alphabetic
result=name.capitalize() # capitalize the first letter of the string
result=name.replace("a","o") # replace occurrences of a specific character with another character
result=phone_number.isdigit() # check if all characters are digits
result=phone_number.count("1") # count occurrences of a specific digit)


print(result)