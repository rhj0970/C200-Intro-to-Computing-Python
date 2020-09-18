import math

s1 = 75              # miles/hours
t1 = 4               # hours
t2 = 2020            # min
t3 = 414241          # sec
d1 = 100             # miles
d2 = 1442412


def speed(d, t):
    spd = d/t
    return spd
print(speed(100,4), "miles/hour")

# 2 Finish this function 
# Finds distance in miles using speed (mph) and time (hours)
# Input Parameters: speed s (mph), time t (hours)
# Return Value: distance (miles)
def distance (s, t):
   dist = s*t
   conver = 160.934
   return conver/dist
print(distance(1,4), "kilometers/hour")

# 3 Finish this function
# Finds time in hours using speed (mph) and distance (miles)
# Input Parameters: speed s (mph), distance d (miles)
# Return Value: time (hours)
def time (s, d):
    tim = d/s
    return tim
print(time(75,100))


# 4 Finish this function
# Converts hours to minutes
# Input Parameters: hours numberHours
# Return Value: minutes
def hours_to_min(numberHours):
    min = numberHours*60
    return min
print (hours_to_min(4))


# 5 Finish this function
# Converts minutes to seconds
# Input Parameters: minutes numberMinutes
# Return Value: seconds
def min_to_sec(numberMinutes):
    sec =numberMinutes*60
    return sec
print (min_to_sec(4))


# 6 Finish this function
# Converts feet to miles
# Input Parameters: feet numberFeet
# Return Value: miles
def feet_to_mile(numberFeet):
    feetmile= numberFeet/5280
    return feetmile 
print (feet_to_mile(5))



# 7 Finish this function
# Converts miles to kilometers
# Input Parameters: miles numberMiles
# Return Value: kilometers
def miles_to_kilometers(numberMiles):
    mkm= numberMiles*1.60934
    return mkm
print (miles_to_kilometers(5))


# 8  Finish this function
# Converts kilometers to miles
# Input Parameters: kilometers numberKilometers
# Return Value: miles 
def kilometers_to_miles(numberKilometers):
    kmile= numberKilometers/1.60934
    return kmile
print (kilometers_to_miles(5))



# 9 Finish this function
# Converts miles to feet
# Input Parameters: miles numberMiles
# Return Value: feet
def miles_to_feet(numberMiles):
    milesfeet = numberMiles*5280
    return milesfeet
print (miles_to_feet(10))

# 10 Finish this function
# Converts degrees to radians
# Input Parameters: degrees numberDegrees
# Return Value: radians
def degrees_to_radians(numberDegrees):
    degradian =  numberDegrees*math.pi/180
    return degradian
print (degrees_to_radians(4))

# 11 Finish this function
# Finds the length of side c of a triangle (Law of Cosines)
# where gamma is degrees and is converted to radians
# Input Parameters: side length a, side length b, degrees of angle gamma
# Return Value: length of side c
def side_length_triangle(a, b, gamma):

    c= a**2+b**2-2*a*b*math.cos(gamma)
    c1= math.sqrt(c)
    return c1
print (side_length_triangle(3, 4, 37))


# 12 Finish this function
# Convert Celsius to Fahrenheit 
# Input Parameters: degrees Celsius numberDegreesC
# Return Value: degrees Fahrenheit
def celsius_to_fahrenheit(numberDegreesC):
    celfah= numberDegreesC*9/5+32
    return celfah
print (celsius_to_fahrenheit(5))

# 13 Finish this function
# Converts Fahrenheit to Celsius
# Input Parameters: degrees Fahrenheit numberDegreesF
# Return Value: degrees Celsius
def fahrenheit_to_celsius(numberDegreesF):
    farcelsius = (numberDegreesF-32)*5/9
    return farcelsius
print (fahrenheit_to_celsius(68))

# 13 Finish this function
# Converts Fahrenheit to Kelvin
# Input Parameters: Kelvin numberKelvin
# Return Value: degrees Fahrenheit
def kelvin_to_fahrenheit(numberKelvin):
    kelfah =9/5*(numberKelvin-273)+32
    return kelfah
print (kelvin_to_fahrenheit(50))

# 14 Finish this function
# Given a stock price p and amount change +/- d, 
# calculate the percentage difference
# Input Parameters: stock price p, dollar amount change d
# Return Value: percent change
def percent_change(p, d):
    if p<0:
        return -(1-((p+d)/p))
    else:
        return ((p+d)/p)-1
print (percent_change(5,4))

# 15 Finish this function
# Convert parsecs to kilometers
# Input Parameters: parsecs numberParsecs
# Return Value: kilometers
def parsecs_to_kilometers(numberParsecs):
    par= numberParsecs/3.086*10**13
    return par
print (parsecs_to_kilometers(5))


# 16 Finish this function
# Convert light years to parsecs
# Input Parameters: light years numberLightYears
# Return Value: parsecs
def lightyears_to_parsecs(numberLightYears):
    light= numberLightYears*3.26
    return light
print (lightyears_to_parsecs(3))




print(speed(d1,t1), "miles/hour")
print(miles_to_kilometers(speed(d1,t1)), "kilometers/hour")
print(miles_to_kilometers(speed(d1,t1))/min_to_sec(hours_to_min(1)), "kilometers/sec")
print(celsius_to_fahrenheit(-30), "Fahrenheit")
print(min_to_sec(hours_to_min(1)), "seconds")
print(fahrenheit_to_celsius(-22), "Celcius")
print(celsius_to_fahrenheit(20), "Fahrenheit")
print(kelvin_to_fahrenheit(293), "Fahrenheit")
print(fahrenheit_to_celsius(kelvin_to_fahrenheit(293)), "Celcius")
print(side_length_triangle(8,11,37), " units")
print(degrees_to_radians(30), "radians")
print(percent_change(170.90,3.31), "percent change")
print(percent_change(170.90,-3.31), "percent change")
print(parsecs_to_kilometers(231), "kilometers")
print(kilometers_to_miles(parsecs_to_kilometers(lightyears_to_parsecs(3.5))), "miles")