import numpy as np

#INPUT two matrices a,b
#RETURN product ab
def mm(a,b):

    r1,c1 = a.shape
    r2,c2 = b.shape
    d = np.zeros(shape = (r1,c2))
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                d[i][j] += a[i][k] * b[k][j]
    return d


#TO DO: Implement function

#INPUT scalar n and matrix add
#RETURN scalar product n
def sm(n,a):
    r1,c1 = a.shape
    e = np.zeros(shape = (r1,c1))
    for i in range(len(a)):
        for j in range(len(a[0])):
            e[i][j] = n*a[i][j]
    return e



#TO DO:Implement function

#INPUT matrix n x m
#RETURN transpose matrix m x n
def tp(a):
    r1,c1 = a.shape
    f = [[row[i] for row in a] for i in range(len(a[0]))]
    return f

#INPUT two matrices a,b
#RETURN sum a + b
def add_m(a,b):
    r1,c1 = a.shape
    r2,c2 = b.shape
    d = np.zeros(shape = (r1,c2))
    for i in range(len(a)):
        for j in range(len(b[0])):
            d[i][j] = a[i][j] + b[i][j]
    return d

a = np.array([[1,2,4],[3,4,3]])
b = np.array([[-1,0],[1,-5],[-3,1]])
print("numpy product\n", np.dot(a,b))
d = mm(a,b)
print(d)
# in order to print orderly


print("numpy scalar product\n", 4*a)
e = sm(4,a)
print(e)


print("numpy tranpose\n", np.transpose(a))
f = tp(a)

print(f[0])
print(f[1])
print(f[2])

print("numpy addition\n", a + a)
g = add_m(a,a)
print(g)

