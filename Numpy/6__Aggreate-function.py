

#Aggreate-function = summrize data and typically return 
#                    a return a single value

import numpy as np
array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

print(np.sum(array))  #55
print(np.mean(array)) #5.5
print(np.var(array))  #8.25
print(np.min(array))  #1
print(np.max(array))  #10

print(np.argmin(array)) #0

print(np.sum(array , axis=0))