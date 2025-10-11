

#collections = single 'variable' used to store multiple values.

#list = [] collection which is ordered and changeable.  Deplicate ok.
#Set = {} collection which is unordered and immutibale. can add/remove. No deplicate.  
#Tuple = () collection which is ordered and unchangeable.  Deplicate ok. faster than list.

fruits = ("apple", "banana", "coconut")
print(fruits) # ('apple', 'banana', 'coconut')
print(fruits[2]) # coconut
print(fruits[-1]) # coconut (last item)
print(fruits[0:2]) # ['apple', 'banana'] (first 2 items)

print(fruits.index("banana")) # get index of item