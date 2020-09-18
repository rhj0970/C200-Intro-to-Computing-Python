import random as rn
import math
import numpy as np
import time

def bs(T,L,R):
   
    while L < R:
        m = math.floor((L+R)/2)
        if a[m] < T:
            L = m+1
        if a[m]>T:
            R = m-1
    return L - 1




size = 100000000
a = np.zeros(size,dtype = int)
for i in range(0,size):
    a[i] = int(rn.gauss(100000,40000))

key = a[rn.randint(0,size)]


print("Looking for {0}".format(key))

print("Linear Search...")
print("Starting {0}".format(time.time()))

found = False
for i in range(0,size):
    if a[i] == key:
        found = True
        break
print("Ending time {0}".format(time.time()))

print("\nQuicksort...")
#default is quicksort
a.sort()
print("BFS...")
print("Starting {0}".format(time.time()))

x = bs(key,0,size)
print("Ending time {0}".format(time.time()))