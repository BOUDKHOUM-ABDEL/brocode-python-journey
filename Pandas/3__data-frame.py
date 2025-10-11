

#DataFrame = A tabular data structure with rows and columns. (2 dimensional)
#            simlar to an Excel spreadsheet
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "age": [25, 30, 22, 28, 35]
}

df = pd.DataFrame(data , index=['student1' , 'student2' , 'student3' , 'student4' , 'student5'])
print(df)
# output:
#              Name  age
# student1    Alice   25
# student2      Bob   30
# student3  Charlie   22
# student4    Diana   28
# student5    Ethan   35

print(df.loc['student3'])
# output:
# Name    Charlie
# age          22

#Add new column
df["city"] = ["Paris", "London", "New York", "Tokyo", "Berlin"]
print(df)
#              Name  age      city
# student1    Alice   25     Paris
# student2      Bob   30    London
# student3  Charlie   22  New York
# student4    Diana   28     Tokyo
# student5    Ethan   35    Berlin

#Add new row
new_row = pd.DataFrame([{"Name" : "Sandy" , "age" : 28 , "city" :"Lile"}],index = ["Student6"])
df = pd.concat([df,new_row])
print(df)
#              Name  age      city
# student1    Alice   25     Paris
# student2      Bob   30    London
# student3  Charlie   22  New York
# student4    Diana   28     Tokyo
# student5    Ethan   35    Berlin
# Student6    Sandy   28      Lile
new_rows = pd.DataFrame([{"Name" : "Lina" , "age" : 23 , "city" :"Barcelona"},
                         {"Name" : "Mark" , "age" : 27 , "city" :"Machester"}],
                         index = ["Student7" , "Student8"])


df = pd.concat([df,new_rows])
print(df)
#              Name  age       city
# student1    Alice   25      Paris
# student2      Bob   30     London
# student3  Charlie   22   New York
# student4    Diana   28      Tokyo
# student5    Ethan   35     Berlin
# Student6    Sandy   28       Lile
# Student7     Lina   23  Barcelona
# Student8     Mark   27  Machester


