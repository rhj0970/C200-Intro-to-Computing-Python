# Input Parameter: a list of numbers x
# Returns: the max number in list x (does not have to be unique)
def maxFor(x):
    maxvalue = x[0]  
    i =0
    while i > maxvalue:  
           maxvalue = i
           i +=1
    return maxvalue  



# Input Parameter: a list of numbers x
# Returns: the minimal number value in list x (does not have to be unique)
def minFor(x):
    minvalue = x[0] #첫번째와 동일하지만 minvalue 를 구하는 것 이므로 부등호만 바꿔주면됨
    for i in x:
        if i < minvalue:
            minvalue=i
    return minvalue


# Input Parameters: a number x and a list of numbers lst
# Returns: the list lst with all occurrences of x removed
def myRemove(x, lst):
    stack = 0     #0부터 시작해야 차례대로 감/ 만약에 홀수로 가고싶으면 1을 넣으면 됨
    removingvalue = []   
    
    for i in range(0,len(lst)):     
        if x==lst[stack]:    #x 예를들어 "a"가 리스트 즉a 안에있는 수랑 같으면 (처음 스택이 0이므로) 걍 지나감 바로 밑의 식을 이용해서
            stack = stack +1  #하나씩 더하므로 lst[0], lst[1].... 처럼 지나감
        else:
            removingvalue = removingvalue + [lst[stack]]    #빈 startvalue[] 에 더하는 것이므로 없어짐
            stack = stack +1
    return removingvalue





# Input Parameters: a number oldX, a number newX and a list of numbers lst
# Return Value: the list lst with all occurrences of oldX replaced with newX
def myReplace(oldX, newX, lst):

    count = 0
    replacement = []
    
    for i in range(0,len(lst)):
        if oldX==lst[count]: #리스트안에 oldX 가 있으면
            replacement = replacement + [newX]  #output 아직 없으니까 newX 즉 새로운 값을 넣어줌
            count = count +1   #지나가게 하는것

        else:
            replacement = replacement + [lst[count]]   #나머지도 계속하기 위함
            count = count +1
    return replacement








# Input Parameters: two lists x and y, x = [x1, x2, x3, ..., xk] and y = [y1, y2, y3, ..., yk]
# Returns: a new list with the following structure [x1, y1, x2, y2, x3, y3, ..., xk, yk]
# Note: assume that both lists are same length
def myLeftMerge(x, y):
    count = 0
    result = []

    for i in range (0,len(x)):
        
        result = result + [x[count]]
        result = result + [y[count]]
        count = count+1
    return result
	
# Input Parameter: takes a list of lists of numbers [[x1, x2, x3, ...,  xn], [y1, y2, y3, ..., ym],...]
# Returns: a single list of numbers where each element is product of the inner list at that position, [x1*x2*x3*...*xn, y1*y2*y3*...*ym, ...]
def listProducts(x):
    result = []

    for j in range(len(x)):
        y = x[j]
        result1 = [1]
        
        for i in range( len(y)):
              number = y[i]
              result1[0] = result1[0]*number   #result*number

        result = result + result1

        
    return result

	

# Input Parameter: a list x of objects [x1, x2, x3,..., xn]
# Returns: a list with the string objects removed

def removeString(x):    
    startvalue = []   #the reason why it's blank is because it's deleting it


    for i in range(len(x)):
        if type (x[i]) is not str:
            startvalue = startvalue + [x[i]]  #list can only be added with the list 
                                                #so that's why we use [x[i]] instead of (x[i])


    return startvalue
	

# Input Parameter: a string x
# Returns: the string with all vowels, upper and lower case removed

def removeVowels(x):
    vowelsremove=""
    for i in x:
        if i not in "aeiouAEIOU":
            vowelsremove = vowelsremove+i
    return vowelsremove


# Data
x = [1,42,24,22,61,100,0,42]
y = [2]
z = [555,333,222]
nlst = [x,y,z]
c = [0,1,1,0,2,1,4]
a = ["a","b","b", "a", "c","b","e"]
b = [1,1,2,1,1,2,1,1,2,1,3,1]


for i in nlst:
    print(minFor(i))
    print(maxFor(i))

print(myRemove("a",a))
print(myRemove("b",a))
print(myRemove("z",a))
print(myRemove(1,b))
print(myRemove(2,b))
print(myRemove("a",b))
print(myReplace("a",":)",a))
print(myReplace(1,0,b))
print(removeVowels("the lazy brown fox jumped over the eager dog"))
print(listProducts([[1],[2,3,4],[10,10,10,10]]))
print(removeString(["This",1, "is", "very", 3, [4], "exciting"]))
print(myLeftMerge(a,b))
print(myLeftMerge(['aa','bb'],[1,2]))
