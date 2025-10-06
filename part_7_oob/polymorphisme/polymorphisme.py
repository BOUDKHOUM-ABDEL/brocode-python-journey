class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Pizza(Circle):
    def __init__(self,topping, radius):
        super().__init__(radius)
        self.topping = topping
        



# Create list 1 of shapes
shapes1 = [Rectangle(12, 23), Circle(10), Triangle(12, 23)]

# Print the area of each shape
for shape in shapes1:
    print(f"{type(shape).__name__} area: {shape.area()}")

# Create list 2 of shapes
shapes2 = [Rectangle(20,50), Circle(5) , Triangle(3,4) , Pizza("pepperoni",7)]

# Print the area of each shape
for shape in shapes2:
    print(f"{type(shape).__name__} area: {shape.area()}")
