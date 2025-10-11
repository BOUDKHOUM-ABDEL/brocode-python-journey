

class Animal :

    def __init__(self, name) :
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} is meowing")

class Mouse(Animal):
    def squeak(self):
        print(f"{self.name} is squeaking")

dog1= Dog("Scooby")
cat1= Cat("Tom")
mouse1= Mouse("Jerry")

dog1.eat()
cat1.sleep()
print(mouse1.is_alive)

dog1.bark()
cat1.speak()
mouse1.squeak()

