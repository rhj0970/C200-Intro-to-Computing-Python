import numpy as np
from numpy import linalg

a = np.zeros ((4,4),dtype = float)
a[0] = [0,1,1,1]
a[1] = [0,0,0,1]
a[2] = [1,0,0,0]
a[3] = [1,1,0,0]

for i in range(len(a)):
    counter = 0
    for j in range(len(a[0])):
        if a[i][j] == 1:
            counter +=1
    if counter == 0: counter = 1
    a[i] = [a[i][0]/counter,a[i][1]/counter,a[i][2]/counter,a[i][3]/counter]

a = np.transpose(a)


    




#INPUT an adjacency matrix A of 0s,1s and bound on iteration k
#OUTPUT page rank vector
def pr(A,k):

    v = np.zeros ((4,1),dtype = float)
    v[0] = [0.25]
    v[1] = [0.25]
    v[2] = [0.25]
    v[3] = [0.25]
    #A = A**2
    for i in range(k):
        A = np.matmul(A, A)
    lo = np.dot(A, v)
    return lo


print(pr(a,8))
#code output certified by AI (Tuesday office hours)
### if the graph had a builtin multiplication method, it could multiply a matrix by itself to the n power.