#This is the bank as a dictionary.
#The key is the type and value is the number of pints.
# bank["O+"] == 2
bank = {"A+":4, "A-":2, "O-":0, "O+":2, "B+":5, "B-":2, "AB+":4, "AB-":2}

#1 Parameters donor's blood type donor_blood_type
#Return a string of the types that can accept the blood
#If the donor_blood_type is unknown, then return "Uknown"
def red_blood_compability(donor_blood_type):
    if donor_blood_type == "A+":
        return "A+","AB+"
    elif donor_blood_type == "A-":
        return "O-","O+","A-","A+"
    elif donor_blood_type == "O-":
        return "A+","A-","O-","O+","B+","B-","AB+","AB-"
    elif donor_blood_type == "O+":
        return "AB+","B+","A+","O+"
    elif donor_blood_type == "B+":
        return "B+","AB+"
    elif donor_blood_type == "B-":
        return "B-","B+","AB+","AB-"
    elif donor_blood_type == "AB+":
        return "AB+"
    elif donor_blood_type == "AB-":
        return "AB-"
    else:
        return "unknown"




# Show the current bank
# This is a dictionary
def show_bank():
    print(bank)

#2 Parameters donor blood type is donor, recipient's type is recipient, and pints is the 
# number of pints that donor will give to recipient using the bank.
# Return True if the blood bank has enough pints to give 
# and remove the amount of pints used from the bank
# Return False if either the recipient can't recieve the type or there's not enough blood
def transfusion(donor, recipient, pints):

    if (donor =="A+" and recipient == "AB+"):
        bank ["A+"]=3
        return True

    elif (donor == "A-" and recipient == "O-"):
        
        return True

    else:

        return False


print(red_blood_compability("A+"))
print(red_blood_compability("O-"))
print(red_blood_compability("C+"))


show_bank()
print(transfusion("A+","AB+",1))
show_bank()
print(transfusion("A-", "O-",1))
show_bank()
print(transfusion("A-", "B+",1))
show_bank()
print(transfusion("AB-", "AB+",3))
