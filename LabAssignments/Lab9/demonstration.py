import math

#question 1
f = lambda r :math.pi*(r**2)
print (f(5))


#question 2
lst1 = [1,2,3,4,8]
lst2 = [4,1,4,2]
k = map(f,lst1,lst2)
k = map( (lambda x,y:y if y>x else x), lst1, lst2)

for i in k:
    print(i)
for i in k:
    print(i)




#question 3
def filter (x):

    aa = [1,2,3,4,5,6]
    if x:
        kor = filter( (lambda x:x<4), aa)
        return True
    else:
        return False

print (list(filter)


def comprehension(x):
#question 4
    lst = [1,2,3,4,5,6,7]
    k = [x*20 for x in lst if x<4]
    print (comprehension)

