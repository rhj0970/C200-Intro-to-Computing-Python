# Input Parameter: a list of numbers x
# Returns: the max number in list x (does not have to be unique)
def maxFor(x):
    max = x[0]       
    for i in x:      
        if i > max:  
           max = i   
    return max 


# Input Parameters: list of numbers xlst, and number v
# Returns: list xlst without v
def remove(xlst, v):
     stack = 0     
     removingvalue = []   
     for i in range(0,len(lst)):     
        if v==xlst[stack]:   
            stack = stack +1  
        else:
            removingvalue = removingvalue + [xlst[stack]]   
            stack = stack +1
        return removingvalue


# Input Parameters: list of numbers xlst
 # Returns: smallest number in list
# Assume len(xlst) > 0
def min(xlst):
     minvalue = x[0] 
     for i in x:
        if i < minvalue:
            minvalue=i
        return minvalue



#TODO: implement this function


# Input Parameters: list of numbers xlist
# Returns: second smallest number in the list
# You can only use the functions above and assignment states

x = [[1,2,3,4],[4,5,0,1],[22,21,31,10]]
def second_smallest(x):
     for i in x:
        minvalue = i[0]

        for j in i:           
            if j < minvalue:
                minvalue=j
        
        i.remove(minvalue)
        minvalue = i[0]
        for j in i:
            if j < minvalue:
                minvalue=j
        print(minvalue)
        
second_smallest(x)    

        
            



     

 








