
def meaning (aaa):
    if aaa == "none of the emojis are found":
        return 0
    
    if aaa == ":)":
        return 1
    elif aaa == "-_-":
        return 2
    elif aaa == ":(":
        return 3
    elif aaa == ":0":
        return 4
    elif aaa == ":p":
        return 5

print(meaning(":),-_-"))


def competitionBracket(age, desiredBracket):

    if (age < 30):
        print("Adult Bracket")
    elif (age > 30 and age <= 35 or (age>35 and desiredBracket== "M1")):
        print("Master 1 Bracket")
    elif (age > 35 and age <= 40) or (age>40 and desiredBracket== "M2"):
        print("Master 2 Bracket")
    elif (age > 40 and age < 45) or (age>45 and desiredBracket == "M3"):
        print("Master 3 Bracket")
    elif (age > 30 and (desiredBracket =="adult")):
        print("Adult Bracket")
    elif (age >=45):
        print("Master 4 Bracket")

competitionBracket(34, "M1")