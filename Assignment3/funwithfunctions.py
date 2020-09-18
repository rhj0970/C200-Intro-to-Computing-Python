import math

def hi (d,r,t):
    hi = d*(math.exp(1)**(r*t))
    return hi

print(hi(1000,.02,10))



def N(n_0, m, t):
    
    N = n_0*math.e**(m*t)
    return N
print(N(500,100,4))



def N_t(t):
 N_t = 71.8*math.e**(-8.96*math.e**(-.0685*t))
 return N_t

print(math.floor(N_t(1000)))


def D(t):
    D = ((9/2.6)*t)/(2*(t**2)+3)
    return D
print(D(1))


def r(t):
    r= 1.5207*(t**4) - 19.166*(t**3)+62.91*(t**2)+(6.0726*t)+1026
    return r
print(r(4))


def p(x):
    p= 4*(x**2)-100*x-1000
    return p
print(p(10))


def W(p1,p2):
    W = (8.314*300)*pow(p1/p2*math.e)
    return W
print(W(10,1))




#question 8 (didn’t do 7 yet)


def depreciate(c,s,life):
    depreciate = (c-s)/life
    return depreciate

print(depreciate(20000,1000,5))



def L(k,V,A,C):

    L = k*(V**2)*A*C
    return L

print(L(0.0033,33.8,512,0.515))

