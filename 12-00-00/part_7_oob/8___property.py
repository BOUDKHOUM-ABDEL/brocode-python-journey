

#@property = Decorator user to define a methode as property(it can be accessed like attribute)
#            Benefit : Add additional logic when read, wrhite , or Delete attributes
#            Gives you getter , setter , and deleter method


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    # Getter for width
    @property
    def width(self):
        return self._width

    # Setter for width
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    # Deleter for width
    @width.deleter
    def width(self):
        print("Deleting width...")
        del self._width

    # Getter for height
    @property
    def height(self):
        return self._height

    # Setter for height
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    # Deleter for height
    @height.deleter
    def height(self):
        print("Deleting height...")
        del self._height

    # Read-only property for area
    @property
    def area(self):
        return self._width * self._height

# Example usage
rect = Rectangle(5, 10)
print(rect.area)       # Accessing area like an attribute
rect.width = 7         # Using setter
print(rect.area)       # Updated area
del rect.height        # Using deleter

