import LoopsAndContainers as lac
import numpy as np

d = {0:"z", 1:"o", 2:"t", 3:"f", 4:"f", 5:"f"}
print("Our dictionary: "+str(d))
print("Keys: "+str(d.keys()))
print("Testing evenCount2")
print(lac.evenCount2(d))




print("Testing evenCount3")
print(lac.evenCount3(6))



print("positionalSumArray2 Test 1")
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print (lac.positionalSumArray2(arr1,arr2))