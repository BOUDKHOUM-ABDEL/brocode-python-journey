
import numpy as np

#scalar arithmetic 
array =np.array([1,2,3,4])
print(array + 1)
print(array * 3)
print(array ** 2)

#vectorized math funcs
array =np.array([4,16,49,121])
print(np.round(array))  #[  4  16  49 121]

print(np.sqrt(array)) #[ 2.  4.  7. 11.]
print(np.pi)

#Element-wise arithmetic
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
print(array1 + array2)
print(array1 * array2)
print(array1 - array2)
print(array1 ** array2)

#Comparison operators
scores = np.array([90,30,50,70,10,40])
print(scores == 10)
print(scores > 50)
[scores < 50] = 0
print(scores)

