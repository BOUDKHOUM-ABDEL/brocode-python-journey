

# Decorator = A function that takes another function as an argument and extends or alters its behavior without explicitly modifying it.
# Decorators are commonly used for logging, access control, timing, and more.

def add_spinkles(func):
    def wrapper(*args,**kwargs):
        print("you add spinkles")
        func(*args,**kwargs)
    return wrapper

def add_frdge(func):
    def wrapper(*args,**kwargs):
        print("you add fudge ")
        func(*args,**kwargs)
    return wrapper

@add_spinkles
@add_frdge 
def get_ice_cream(flavor):
    print(f"Here is your {flavor} !")



get_ice_cream("vanilla")


#you add spinkles
#you add fudge
#Here is your ice cream !

