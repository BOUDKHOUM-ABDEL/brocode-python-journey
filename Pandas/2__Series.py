import pandas as pd 

# Series = A pandas 1-dimentional labled array that can hold any data type 
#          think of it like a single column in a spreadsheet (1-Dimensional)

calories = {"Day1":1750 , "Day2":2100 , "Day3":1700 , "Day4":2000}
series = pd.Series(calories)

print(series)
#output:
#Day1    2000
#Day2    2100
#Day3    1700
#dtype: int64

series.loc["Day3"] +=200
print(series)
#output:
#Day1    2000
#Day2    2100
#Day3    1900
#dtype: int64

print(series[series < 2000])
#output:
#Day3    1900
#dtype: int64