# Task 1: Finish the 4 following functions

def maxThree(x, y, z):
    """
    Returns the max of the three parameters
    """
    if x >=y and x>=z:
        return x
    elif y>=z and y>=x:
        return y
    else:
        return z
print (maxThree(3,5,7))

    


def minThree(p1, p2, p3):
    """
    Returns the min of the three parameters
    """

    if p1<=p2 and p1<=p3:
        return p1
    elif p2<=p3 and p2<=p1:
        return p2 
    else:
        return p3
print (minThree(3,4,5))



def maxTwoSum(tomato, potato, idaho):


    if potato+idaho>= tomato and potato+tomato>= idaho:
        return potato+idaho
    elif tomato+idaho>=potato and tomato+potato>= idaho:
        return tomato+idaho
    else:
        return idaho+potato

print (maxTwoSum(3,4,5))


def minThree(x,y,z):
    if x+y<=z+x and x+y<y+z:
        return (x+y)
    elif y+z<=x+y and y+z<=x+z:
        return (y+z)
    else:
        return (x+z)
print (minThree(5,6,7))


# Rewrite the 2 problems from assignment 1 but ...

# Task 2: Uncomment and put in the appropriate number of parameters
#         to complete both a "windchill" and "creditcard" function

# def windchill( """ Replace with correct parameters """):
    # Takes the appropriate number of parameters to solve the problem. Returns the appropriate value

# def creditcard( """ Replace with correct parameters """):
    # Takes the appropriate number of parameters to solve the problem. Returns the appropriate value

def windchill(Ta, V):

    Twc = 34.74 + 0.621*Ta - 35.75*V**.16 + .4275*Ta *V**.16
    print("The windchill for", Ta,"deg and", V, "mph is", Twc, "deg")
windchill(5,20)

import math
def creditcard(APR, C, p):

    apr = APR/100
    i = apr/12
    n = -math.log(1-(i*C/p)) / math.log(i+1)
    print("You’ll make ", math.ceil(n), " payments.")
creditcard(19,1000,25)





# Task 3: Uncomment and make the following function with no parameters 
#         to complete both a "windchill_input" and "creditcard_input". 
#         Both functions to ask for "input()" inside the function and 
#         print out the value. DO NOT RETURN

def windchill(Ta=float(input("Enter Farenheit Temperature: ")), V=float(input("Enter wind speed mph: "))):

    Twc = 34.74 + 0.621*Ta - 35.75*V**.16 + .4275*Ta *V**.16
    print("The windchill for", Ta,"deg and", V, "mph is", Twc, "deg")
windchill()

import math
def creditcard(APR=float(input("What is your APR: %")), C=float(input("What is the amount owed on the credit card: $")), p=float(input("What it the monthly payment made: $"))):

    apr = APR/100
    i = apr/12
    n = -math.log(1-(i*C/p)) / math.log(i+1)
    print("You’ll make ", math.ceil(n), " payments.")
creditcard()
