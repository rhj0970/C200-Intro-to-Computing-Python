x = True
y = False
z = 12
a = 10
b = not (x or not (x or y)) and True


if b:
    print("Happy")
elif b and x:
    print("Valentines")
elif not b and not x and not y:
    print("day!")
else:
    None
###################


#2#################
if (z < a):
    print("C200")
elif (2*a<z):
    print("is bliss")
else:
    None
###################


#3#################
if not (not (x and y) or not x):
    print(a)
###################
#4#################
if (2 > z) or not x:
    print("1")
elif 2 == 1:
    print("2")
elif y and not x:
    print("3")
elif y:
    print("4")
     
def f(x):
    return (x==4)*100 + (x==3)*10 + (x==2)*1000 + (x!=4)*(x!=3)*(x!=2)*100000

print(f(4))
print(f(3))
print(f(2))
print(f(1))
