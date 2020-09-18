#inputs signals A,B, Cin
#outputs F
def xor (A,B):
    if A and B:
        return False
    elif A or B:
        return True
    else:
        return False
    






def F(A,B,Cin):
    ABC = xor(xor(A,B),Cin)
    return ABC

#inputs signals A,B, Cin
def G(A,B, Cin):
    XYZ = (A and B) or ((xor(A,B) and Cin))
    return XYZ       

signals = [0,1]

for A in signals:
    for B in signals:
        for Cin in signals:
            print(A,B,Cin,F(A,B,Cin),G(A,B,Cin))

