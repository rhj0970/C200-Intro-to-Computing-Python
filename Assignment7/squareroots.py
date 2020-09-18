import numpy as np
import matplotlib.pyplot as plt

est = np.zeros (10)
g = np.zeros (10)


def error(s, x):
    return abs((s-x**2)/(2*x))

def bakhshali(s, epsilon, estimate):
    a = (s-(estimate**2))/(2*estimate)

    k = estimate + a - (a**2)/(2*(estimate+a))
    return k

    
    
def square_root(s,epsilon,estimate):
    x = estimate
    i =0
    est[i]= error(s,x)
    g[i] = x
    while error(s,x) > epsilon:
        i+=1
        x = (x+s/x)*(1/2)
        est[i] = error(s,x)
        g[i] = x
        
        
    return g



t1 = np.arange(1,8,1)

plt.ylabel("Initial Estimate")
plt.xlabel("Iterations")
plt.title("Convergence of Square Root")

g = square_root(1000,.00005,500)
print(g)
plt.plot(t1,g[t1],'r-o')

g = square_root(1000,.00005,775)
print(g)
plt.plot(t1,g[t1],'b-o')

g = square_root(1000,.00005,3)
print(g)
plt.plot(t1,g[t1],'g-o')

plt.show()

