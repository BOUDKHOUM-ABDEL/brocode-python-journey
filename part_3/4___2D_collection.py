

#2d collection = list of lists (matrix)

from ast import Num


groceries= [ ["apple", "banana", "coconut"], 
             ["carrot", "broccoli", "asparagus"],
             ["chicken", "pork", "beef"] ]

print(groceries)

for category in groceries:  
    for item in category:   
        print(item, end=" ")
    print()  #new line after each category

num_pad= ( (1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#") )
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()  #new line after each row