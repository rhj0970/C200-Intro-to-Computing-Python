#CODE Assigment 11

import pygame, sys
import math
from pygame.locals import *
import random as rn
pygame.init()

BLUE = (0,0,255)
WHITE = (255,255,255)

DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)

pygame.display.set_caption('S-Triangle')

#INPUT takes a location loc = (x,y) pair of points and width
#RETURN 3 points of the equilateral triangle determined by loc and width
def triangle(loc,width):
    z = math.sqrt(width**2 -((width/2)**2))
    top= (loc[0]+width/2, loc[1])
    right= (loc[0]+width, loc[1]+z)
    left= (loc[0], loc[1]+z)
    return top, left, right
#TO DO: Implement function

DISPLAYSURF.fill(WHITE)

#Draws Triangle
#(triangle(loc,w)) is a tuple of tuples...)
def draw_triangle(loc, w):
    newcolor = (rn.randint(0,255),rn.randint(0,255),rn.randint(0,255))
    pygame.draw.polygon(DISPLAYSURF, newcolor , (triangle(loc,w)),1)

#INPUT location and width
#RETURN nothing -- follows algorithm
def s(loc,width):
    draw_triangle(loc,width)
    if width >1:       
        s(triangle(loc,width/2)[0], width/2)
        s(triangle(loc,width/2)[1], width/2)
        s(triangle(loc,width/2)[2], width/2)
    else:
        return None
#TO DO: Implement Function

s((0,0),440)

while True:
    for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

