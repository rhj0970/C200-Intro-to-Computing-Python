import functionsandloops as fal
tList = [8,3,1]
test1 = fal.sumListFor(tList)
print("sumListFor: ", test1, "?=", 12, " ", test1 == 12)


test2 = fal.multiplyListFor(tList)
print("multiplyListFor: ", test2, "?=", 24, " ", test2 == 24)


d = {1:2, 3:4, 5:6}
test3 = fal.flippingKeyValues(d)
print(d)
print(test3)