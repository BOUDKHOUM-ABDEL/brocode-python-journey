

# Decorator = A function that takes another function as an argument and extends or alters its behavior without explicitly modifying it.
# Decorators are commonly used for logging, access control, timing, and more.

def add_spinkles(func):
    def wrapper():
        print("you add spinkles")
        func()
    return wrapper

@add_spinkles
def make_cake():
    print("Cake is ready!")



make_cake()
# Output:
# you add spinkles
# Cake is ready!

# Example: Decorator with arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")



say_hello()
# Output:
# Hello!
# Hello!
# Hello!