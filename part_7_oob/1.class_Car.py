#object = a bundlle of related attributes (variables) and methods (functions)
#         ex. phone , cup , book 
#         you need a "class" to create objects

#class = (blueprint) used to design the structure and layout of an object 

class car:
    def __init__(self,model, year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale= for_sale

    def info(self):
        print(f"Model: {self.model}\nYear: {self.year}\nColor: {self.color}\nFor Sale: {self.for_sale}")
       

    def in_sale(self):
        if self.for_sale:
            print(f"{self.color} {self.model } is for sale")
        else:
            print(f"{self.color} {self.model } is not for sale")




car1=car("Dacia",2020, "blue", True)
car2=car("Renault",2018, "red", False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.info()
car2.info()
car1.in_sale()
car2.in_sale()
