def addition(n1, n2):
    """
    Takes n1 and adds n2 to the value
    """
 
    print ("addition function")
    return n1+n2
print(addition(1, 2))


def subtraction (tomato, idaho):
    "subtracts tomato from idaho"
    print ("subtraction function")
    a = addition(-tomato, idaho)
    return a
print(subtraction(32,15))


def division(d1, d2):
    #does the follwoing: d1,d2
    print ("division function")
    if d2 == 0:
        return 0
    return d1/d2
print (division(5, 0))


def welcomePrint():
    name = input("what is your name? >")
    print("hello" + name)

print(welcomePrint())

def welcomeReturn(name):
    return "Hello" + name

print(welcomeReturn("Jason"))

print(division(addition(5,3), subtraction(100,98)))