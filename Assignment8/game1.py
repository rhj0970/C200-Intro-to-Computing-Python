import pygame
import sys
import numpy as np
import random as rn

pygame.init()
 
BLACK = ( 0,0,0)
WHITE = (255,255,255)
BLUE =  (0,0,255)
DARKGREEN = (0,100,0)
RED =   (255,0,0)
YELLOW = (255,255,0)

class Rectangle:

    def __init__(self,color,loc):
        self.loc = loc
        self.color = color

    def my_draw(self,screen):
        pygame.draw.rect(screen, self.color, self.loc)
    
    def my_move(self,xoffset,yoffset):
        self.loc = [self.loc[0]+xoffset,self.loc[1]+yoffset] + self.loc[2:]

    def set_color(self, new_color):
        self.color = new_color
        

  
        
size = [300, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("C200 CHANGE")


r = Rectangle(RED, [0, 0, 20, 20])

while True:
    
    pygame.time.wait(40)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
 
    screen.fill(WHITE)
 
    r.my_draw(screen)
    
    if r.loc[0] > 280:
        xd = -rn.randint(1, 3)
        r.set_color(DARKGREEN)
    if r.loc[1] > 280:
        yd = -rn.randint(1, 3)
        r.set_color(BLUE)
    if r.loc[0] < 10:
        xd = rn.randint(1, 3)
        r.set_color(RED)
    if r.loc[1] < 10:
        yd = rn.randint(1, 3)
        r.set_color(YELLOW)

    r.my_move(xd,yd)

    pygame.display.flip()



