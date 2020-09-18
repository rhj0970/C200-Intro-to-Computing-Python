Ursala_married = True
Ursala_income = 252225
Kaiser_married = False
Kaiser_income = 375000
Shilah_married = True
Shilah_income = 77399




#1 Finish this function
# Calculates the taxes an unmarried person owes for 2018
# Input Parameters: amount of income in USD income
# Return Value: amount taxes owed (USD)
def unmarriedTax(income):
    if income>500000:
        return income*.37
    elif income>200000:
        return income*.35
    elif income>157500:
        return income*.24
    elif income>38700:
        return income*.22
    elif income>9525:
        return income*.12
    else:
        return income*.1



# 2 Finish this function
# Calculates the taxes a married person owes for 2018
# Input Parameters: amount of income in USD income
# Return Value: amount taxes owed (USD)
def marriedTax(income):
    if income>600000:
        return income*.37
    if income>400000:
        return income*.35
    if income>315000:
        return income*.24
    if income>77400:
        return income*.22
    if income>19050:
        return income*.12
    else:
        return income*.1


# Calculates the taxes an individual owes for 2018
# Input Parameters: amount of income in USD income and marital status  
#Boolean maritalStatus
# Return Value: amount taxes owed (USD)
def tax(income, maritalStatus):
    if(maritalStatus):
        return marriedTax(income)
    else:
        return unmarriedTax(income)




print("Ursala owes ", tax(Ursala_income, Ursala_married))
print("Kaiser owes ", tax(Kaiser_income, Kaiser_married))
print("Shilah owes ", tax(Shilah_income, Shilah_married))


