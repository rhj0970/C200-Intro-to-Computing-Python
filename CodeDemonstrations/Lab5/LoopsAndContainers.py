import random as rand
import numpy as np



def evenCount2(dictionary):

    print("In evenCount2")
    print("Dictionary: " +str(dictionary))
    print("Keys in dictionary: "+str(dictionary.keys()))
    count=0
    for key in dictionary:    
        print("key: "+str(key))
        if key%2==0:
            count+=1
        print("Count: "+str(count))
        print("="*10)
    return count



def evenCount3(n):
    # 랜덤숫자중에 짝수 찾기
    randomlist = []    #randomlist 가 list 임을 나타냄
    i=0
    while i <n:
        randomlist += [rand.randint(1,100)]
        i += 1
    i=0
    count =0
    while i <len(randomlist):
        if randomlist[i]%2 ==0:
            count += 1
        i +=1
    print(randomlist)
    return count





def positionalSumArray2(a1,a2):
    #given 2 numpy arrays, add the positional sum
    #if not the same 길이, return a numpy array of length 1 with value
    if a1.size != a2.size:
        return np.array([0])
    s = a1.size
    arr = np.zeros(s)
    for i in range(s):
        arr[i] =a1[i]+a2[i]
    return arr 






















            

   
        