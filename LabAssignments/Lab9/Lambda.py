lst1 = [5, 2, 5, 7, 10]
lst2 = [10, 5, 1, 8, 15]
lst3 = ["deep", "in", "the", "hundred", "acre", "wood"]
##
for i in filter((lambda x: "r" in x), lst3):
    print(i)
##
k = [x+"four" for x in lst3 if len(x)==4]

print(k)

##
print((lambda x,y,z: x+y+z)("no", "more", "homework"))



k = map(lst1,lst2)
k = map( (lambda x,y: x+y), lst1, lst2)

for i in k:
    print(i)
for i in k:
    print(i)

##
k = ((lambda x,y:y if x>y else x**2), lst1)
print (k)