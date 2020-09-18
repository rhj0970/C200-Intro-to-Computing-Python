
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return x**2
def fp(x):
    return 2*x
def newton_iteration(x, iterations):
    ra = np.zeros(iterations)
    for i in range(iterations):
        ra[i] = x - (f(x)/fp(x))
        x= ra[i]
    return ra
results = newton_iteration(1,5)
plt.ylabel("estimate")
plt.xlabel("iterations")
plt.title("convergence of newton method")
print(results)
plt.plot([i for i in range(5)], results, 'r-o')
plt.show() 


def newtonchange(x):
    xlist = [x]
    change = x
    tau = .1
    while change >tau:
        newx = x - (f(x)/fp(x))
        change = abs(newx -x)
        x = newx
        xlist.append(x)
    return xlist

results = newtonchange(1)
plt.ylabel("estimate")
plt.xlabel("iterations")
plt.title("convergence of newton method")
print(results)
plt.plot([i for i in range(len(results))], results, 'r-o')
plt.show() 