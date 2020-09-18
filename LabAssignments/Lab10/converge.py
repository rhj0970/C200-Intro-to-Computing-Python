import numpy as np
#import matplotlib.pyplot as plt


#Bisection Method is a root finding algorithm like Newton's method - but instead it uses 2 endpoints to determine the root of a function
#Requires f(a) and f(b) to have different signs (+,-), which implies that the root is between them
#If the middle of a and b, f(c), is the same sign as f(a), we know that the root is between c and b, so a becomes the current c
#Otherwise we know it's between a and c, so b becomes the current c
def f(x):
	return x**3 - x - 2
def bisection_converge(a,b,tau):
	c = (a + b)/2
	clist = [c]
	change = tau + 1
	while f(c) != 0 and change > tau:		
		if np.sign(f(c)) == np.sign(f(a)):
			a = c
		else:
			b = c
		change = abs(c - (a+b)/2)
		c = (a + b)/2
		clist.append(change	)
	return clist
print(bisection_converge(1,2,.0025))

#Write bisection_iteration that returns a numpy array with 10 iterations when called with bisection_iterations(1,2,10)
#Hint - convert the while loop into a for loop removing the boolean expressions and replacing them with a range using iterations like the Code Demonstrations
def bisection_iteration(a,b,iterations):
    xlist = [x]
    change = x
    iteration = 10
    for i in range(0,iteration):
        newx = x - (f(x)/fp(x))
        change = abs(newx -x)
        x = newx
        xlist.append(x)
    return xlist
pass

result = bisection_iteration(1,2,10)
print(result)

#Write the plot functions (Give your plot a title, axes names, etc.) and plot the result of bisection_iterations 	


#Using the plot, determine the best tau for the problem and call bisection_converge.
#print(bisection_converge(1,2, your_number_here))

#Write a class University who's init function takes in the name, nickname and enrollment of a school. 
#Write a function set_enrollment that allows you to change the enrollment.
#Write one more function get_info that prints out the University's name, nickname and enrollment level
#Uncomment out test code below to test your class!
class college:
   
    def __init__(self, NAME, NICKNAME, ENROLLMENT):
        self.name = NAME
        self.nickname = NICKNAME
        self.enrollment = ENROLLMENT

    def getname(self):
        return self.getname
    def getnickname(self):
        return self.nickname
    def set_enrollment(self, e):
        self.enrollment = e
        return self.enrollment

    def get_info(self):
        return self.name + " "+self.nickname + " " + str(self.enrollment)


indiana = college("Indiana", "Hoosiers", 43710)
purdue = college("Purdue", "Boilermakers", 41573)
print(indiana.get_info())
print(purdue.get_info())
purdue.set_enrollment(0)
print(purdue.get_info())


