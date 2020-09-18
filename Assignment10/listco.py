import numpy as np

Data = [(2,1),(5,2),(7,3),(8,3)]

X = np.zeros((4,2),dtype = int)
Y = np.zeros((4,1),dtype = int)


S_y = sum([i[1] for i in Data])
S_x2 = sum([i[0]**2 for i in Data])
S_x = sum([i[0] for i in Data])
S_xy = sum([i[0]*i[1] for i in Data])

Beta_0 = (S_y*S_x2 - S_x*S_xy)/(4*S_x2-(S_x)**2)
print(Beta_0)
Beta_1 = (4*S_xy - S_x*S_y)/(4*S_x2 - (S_x)**2)
print(Beta_1)
