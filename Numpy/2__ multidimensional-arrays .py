import numpy as np

# Define the array
array = np.array([[['A','B','C'], ['D','E','F'], ['G','H','I']],
                  [['J','K','L'], ['M','N','O'], ['P','Q','R']],
                  [['S','T','U'], ['V','W','X'], ['Y','Z',' ']]])

# Print the array
print("Array:")
print(array)

# Print the shape
print("\nShape of the array:", array.shape) #(3,3,3)

print(array[0][0][0])  #A
print(array[1][2][0])  #P
print(array[2][2][1])  #Z
print(array[0,2,1])    #H