

#*args = allows us to pass multiple non-key arguments to a function

#exemple 1
def add(*args):  #*args = takes multiple non-key arguments and packs them into a tuple
    total = 0
    for num in args:
        total += num
    return total
print(add(1, 2, 3))  # Output: 6

#exemple 2
def display_names(*names):
    for name in names:
        print(name, end=" ")

print(display_names("Alice", "Bob", "Charlie"))  # Output: Alice Bob Charlie
print(display_names("David", "Eve"))  # Output: David Eve
print(display_names("David","Alice", "Bob", "Charlie", "Brown" )) 

