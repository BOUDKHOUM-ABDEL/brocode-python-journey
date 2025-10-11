

#collections = single 'variable' used to store multiple values.

#list = [] collection which is ordered and changeable.  Deplicate ok.
#Set = {} collection which is unordered and immutibale. can add/remove. No deplicate.  
#Tuple = () collection which is ordered and unchangeable.  Deplicate ok. faster than list.

fruits = {"apple", "banana", "coconut"}
print(fruits) # {'banana', 'coconut', 'apple'}
#print(fruits[2]) # coconut (error, set does not support indexing

fruits.add("orange") # add item to end of list
fruits.add("kiwi") # add item
fruits.remove("banana") # remove item by value
print(fruits) # {'kiwi', 'coconut', 'apple', 'orange'}
fruits.pop() # remove last item
print(fruits) # {'kiwi', 'coconut', 'apple'}
