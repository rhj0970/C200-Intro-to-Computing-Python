import math

APR = float(input("What is your APR: %"))
C = float(input("What is the amount owed on the credit card: $"))
p = float(input("What it the monthly payment made: $"))

apr = APR/100
i = apr/12
n = -math.log(1-(i*C/p)) / math.log(i+1)


print("You’ll make ", math.ceil(n), " payments.")
