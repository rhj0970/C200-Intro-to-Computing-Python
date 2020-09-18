Ta = float(input("Enter Farenheit Temperature: "))
V = float(input("Enter wind speed mph: "))
Twc = 34.74 + 0.621*Ta - 35.75*V**.16 + .4275*Ta *V**.16

print("The windchill for", Ta,"deg and", V, "mph is", Twc, "deg")