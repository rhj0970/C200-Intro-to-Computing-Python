def factorial(n):
    print("factorial(" +str(n)+ ")")
    if n ==1:
        print("Base Case")
        return 1
    else:
        print("Inductive Step")
        res = n*factorial(n-1)
        print("Back in factorial(" +str(n) +")")
        print("Intermeidate result: " + str(res))
        return res

print(factorial(5))


def fibfor(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a
#print(fibfor(5))

def fib(n):
    if n ==0 or n ==1:
        return n
    else:
        return fib(n-1) + fib(n-2)

#print(fib(5))

import os
print(os.getcwd())

f= open("Lab7/lab7.txt", "r")
print(f.read())
f.close()