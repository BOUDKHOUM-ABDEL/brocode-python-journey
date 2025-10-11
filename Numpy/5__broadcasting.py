

#Broadcasting allows Numpy to perform operation on arrays 
#with different shapes by virtually expanding dimensions 
#so they match the larger array's shapes.

#the dimensions have the same size.
#OR 
#One of the dimensions has a size of 1.

import numpy as np

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1],[2],[3],[4]])
print(array1)
print(array2)
print(array1.shape)  #(1, 4)
print(array2.shape)  #(4, 1)

print(array1 * array2)

array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(array1.shape)  #(1, 4)
print(array2.shape)  #(4, 1)

print(array1 * array2)