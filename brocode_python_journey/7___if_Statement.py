
#if = do something if a condition is true
#else = do something else if the condition is false

#Example 1.......................................
from math import e
from urllib import response


age= int(input("Enter your age: "))

if age>=18 and age<=100:
    print("You are now signed up")
elif age<=0:
    print("you have not been born yet")
elif age>=100:
    print("You are too old to sign up")
else:   
    print("You must be at least 18 years old to sign up")

#Example 2.......................................
response=input("would you like food ? (y/n) : ")
if response=="y" or response=="Y":
    print("Here is food")
elif response=="n" or response=="N":
    print("No food for you")
else:
    print("Invalid input")