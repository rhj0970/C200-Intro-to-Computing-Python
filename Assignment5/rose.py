def is_member1(x,ylist):
    if x in ylist:
        return True
    else:
        return False

def is_member2(x,ylist):
    for i in ylist:
        if x in ylist:
            return True
        else:
            return False
       

def is_member3(x,ylist):
    i =0
    found = False
    while i < len(ylist):
        if x == ylist[i]:
           found = True
        i+=1    
    return found

def is_member4(x,ylist):
   
    for i in ylist:
        if x in ylist:
            found = True
        else:
            found = False
        return found



y = [1,3,5]
x = [1,2,3,4]

for i in y:
    print("1 ", is_member1(i,x))
    print("2 ", is_member2(i,x))
    print("3 ",is_member3(i,x))
    print("4 ",is_member4(i,x))
