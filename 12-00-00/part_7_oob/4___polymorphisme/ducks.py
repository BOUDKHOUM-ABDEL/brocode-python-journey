

#Duck typing = 

class Animal():
    is_alive = True

class Cat(Animal):
    def speak(self):
        print("Meow !")

class Dog(Animal):
    def speak(self):
        print("WOOF !")

class animal3():
    is_alive = False

    def speak(self):
        print("WOOH !")




Animals=[Cat(),Dog()]

for animal in Animals :
    animal.speak()

Animals2 = [Cat(),Dog(), animal3()]

for animal in Animals2:
     print(animal.is_alive)

