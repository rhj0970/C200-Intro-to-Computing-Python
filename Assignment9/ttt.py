import numpy as np
import random as rn

class TTT:
    def __init__(self):
       self.b = np.array([1,2,3,4,5,6,7,8,9])
       self.moves = [1,2,3,4,5,6,7,8,9]
       self.game = []

    def pt(self, x):
       if (x == 0):
           return "x"
       elif (x == -1):
           return "o"
       else:
           return str(x)

    def win(self, player):
        if self.b[0] == self.b[1] and self.b[1] == self.b[2] and self.b[0] == self.b[2]:
            return player + "you won!!!!!!!!!!!!!!"
        elif self.b[3] == self.b[4] and self.b[4] == self.b[5] and self.b[3] == self.b[5]:
            return player + "you won!!!!!!!!!!!!!!"
        elif self.b[6] == self.b[7] and self.b[7] == self.b[8] and self.b[6] == self.b[8]:
            return player + "you won!!!!!!!!!!!!!!"
        elif self.b[0] == self.b[3] and self.b[3] == self.b[6] and self.b[0] == self.b[6]:
            return player + "you won!!!!!!!!!!!!!!"
        elif self.b[2] == self.b[4] and self.b[4] == self.b[6] and self.b[2] == self.b[6]:
            return player + "you won!!!!!!!!!!!!!!"
        elif self.b[1] == self.b[4] and self.b[4] == self.b[7] and self.b[1] == self.b[7]:
            return player + "you won!!!!!!!!!!!!!!"
        elif self.b[2] == self.b[5] and self.b[5] == self.b[8] and self.b[1] == self.b[8]:
            return player + "you won!!!!!!!!!!!!!!"
        elif self.b[0] == self.b[4] and self.b[4] == self.b[8] and self.b[0] == self.b[8]:
            return player + "you won!!!!!!!!!!!!!!"
        else:
            return False
            
           

       #TO DO: Implement Function

    def board(self):
        print()
        for i in range(0,3):
            print("{0:^3}|{1:^3}|{2:^3}".format(self.pt(self.b[i+i*2]), self.pt(self.b[i+1+i*2]),self.pt(self.b[i+2+i*2])))
            if i < 2:
                print("=== === ===")


    def play(self, value='x'):
      
        
        if value == "x":
            self.board()
            computer = "o"
        else:
            computer = "x"
        player = 'x'
        while self.moves or self.win(player):
            if value == "x":
                move = int(input("input moves: "))
                
                self.moves.remove(move)
                self.b[move-1] = 0
                self.board()

                if (self.moves):
                    m = rn.choice(self.moves)
                    self.moves.remove(m)
                    self.b[m-1] = -1
                    self.board()
                    
                    self.win('x')

            else:
                m = rn.choice(self.moves)
                self.moves.remove(m)
                self.b[m-1] = 0
                self.board()
                if (self.moves):
                    move = int(input("input moves: "))
                
                    self.moves.remove(move)
                    self.b[move-1] = -1
                    self.board()
                    self.win('x')
            print(self.moves)

        winner = win(player)
        if winner:
            print ("{} wins!".format(winner))
        else:
            print ("tie!")
             


x = TTT()
x.play('o')


