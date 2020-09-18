f = lambda x: x**6-x-1
def secant(f,x0,x1,tau):
    n=0

    while abs(f(x1))>=tau:
        tmp = x1
        x1 = x1-f(x1)*((x1-x0)/(f(x1)-f(x0)))
        x0 = tmp
        n += 1
        print("{0:.5f} {1:.5f} {2:.5f} {3:.5f} ".format(x0,f(x0),f(x1),x0-x1))
    return x1


secant(f,2.0,1.0,.0001)