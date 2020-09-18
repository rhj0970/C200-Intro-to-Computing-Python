import math

# INPUT function fn, start is a, end is b,
# n is an even number of intervals
# RETURN approximate area under the curve
def simpson(fn,a,b,n):
    
    delta_x = (b - a)/n
    interval = lambda i: a + i*delta_x
    sum = fn(a)
    for j in range(1,n):
        if j %2 == 0:
            sum += 2*fn(interval(j))
        else:
            sum += 4*fn(interval(j))
    return ((b - a) / (3*n)) * (sum + fn(b))

    



# convert string to either number or expression
def convert(x):
    if x.isnumeric():
        return float(x)
    else:
        return eval(x)
    


with open("integralfile.txt", "r") as xfile:
    xlines = [d.split(",") for d in xfile.read().split("\n")]

for i in xlines:
    body = i[0]
    fn = eval("lambda x : " + body)
    a = convert(i[1])
    b = convert(i[2])
    n = convert(i[3])
    answer = convert(i[4])
    integration = simpson(fn,a,b,n)
    error = abs((answer - integration)/answer)
    print("f(x) = {0} over [{1},{2}] is {3:.3f}".format(body,a,b,integration))
    print("Actual answer is {0:.3f}".format(answer))
    print("Error is {0:.3f}".format(error))
