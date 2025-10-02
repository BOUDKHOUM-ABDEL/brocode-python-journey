

#list comprehension = a way to create a new list with less syntax
#                     can replace many for loops with a single line of code
#                     [expression for item in iterable if condition ]

doubles=[x*2 for x in range(0,11)]
print(doubles)

print("positive" if 5 > 0 else "negative")  #ternary operator = shortcut for if-else statement)

fruits = ["apple", "orange", "coconut", "banana"]
fruits_upper = [fruit.upper() for fruit in fruits]
print(fruits_upper)
fruits_letter= [fruit[0] for fruit in fruits]
print(fruits_letter)

numbers=[-4,8,19,23,-12,98,-3]
positive_numbers = [num for num in numbers if num >= 0]
print(positive_numbers)
negative_numbers = [num for num in numbers if num < 0]
print(negative_numbers)