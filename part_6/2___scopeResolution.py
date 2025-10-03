#scope resoultion = where a variable is visible and accessible
#LEGB = Local, Enclosing, Global, Built-in

x = "global x" #global variable
def test():
    x = "local x" #local variable
    print(x)

test() #prints local x
print(x) #prints global x
def outer():
    x = "outer x" #enclosing variable
    def inner():
        x = "inner x" #local variable
        print(x)
    inner()
    print(x)
outer()
print(x) #prints global x
#built-in variable
print(len(x)) #len is a built-in function