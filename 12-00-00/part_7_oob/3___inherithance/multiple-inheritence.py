
#mutiple inheritence : when a class is derived from more than one base class.
#                     C(A,B)

#mulilevel inheritence : when a class is derived from a class which is also derived from another class.
#                       C(B) <-- B(A) <-- A


class Animal:

    def __init__(self, name):
        self.name = name
        


    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal): 
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
        pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass


rabbit = Rabbit("bugs")
hawk = Hawk("Tony")
fish = Fish("memo")

fish.flee()
fish.hunt()

rabbit.eat()
hawk.sleep()
fish.eat()