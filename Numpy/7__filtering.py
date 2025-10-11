
#filtering = Refres to the process of selecting elements 
#            from an array that match a given condition

import numpy as np
ages = np.array([[21,32,15,26,30,17],
                [49,12,50,66,39,72]])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages <= 50) ]
seniors = ages[(ages >= 50) & (ages <= 99) ]
print(teenagers)
print(adults)
print(seniors)



