#f = lambda x: x**6 - x - 1
#fp = lambda x: 6*(x**5) - 1

def fpa(f):
    h = .000001
    return lambda x: (eval(f)(x+h)-eval(f)(x-h))/(2*h)



def newton(f,fp,x,tau):
    
    def n(x,i):
        for i in range(0,b):
            
            while eval(f)(x) > tau:
                
                print("{0} {1:.5f} {2:.5f}".format(i,x,eval(f)(x)))
                x = x - eval(f)(x)/fp(x)
                i += 1
            return x

    n(x,0)

f = "lambda x:"+ input("enter function: ")
x = float(input("enter number for x0: "))
tau = float(input("enter number for tau: "))
b = int(input("Enter number: "))
print(eval(f)(x))
newton(f,fpa(f),1.5,.0001)