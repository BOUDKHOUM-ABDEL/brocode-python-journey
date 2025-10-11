
#class methods = Allows opretations related to the class itself 
#                take (cls) as the first parameter , which represents the class itself


class Student:

    count = 0 
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count+=1
        Student.total_gpa += gpa

    #instance method
    def get_info(self):
        return f"{self.name} has a GPA of {self.gpa}"

    #class method
    @classmethod
    def get_count(cls):
        return f"There are {cls.count} students in total"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        return cls.total_gpa / cls.count

     
print(Student.get_count()) # There are 0 students in total

student1 = Student("John", 3.5)
student2 = Student("Jane", 3.8)
student3 = Student("Doe", 2.8)
print(Student.get_count()) # There are 3 students in total
print(f'{Student.get_average_gpa() : .2f}') # 3.37