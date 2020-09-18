import math
import matplotlib.pyplot as plt
import numpy as np
with open("acme_zyx.txt","r") as stock:
            list = stock.read().splitlines()
Acme = list[0]
Acme = Acme[int(Acme.index("["))+1: int(Acme.index("]"))]
Acme = Acme.split(", ")
for i in range(len(Acme)):
    Acme[i] = float(Acme[i])
ZXY = list[1]
ZXY = ZXY[int(ZXY.index("["))+1: int(ZXY.index("]"))]
ZXY = ZXY.split(", ")
for i in range(len(ZXY)):
    ZXY[i] = float(ZXY[i])

def mean(lst):
    return(sum(lst)/len(lst))
   # for i in range(0,len(lst)):

     #   acMean = sum(Acme)/len(Acme)
       # zxMean = sum(ZXY)/len(ZXY)
       # return acMean,zxMean

def sd(xlst,abc):
    k = [xlst[0] for x in xlst]
    y = [xlst[1] for x in xlst]
    xlst = []
    for i in k:
        xlst.append(i-abc[0]**2)
    tot = sum(ylst)
    var = tot/(len(xlst)-1), tot/(len(ylst)-1)
    sdlst = []
    for i in range(len(k)):
        numx = (k[i]-abc[0])
        numy = (y[i]-abc[1])
        denox = sqrt(var[0])
        denoy = sqrt(Var[1])
        sdlst.append(numx/denox)*(numy/denoy)
    return sum(sdlst)/(len(sdlst))
x = [[2,3],[4,3],[1,1.4],[1,.5],[5,3]]
r = sd(x,mean(x))

print(r)
plt.plot([i[0] for i in x],[i[1] for i in x], 'ro')
t = np.arange(0,6,.1)
plt.plot(t,t*.65 + .5,'g--')
plt.axis([0,6,0,6])
plt.xlabel("A values")
plt.ylabel("B value")
plt.title("r = {0:.3}".format(r))
plt.show()