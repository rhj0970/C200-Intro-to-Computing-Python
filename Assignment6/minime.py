def min(x,y):
    if x <y:
        return x
    else:
        return y



def MIN(lst):
   # if len has one number
    if len(lst) == 1:
        return min (lst[0],lst[0]) 
    # 
    else: 
        return min(lst[0], MIN(lst[1:]))



# for loop and index into list
def min1(x):
#TO DO: Implement function
    minvalue = x[0] 
    for i in range (0,len(x)):
        if x[i] < minvalue:
            minvalue =x[i]
    return minvalue

# for loop and list iteration
def min2(x):
    minvalue = x[0] 
    for i in x:
        if i < minvalue:
            minvalue=i
    return minvalue

# while loop and index
def min3(x):
    minvalue = x[0]
    i = 1
    while  i<len(x):
        if minvalue >x[i]:
            minvalue = x[i]
        i +=1
    return minvalue



# while loop list iteration
def min4(x):
    minvalue = x[0]
    
    while  x != []:
        if minvalue >x[0]:
            minvalue = x[0]
        x = x[1:]
    
    return minvalue



# for loop reverse index
def min5(x):
    small = x[-1]
    for i in range(len(x)-1,-1,-1):
        if x[i] < small:
            small = x[i]
    return small

x = [1,42,-1,22,0,12]

mf = [MIN, min1, min2, min3, min4, min5]

for f in mf:
    print("{0}({1}) = {2}".format(f.__name__,x,f(x)))

