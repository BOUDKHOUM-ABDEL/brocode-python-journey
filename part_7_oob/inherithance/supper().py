

#super() : function used in a child class to call methods from a parents class



class Shape:
    def __init__(self,color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def Describe(self):
        print(f"It's {self.color} and {"filled" if self.is_filled else 'not filled'} ")
    



class Circle(Shape):
    def __init__(self,color, is_filled, radius):
        super().__init__(color, is_filled)
        
        self.radius = radius
    def Describe(self):
        super().Describe()
        print(f"It's a circle with Area of {3.14*self.radius*self.radius} cm2")


class Square(Shape):
    def __init__(self,color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def Describe(self):
        super().Describe()
        print(f"It's a Square with Area of {self.width**2} cm2")


class Triangle(Shape):
    def __init__(self,color, is_filled, width, hight):
        super().__init__(color, is_filled)
        self.radius = width
        self.hight = hight


circle1= Circle("red", True, 5)
print(circle1.color) # 'red'
print(circle1.is_filled) # True

square1= Square("blue", False, 4)
print(square1.color) # 'blue'
print(square1.is_filled) # False

Triangle1=Triangle(color="blue", is_filled=True, width=6 , hight=3)

print(Triangle1.color)
Triangle1.color="Yellow"
print(Triangle1.color)
 


circle1.Describe() #output: 