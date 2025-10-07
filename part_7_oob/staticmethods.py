
#sytatic methods = A method that belong to aclass rather than any object
                  # from a claas (instance) usually used to do utility functions
                  #    
# instance methods = Best for operations on instances (objects) of a class
#static methods = Best for utility functions that don't need to access anything in the class



class Employee:

    def __init__(self, name, position):
        self.name = name    
        self.position = position

    def get_info(self):
        return f"{self.name} is a {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ['Manager', 'Staff', 'Intern' , 'Janitor']
        return position in valid_positions

print(Employee.is_valid_position("Manager")) # True
print(Employee.is_valid_position("CEO")) # False

emp1 = Employee("John", "Manager")
emp2 = Employee("Jane", "CEO")
emp3 = Employee("Doe", "Intern")

print(emp1.get_info()) # John is a Manager
print(emp2.get_info()) # Jane is a CEO
print(emp3.get_info()) # Doe is a Intern