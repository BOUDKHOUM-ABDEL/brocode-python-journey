
#function: a block of code that performs a specific task 

#exemple 1
def happy_birthday(name, age):
    print(f"Happy birthday, {name}! You are now {age} years old.")

happy_birthday("joe",30)
happy_birthday("steve",25)


#exemple 2
def display_inovoice(username, amount, due_date):
   print(f"Hello {username}")
   print(f"your bill of ${amount} is due : {due_date}")

display_inovoice("steve",100,"01/01")

#exemple 3

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2

  #test the functions
print(add(10, 5))        # Output: 15
print(subtract(10, 5))   # Output: 5
print(multiply(10, 5))   # Output: 50
print(divide(10, 5))     # Output: 2.0


#exemple 4

import time 
def count (start, end):
    if start > end:
        print("Start should be less than or equal to end.")
        return
    for i in range(start, end + 1):
        print(i)
        time.sleep(1)  # Pause for 1 second between numbers
    print("Done!")

count(0,10)  # Count from 5 to 10 with a 1-second interval


 
