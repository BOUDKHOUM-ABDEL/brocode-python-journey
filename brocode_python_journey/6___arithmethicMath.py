

friends=3
friends=friends+1

#........
print(friends)


friends=friends**2 # friends=friends*friends
print(friends)

#........code2............
pi=3.14
y=4
z=5

result=round(pi) #3
result=pow(y,z) #1024
result=abs(-y) #4
result=max(y,z,pi) #5
result=min(y,z,pi) #3.14

print (result)

#........code3............
import math
from tkinter import ROUND
print(math.pi) #3.141592653589793
print(math.e)   #2.718281828459045
print(math.sqrt(16)) #4.0

#..........Exercice...............
import math

raduis=float(input("Enter the raduis of the Circule  : "))

circumference=2*math.pi*raduis
print(f"the circumference = {round(circumference,3)} cm")

area=math.pi*pow(raduis,2)
print(f"the raduis = {round(area,3)} cm2")


#..........End Exercice...............
import math
a=float(input("Enter the value of a : "))
b=float(input("Enter the value of b : "))
c=math.sqrt(pow(a,2)+pow(b,2))

print(f"the value of c = {round(c,2)}")