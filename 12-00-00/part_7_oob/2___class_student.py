
#class variabes = 

from re import S


class student :

    _class_year = 2025
    _nbr_students=0
    _school_name="ABC School"


    def  __init__(self, name, age):
        self._name = name
        self._age = age
        student._nbr_students+= 1

    def info(self):
        print(f"name: {self._name} age: {self._age}")

student1=student("joe",20)
student2=student("steve",22)
student3=student("anna",19)
student4=student("maria",21)
student5=student("linda",23)

print(student1._class_year)
student2.info()
print(f"in {student._school_name} there is {student._nbr_students} students")
print(f"my graduating class of {student._class_year} has {student._nbr_students} Students")
student1.info()
student2.info()
student3.info()
student4.info()
student5.info()
