#module = a file containing code you want to include in your program 
#         use import to include a module

import math
from unittest import result 
print(math.pi)

import math as m 
print(m.e)

from math import pi
print(pi)

import module2 #importing a module

print(module2.subtract(10,5))
result = module2.multiply(4,7)
print(result)

