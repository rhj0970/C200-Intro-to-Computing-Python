import random as rn
import numpy as np

#INPUT Parameters: a square numpy array with integers from 1, 100
#Return: The indices of the largest value
def max_index(y):
    maxvalue = y[0][0]
    for i in range(0,len(y)):
        for j in range(0,len(y)):
           
            if y[i][j] > maxvalue:  
               maxvalue = y[i][j] 
               k = [i,j]
               
    return k
    

    

x = rn.randint(3,6)

print(x)
y = np.arange(x**2).reshape(x,x)

for i in range(0,x):
    for j in range(0,x):
        y[i][j] = rn.randint(1,100)

print(y)
i = max_index(y)
print(i)
print(y[i[0]][i[1]])
