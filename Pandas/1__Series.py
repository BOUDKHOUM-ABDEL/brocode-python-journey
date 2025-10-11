import pandas as pd 

# Series = A pandas 1-dimentional labled array that can hold any data type 
#          think of it like a single column in a spreadsheet (1-Dimensional)

data = [100 , 102, 104]
series = pd.Series(data)

print(series)
#output:
# 0    100
# 1    102
# 2    104
# dtype: int64

series = pd.Series(data,index=['a','b','c'])
print(series)
#output:
# a    100
# b    102
# c    104
# dtype: int64

print(series.loc['c'])  #104
print(series.iloc[0])   #100

