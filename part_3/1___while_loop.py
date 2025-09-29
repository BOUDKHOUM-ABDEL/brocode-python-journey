

name=input("Enter your name : ")

while name == "" :
    print("you did not Enter your name. ")
    name=input("Enter your name : ")
print(f"Hello {name}")        

food=input("Enter a food would you like to eat : (q to quit) : ")
while not food=="q":
    print(f"I like {food} too")
    food=input("Enter a food would you like to eat : (q to quit) : ")
print("Thank you")