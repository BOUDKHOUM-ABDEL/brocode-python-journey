

#collections = single 'variable' used to store multiple values.

#list = [] collection which is ordered and changeable.  Deplicate ok.
#Set = {} collection which is unordered and immutibale. can add/remove. No deplicate.  
#Tuple = () collection which is ordered and unchangeable.  Deplicate ok. faster than list.

fruits = ["apple", "banana", "coconut"]
print(fruits) # ['apple', 'banana', 'coconut']
print(fruits[2]) # coconut
print(fruits[-1]) # coconut (last item)
print(fruits[0:2]) # ['apple', 'banana'] (first 2 items)
fruits[0] = "pear" # change item
for fruit in fruits: 
    print(fruit , end=" ") # pear banana coconut (print all items in one line)

fruits.append("orange") # add item to end of list
fruits.insert(1, "kiwi") # add item at index 1
fruits.remove("banana") # remove item by value
print(fruits) # ['pear', 'kiwi', 'coconut', 'orange']
fruits.sort() # sort list alphabetically
print(fruits) # ['coconut', 'kiwi', 'orange', 'pear']
fruits.pop() # remove last item
print(fruits.index("kiwi")) # get index of item
