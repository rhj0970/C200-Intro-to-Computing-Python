def s(n):
    if n == 0:
        return n
    else:
        return s(n-1)+n
print (s(5))

def s1(n):
    if n == 0:
        return n
    else:
        return (n*(n+1))/2
print (s1(5))

def p(n):
    if n == 0:
        return 10000
    else:
        return p(n-1)+((.02*p(n-1)))

print (p(5))

def p1(n):
    if n ==0:
        return 10000
    else:
        return ((1.02)**n)*10000
print (p1(5))


def b(n):
    if n ==1:
        return 2
    elif n == 2:
        return 3
    else:
        return b(n-1)+b(n-2)
print (b(10))

def c(n):
    if n == 1:
        return 9
    else:

        return 9*c(n-1)+10**(n-1)-c(n-1)
print (c(10))

def d(n):
    if n == 0:
        return 1
    else:
        return 3*d(n-1)+1
print (d(10))

def d1(n):
    if n ==0:
        return 1
    else:

        return (3**(n-1)-1)/2
print (d1(10))