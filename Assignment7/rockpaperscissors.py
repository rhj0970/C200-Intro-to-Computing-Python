import random as rn

def get_best_move(rules, history):

    print(history)
    value =0
    best_move = ""
    for i in rules:
        if history[i[1]] > value:
            value = history[i[1]]
            best_move = i[0]
    return best_move

def RPS(n):

#INITIALIZATION

    rules = [["r","s"],["p","r"],["s","p"]]
    wins = 0
    ties = 0
    losses = 0
    moves = ["r", "s", "p"]
    cnt = 0
    
# Keep track of human's play
    history = {"r":0, "p":0, "s":0} 

    while cnt < n:
        x = input("play: ")
        m = moves[rn.randint(0,2)]
        history[x] += 1
        m = get_best_move(rules, history)
        if x == m:
            ties =+ 1
            print("tie")
        elif [x,m] in rules:
            print("human wins {0} beats {1}".format(x,m))
            wins += 1
        else:
            losses += 1
            print("robot wins {0} beats {1}".format(m,x))
        cnt += 1

    print("human wins : {0}".format(wins))
    print("robot wins : {0}".format(losses))
    print("ties:  {0}".format(ties))

# GAME
t = int(input("How many games: "))
RPS(t)

