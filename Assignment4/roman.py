

def roman(n):

    if n//10 == 0:
        value=""
    elif n//10 == 1:
        value = "X"
    elif n//10 == 2:
        value = "XX"
    elif n//10 == 3:
        value = "XXX"
    elif n//10 == 4:
        value = "XL"
    elif n//10 == 5:
        value = "L"
    elif n//10 == 6:
        value ="LX"
    elif n//10 == 7:
        value = "LXX"
    elif n//10 == 8:
        value = "LXXX"
    elif n//10 == 9:
        value = "XC"
    elif n//10 == 10:
        value = "C"
        

    if n%10 == 0:
        value2= ""
    elif n%10 == 1:
        value2= "I"
    elif n%10 == 2:
        value2= "II"
    elif n%10 == 3:
        value2= "III"
    elif n%10 == 4:
        value2= "IV"
    elif n%10 == 5:
        value2= "V"
    elif n%10 == 6:
        value2= "VI"
    elif n%10 == 7:
        value2= "VII"
    elif n%10 == 8:
        value2= "VIII"
    elif n%10 == 9:
        value2= "IX"




    return value + value2
 
    

    




for i in range(1,100):
    if i % 5 == 0:
        print()
    print(i, roman(i), ", ", end="")