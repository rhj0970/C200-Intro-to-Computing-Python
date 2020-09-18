
def circuit(A, B, C):
    def Z():
    
        if A and B:
            return True

        elif (A and B) or C:
            return True
        else:
            return False
        return Z
    return not Z or not C

print(0,0,0,circuit(0,0,0))
print(0,0,1,circuit(0,0,1))
print(0,1,0,circuit(0,1,0))
print(0,1,1,circuit(0,1,1))
print(1,0,0,circuit(1,0,0))
print(1,0,1,circuit(1,0,1))
print(1,1,0,circuit(1,1,0))
print(1,1,1,circuit(1,1,1))
