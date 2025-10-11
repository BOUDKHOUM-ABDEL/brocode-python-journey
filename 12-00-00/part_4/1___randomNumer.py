
from optparse import Option
import random

number= random.randint(1,100) 

low=1
high=100
number = random.randint(low,high)
print(number)

options=["rock","paper","scissors"]
Option=random.choice(options)
print(Option)