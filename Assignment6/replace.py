#Non-recursive
def replace(new,old,x):
    i =0
    count = 0
    replacement = []
    
    if old==x[i]: 
        replacement = replacement + [new]  
        i+=1  
        return 

    else:
        replacement = replacement + [x[i]]   
        i+=1
        return replacement
#Recursive
def REPLACE(new,old,lst):
    if lst==[]:
        return []
    elif lst[0] == old:
        return [new] + REPLACE(new, old, lst[1:])
    return [lst[0]] + REPLACE(new, old, lst[1:])
          
        
 


x = [1,3,2,4,2,1,1,2,2,1]
print(REPLACE(10,1,x))
print(REPLACE(1,3,REPLACE(1,3,x)))


