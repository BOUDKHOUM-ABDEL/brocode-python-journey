
#keywords arguments =   an argument preceded by an identifier (e.g. name=value)
#                       helps with readability and allows us to pass arguments in any order
#                       order doesn't matter when using keyword arguments
#                       1.positional 2.default 3.keyword 4.arbitrary

#exemple 1
def hello(greeting , title , first , last):
    print(f"{greeting}{title} {first} {last}")


hello("Hello","Mr.","Joe","Smith")  #positional arguments
hello("Hello","Mr.","Smith","Joe")  #positional arguments
hello(first="Joe", last="Smith", title="Mr.", greeting="Hello")  #keyword arguments

#exemple 2

print("10","20","30",sep="-")  #positional arguments
for i in range(0,5):  #positional arguments
    print(i , end=" ") #keyword arguments