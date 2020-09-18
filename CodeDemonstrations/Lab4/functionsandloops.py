def sumListFor(alist):

#Sums all the numbers in a list using a for loop#
    result = 0
    for number in alist:
        result += number # reuslt+number#
    return (result)

def multiplyListFor(aList):
    #multiply the nummber in a list together us ing a for loop#
    result = 1
    for i in range(len(aList)):
        number = aList[i]
        result *= number   #result*number
    return result

def flippingKeyValues(dct):
    #create dictionares that flipp keyvalues#
    if not type(dct) == dict:
        return dict()
    dNew = {}
    for k in dct.keys():
        v = dct[k]
        dNew[v] = k
    return dNew
