
A = float(input("Do you have adominal pain? "))
B = float(input("Do you have nausea? "))
C = float(input("Do you hvae fever? "))
if A+B+C >= 3:
    print ("Appendicitis")

D = float(input("Do you have vomiting? "))
if A+B+C+D >= 3:
    print ("Appendicitis")

E = float(input("Do you have loss of appetite? "))
if A+B+C+D+E >= 3:
    print ("Appendicitis")
else:
    print ("No Appendicitis")