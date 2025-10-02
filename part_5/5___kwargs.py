


#kargs = allows you to pass a variable number of keyword arguments to a function


#exemple 1
def info(**info):
    for key, value in info.items():
        print(f"{key}: {value} ")

def info_name(**info):
    for name in info.values():
        print(name,end=" ")

print(info(name="joe", age=30, city="New York")) 
print(info_name(first="joe", last="smith"))


print("\n_________________exemple__________________\n\n")
#exemple 2 *args and **kargs combined

def shipping_label(*args, **kwargs):
    print("______Shipping to:______")
    for line in args:
        print(line , end=" ")
    print("\n______Details:______")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

shipping_label("John Doe", "123 Main St", "Apt 4B",\
              city="New York", state="NY", zip="10001")