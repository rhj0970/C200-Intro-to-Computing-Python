f = lambda x: x**6 - x - 1

def sign(x):
    if x<= 0:
        return -1
    else:
        return 1




def bisect(f,a,b,tau):
    while True:
        c = (a+b)/2
        if b-c <=tau:
            return c
        else:
            if sign(f(b)) * sign(f(c)) <= 0:
                a = c
            else:
                b = c
        print("{0:.5f} {1:.5f} {2:.5f} {3:.5f} {4:.5f}".format(a,b,c,b-c,f(c)))


bisect(f,1.0,2.0,.001)

