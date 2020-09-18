import matplotlib.pyplot as plt
import numpy as np

Data = [(2,1),(5,2),(7,3),(8,3)]

X = np.zeros((4,2),dtype = int)
Y = np.zeros((4,1),dtype = int)
def tp(a):
    XtX,XtY = a.shape
    f = np.zeros((XtY,XtX))
    f = np.asarray([[row[i] for row in a] for i in range(len(a[0]))])
    return f

def mm(a,b):

    r1,c1 = a.shape
    r2,c2 = b.shape
    d = np.zeros(shape = (r1,c2))
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                d[i][j] += a[i][k] * b[k][j]
    return d

for r in range(0,len(Data)):
    X[r][0] = 1
    X[r][1] = Data[r][0]
    Y[r][0] = Data[r][1]


XtX = mm(tp(X),X)
XtY = mm(tp(X),Y)
Betas = np.dot (np.linalg.inv(XtX),XtY)
print(Betas)
xp = [i[0] for i in Data]
yp = [i[1] for i in Data]
plt.plot(xp,yp,"ro")
t = np.arange(0.,10,1)
plt.plot(t,Betas[0][0]+Betas[1][0]*t, "g--")
plt.axis([0,8,0,4])
plt.show()


