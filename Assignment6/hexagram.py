symbol = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}


def hex_dec(hex):

    power = len(hex) - 1
    num = 0

    for i in hex:
        
        num += symbol[i] * 16 ** power
        power -= 1

    return num








hex = input("Hex: ")
print(hex_dec(hex))
