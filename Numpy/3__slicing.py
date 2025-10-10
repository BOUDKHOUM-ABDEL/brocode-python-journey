import numpy  as np

array = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])

print(array.shape) #(4,4)

#array[start : end : step]
print(array[2:3:2]) 

# Additional examples for clarity
print("\nSlicing array[1:4:2]:")  # Rows 1 and 3
print(array[1:4:2])

print("\nSlicing array[:, 1:3]:")  # All rows, columns 1 and 2
print(array[:, 1:3])

print("\nSlicing array[::2, ::2]:")  # Every other row and column
print(array[::2, ::2])

# Boolean indexing: elements greater than 10
print("\nElements greater than 10:")
print(array[array > 10])  # Output: [11 12 13 14 15 16]

# Reshape the array to 2×8
reshaped = array.reshape(2, 8)
print("\nReshaped to 2×8:")
print(reshaped)

# Flatten the array
print("\nFlattened array:")
print(array.flatten())  # Output: [1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16]

#  Transpose the array
print("\nTransposed array:")
print(array.T)
