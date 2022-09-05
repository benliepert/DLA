from __future__ import division, print_function
import vpython as vp
from vpython import *

import random
import math
import copy
import numpy

## global variables, should be odd numbers

Xlength = 71
Yheight = 71
Zwidth = 71
EMPTY = 0
FILLED = 1

def randomMovement(position):

    (X, Y, Z) = position

    ## cases include: 8 corners, 6 sides, 12 edges + everywhere else

############CORNERS################################################

    if X == 0 and Y == 0 and Z ==0: # back top left corner
        ran = random.randrange(1, 8)
        if ran == 1:
            newPos = (X, Y+1, Z)
        elif ran == 2:
            newPos = (X, Y, Z+1)
        elif ran == 3:
            newPos = (X, Y+1, Z+1)
            
        elif ran == 4:
            newPos = (X+1, Y, Z)
        elif ran == 5:
            newPos = (X+1, Y+1, Z)
        elif ran == 6:
            newPos = (X+1, Y, Z+1)
        elif ran == 7:
            newPos = (X+1, Y+1, Z+1)

    elif X == 0 and Y == Yheight - 1 and Z == 0: #back top right corner
        ran = random.randrange(1, 8)
        if ran == 1:
            newPos = (X, Y-1, Z)
        elif ran == 2:
            newPos = (X, Y-1, Z+1)
        elif ran == 3:
            newPos = (X, Y, Z+1)
            
        elif ran == 4:
            newPos = (X+1, Y-1, Z)
        elif ran == 5:
            newPos = (X+1, Y, Z)
        elif ran == 6:
            newPos = (X+1, Y-1, Z+1)
        elif ran == 7:
            newPos = (X+1, Y, Z+1)

    elif X == Xlength - 1 and Y == 0 and Z == 0: # back bottom left corner
        ran = random.randrange(1, 8)
        if ran == 1:
            newPos = (X, Y, Z+1)
        elif ran == 2:
            newPos = (X, Y+1, Z+1)
        elif ran == 3:
            newPos = (X, Y+1, Z)
            
        elif ran == 4:
            newPos = (X-1, Y, Z+1)
        elif ran == 5:
            newPos = (X-1, Y+1, Z+1)
        elif ran == 6:
            newPos = (X-1, Y, Z)
        elif ran == 7:
            newPos = (X-1, Y+1, Z)

    elif X == Xlength -1 and Y == Yheight - 1 and Z == 0:
        # back bottom right corner
        ran = random.randrange(1, 8)
        if ran == 1:
            newPos = (X, Y-1, Z+1)
        elif ran == 2:
            newPos = (X, Y, Z+1)
        elif ran == 3:
            newPos = (X, Y-1, Z)
            
        elif ran == 4:
            newPos = (X-1, Y-1, Z+1)
        elif ran == 5:
            newPos = (X-1, Y, Z+1)
        elif ran == 6:
            newPos = (X-1, Y-1, Z)
        elif ran == 7:
            newPos = (X-1, Y, Z)

    elif X == 0 and Y == 0 and Z == Zwidth - 1:
        # front top left corner
        ran = random.randrange(1, 8)
        if ran == 1:
            newPos = (X, Y, Z-1)
        elif ran == 2:
            newPos = (X, Y+1, Z-1)
        elif ran == 3:
            newPos = (X, Y+1, Z)
            
        elif ran == 4:
            newPos = (X+1, Y, Z-1)
        elif ran == 5:
            newPos = (X+1, Y+1, Z-1)
        elif ran == 6:
            newPos = (X+1, Y, Z)
        elif ran == 7:
            newPos = (X+1, Y+1, Z)

    elif X == 0 and Y == Yheight - 1 and Z == Zwidth - 1:
        # front top right corner
        ran = random.randrange(1, 8)
        if ran == 1:
            newPos = (X, Y-1, Z-1)
        elif ran == 2:
            newPos = (X, Y, Z-1)
        elif ran == 3:
            newPos = (X, Y-1, Z)
            
        elif ran == 4:
            newPos = (X+1, Y-1, Z-1)
        elif ran == 5:
            newPos = (X+1, Y, Z-1)
        elif ran == 6:
            newPos = (X+1, Y-1, Z)
        elif ran == 7:
            newPos = (X+1, Y, Z)

    elif X == Xlength - 1 and Y == 0 and Z == Zwidth - 1:
        # front bottom left corner
        ran = random.randrange(1, 8)
        if ran == 1:
            newPos = (X, Y+1, Z)
        elif ran == 2:
            newPos = (X, Y, Z-1)
        elif ran == 3:
            newPos = (X, Y+1, Z-1)
            
        elif ran == 4:
            newPos = (X-1, Y, Z)
        elif ran == 5:
            newPos = (X-1, Y+1, Z)
        elif ran == 6:
            newPos = (X-1, Y, Z-1)
        elif ran == 7:
            newPos = (X-1, Y+1, Z-1)

    elif X == Xlength -1 and Y == Yheight - 1 and Z == Zwidth - 1:
        # front bottom right corner
        ran = random.randrange(1, 8)
        if ran == 1:
            newPos = (X, Y-1, Z)
        elif ran == 2:
            newPos = (X, Y-1, Z-1)
        elif ran == 3:
            newPos = (X, Y, Z-1)
            
        elif ran == 4:
            newPos = (X-1, Y-1, Z)
        elif ran == 5:
            newPos = (X-1, Y, Z)
        elif ran == 6:
            newPos = (X-1, Y-1, Z-1)
        elif ran == 7:
            newPos = (X-1, Y, Z-1)


##############EDGES######################

    elif X == 0 and Y == 0: #top left edge
        ran = random.randrange(1,12)
        if ran == 1:
            newPos = (X, Y, Z-1)
        elif ran == 2:
            newPos = (X, Y+1, Z-1)
        elif ran == 3:
            newPos = (X, Y+1, Z)
        elif ran == 4:
            newPos = (X, Y, Z+1)
        elif ran == 5:
            newPos = (X, Y+1, Z+1)
            
        elif ran == 6:
            newPos = (X+1, Y, Z-1)
        elif ran == 7:
            newPos = (X+1, Y+1, Z-1)
        elif ran == 8:
            newPos = (X+1, Y, Z)
        elif ran == 9:
            newPos = (X+1, Y+1, Z)
        elif ran == 10:
            newPos = (X+1, Y, Z+1)
        elif ran == 11:
            newPos = (X+1, Y+1, Z+1)
            
    elif X == 0 and Y == Yheight -1 : #top right edge
        ran = random.randrange(1,12)
        if ran == 1:
            newPos = (X, Y-1, Z-1)
        elif ran == 2:
            newPos = (X, Y, Z-1)
        elif ran == 3:
            newPos = (X, Y-1, Z)
        elif ran == 4:
            newPos = (X, Y-1, Z+1)
        elif ran == 5:
            newPos = (X, Y, Z+1)
            
        elif ran == 6:
            newPos = (X+1, Y-1, Z-1)
        elif ran == 7:
            newPos = (X+1, Y, Z-1)
        elif ran == 8:
            newPos = (X+1, Y-1, Z)
        elif ran == 9:
            newPos = (X+1, Y, Z)
        elif ran == 10:
            newPos = (X+1, Y-1, Z+1)
        elif ran == 11:
            newPos = (X+1, Y, Z+1)
            
    elif Z == Zwidth - 1 and X == Xlength -1: #top front edge
        ran = random.randrange(1,12)
        if ran == 1:
            newPos = (X, Y-1, Z-1)
        elif ran == 2:
            newPos = (X, Y, Z-1)
        elif ran == 3:
            newPos = (X, Y+1, Z-1)
        elif ran == 4:
            newPos = (X, Y-1, Z)
        elif ran == 5:
            newPos = (X, Y+1, Z)
            
        elif ran == 6:
            newPos = (X+1, Y-1, Z-1)
        elif ran == 7:
            newPos = (X+1, Y, Z-1)
        elif ran == 8:
            newPos = (X+1, Y+1, Z-1)
        elif ran == 9:
            newPos = (X+1, Y-1, Z)
        elif ran == 10:
            newPos = (X+1, Y, Z)
        elif ran == 11:
            newPos = (X+1, Y+1, Z)
            
    elif Z == 0 and X == 0: #top back edge
        ran = random.randrange(1,12)
        if ran == 1:
            newPos = (X, Y-1, Z)
        elif ran == 2:
            newPos = (X, Y+1, Z)
        elif ran == 3:
            newPos = (X, Y-1, Z+1)
        elif ran == 4:
            newPos = (X, Y, Z+1)
        elif ran == 5:
            newPos = (X, Y+1, Z+1)
            
        elif ran == 6:
            newPos = (X+1, Y-1, Z)
        elif ran == 7:
            newPos = (X+1, Y, Z)
        elif ran == 8:
            newPos = (X+1, Y+1, Z)
        elif ran == 9:
            newPos = (X+1, Y-1, Z+1)
        elif ran == 10:
            newPos = (X+1, Y, Z+1)
        elif ran == 11:
            newPos = (X+1, Y+1, Z+1)
            
    elif X == Xlength -1 and Y == Yheight -1: #bottom right edge
        ran = random.randrange(1,12)
        if ran == 1:
            newPos = (X, Y-1, Z+1)
        elif ran == 2:
            newPos = (X, Y, Z+1)
        elif ran == 3:
            newPos = (X, Y-1, Z)
        elif ran == 4:
            newPos = (X, Y-1, Z-1)
        elif ran == 5:
            newPos = (X, Y, Z-1)
            
        elif ran == 6:
            newPos = (X-1, Y-1, Z+1)
        elif ran == 7:
            newPos = (X-1, Y, Z+1)
        elif ran == 8:
            newPos = (X-1, Y-1, Z)
        elif ran == 9:
            newPos = (X-1, Y, Z)
        elif ran == 10:
            newPos = (X-1, Y-1, Z-1)
        elif ran == 11:
            newPos = (X-1, Y, Z-1)
            
    elif X == Xlength -1 and Y == 0: #bottom left edge
        ran = random.randrange(1,12)
        if ran == 1:
            newPos = (X, Y, Z+1)
        elif ran == 2:
            newPos = (X, Y+1, Z+1)
        elif ran == 3:
            newPos = (X, Y+1, Z)
        elif ran == 4:
            newPos = (X, Y, Z-1)
        elif ran == 5:
            newPos = (X, Y+1, Z-1)
            
        elif ran == 6:
            newPos = (X-1, Y, Z+1)
        elif ran == 7:
            newPos = (X-1, Y+1, Z+1)
        elif ran == 8:
            newPos = (X-1, Y, Z)
        elif ran == 9:
            newPos = (X-1, Y+1, Z)
        elif ran == 10:
            newPos = (X-1, Y, Z-1)
        elif ran == 11:
            newPos = (X-1, Y+1, Z-1)
            
    elif X == Xlength -1 and Z == Zwidth -1: #bottom front edge
        ran = random.randrange(1,12)
        if ran == 1:
            newPos = (X, Y-1, Z)
        elif ran == 2:
            newPos = (X, Y+1, Z)
        elif ran == 3:
            newPos = (X, Y-1, Z-1)
        elif ran == 4:
            newPos = (X, Y, Z-1)
        elif ran == 5:
            newPos = (X, Y+1, Z-1)
            
        elif ran == 6:
            newPos = (X-1, Y-1, Z)
        elif ran == 7:
            newPos = (X-1, Y, Z)
        elif ran == 8:
            newPos = (X-1, Y+1, Z)
        elif ran == 9:
            newPos = (X-1, Y-1, Z-1)
        elif ran == 10:
            newPos = (X-1, Y, Z-1)
        elif ran == 11:
            newPos = (X-1, Y+1, Z-1)
            
    elif X == Xlength - 1 and Z == 0: #bottom back edge
        ran = random.randrange(1,12)
        if ran == 1:
            newPos = (X, Y-1, Z+1)
        elif ran == 2:
            newPos = (X, Y, Z+1)
        elif ran == 3:
            newPos = (X, Y+1, Z+1)
        elif ran == 4:
            newPos = (X, Y-1, Z)
        elif ran == 5:
            newPos = (X, Y+1, Z)
            
        elif ran == 6:
            newPos = (X-1, Y-1, Z+1)
        elif ran == 7:
            newPos = (X-1, Y, Z+1)
        elif ran == 8:
            newPos = (X-1, Y+1, Z+1)
        elif ran == 9:
            newPos = (X-1, Y-1, Z)
        elif ran == 10:
            newPos = (X-1, Y, Z)
        elif ran == 11:
            newPos = (X-1, Y+1, Z)
            
    elif Z == Zwidth -1 and Y == 0: #front left edge
        ran = random.randrange(1,12)
        if ran == 1:
            newPos = (X-1, Y, Z)
        elif ran == 2:
            newPos = (X-1, Y+1, Z)
        elif ran == 3:
            newPos = (X, Y+1, Z)
        elif ran == 4:
            newPos = (X+1, Y, Z)
        elif ran == 5:
            newPos = (X+1, Y+1, Z)
            
        elif ran == 6:
            newPos = (X-1, Y, Z-1)
        elif ran == 7:
            newPos = (X-1, Y+1, Z-1)
        elif ran == 8:
            newPos = (X, Y, Z-1)
        elif ran == 9:
            newPos = (X, Y+1, Z-1)
        elif ran == 10:
            newPos = (X+1, Y, Z-1)
        elif ran == 11:
            newPos = (X+1, Y+1, Z-1)
            
    elif Y == Yheight and Z == Zwidth -1: #front right edge
        ran = random.randrange(1,12)
        if ran == 1:
            newPos = (X-1, Y-1, Z)
        elif ran == 2:
            newPos = (X-1, Y, Z)
        elif ran == 3:
            newPos = (X, Y-1, Z)
        elif ran == 4:
            newPos = (X+1, Y-1, Z)
        elif ran == 5:
            newPos = (X+1, Y, Z)
            
        elif ran == 6:
            newPos = (X-1, Y-1, Z-1)
        elif ran == 7:
            newPos = (X-1, Y, Z-1)
        elif ran == 8:
            newPos = (X, Y-1, Z-1)
        elif ran == 9:
            newPos = (X, Y, Z-1)
        elif ran == 10:
            newPos = (X+1, Y-1, Z-1)
        elif ran == 11:
            newPos = (X+1, Y, Z-1)
            
    elif Y == 0 and Z == 0: #back left edge
        ran = random.randrange(1,12)
        if ran == 1:
            newPos = (X-1, Y+1, Z)
        elif ran == 2:
            newPos = (X-1, Y, Z)
        elif ran == 3:
            newPos = (X, Y+1, Z)
        elif ran == 4:
            newPos = (X+1, Y+1, Z)
        elif ran == 5:
            newPos = (X+1, Y, Z)
            
        elif ran == 6:
            newPos = (X-1, Y+1, Z+1)
        elif ran == 7:
            newPos = (X-1, Y, Z+1)
        elif ran == 8:
            newPos = (X, Y+1, Z+1)
        elif ran == 9:
            newPos = (X, Y, Z+1)
        elif ran == 10:
            newPos = (X+1, Y+1, Z+1)
        elif ran == 11:
            newPos = (X+1, Y, Z+1)
            
    elif Z == 0 and Y == Yheight: #back right edge
        ran = random.randrange(1,12)
        if ran == 1:
            newPos = (X-1, Y, Z)
        elif ran == 2:
            newPos = (X-1, Y-1, Z)
        elif ran == 3:
            newPos = (X, Y-1, Z)
        elif ran == 4:
            newPos = (X+1, Y, Z)
        elif ran == 5:
            newPos = (X+1, Y-1, Z)
            
        elif ran == 6:
            newPos = (X-1, Y, Z+1)
        elif ran == 7:
            newPos = (X-1, Y-1, Z+1)
        elif ran == 8:
            newPos = (X, Y, Z+1)
        elif ran == 9:
            newPos = (X, Y-1, Z+1)
        elif ran == 10:
            newPos = (X+1, Y, Z+1)
        elif ran == 11:
            newPos = (X+1, Y-1, Z+1)
    
############SIDES##########################    

    elif Z == 0: # back side
        ran = random.randrange(1,18)
        if ran == 1:
            newPos = (X-1, Y-1, Z)
        elif ran == 2:
            newPos = (X-1, Y, Z)
        elif ran == 3:
            newPos = (X-1, Y+1, Z)
        elif ran == 4:
            newPos = (X, Y-1, Z)
        elif ran == 5:
            newPos = (X, Y+1, Z)
        elif ran == 6:
            newPos = (X+1, Y-1, Z)
        elif ran == 7:
            newPos = (X+1, Y, Z)
        elif ran == 8:
            newPos = (X+1, Y+1, Z)
            
        elif ran == 9:
            newPos = (X-1, Y-1, Z+1)
        elif ran == 10:
            newPos = (X-1, Y, Z+1)
        elif ran == 11:
            newPos = (X-1, Y+1, Z+1)
        elif ran == 12:
            newPos = (X, Y-1, Z+1)
        elif ran == 13:
            newPos = (X, Y, Z+1)
        elif ran == 14:
            newPos = (X, Y+1, Z+1)
        elif ran == 15:
            newPos = (X+1, Y-1, Z+1)
        elif ran == 16:
            newPos = (X+1, Y, Z+1)
        elif ran == 17:
            newPos = (X+1, Y+1, Z+1)
        
    elif Z == Zwidth - 1: # front side
        ran = random.randrange(1,18)
        if ran == 1:
            newPos = (X-1, Y-1, Z)
        elif ran == 2:
            newPos = (X-1, Y, Z)
        elif ran == 3:
            newPos = (X-1, Y+1, Z)
        elif ran == 4:
            newPos = (X, Y-1, Z)
        elif ran == 5:
            newPos = (X, Y+1, Z)
        elif ran == 6:
            newPos = (X+1, Y-1, Z)
        elif ran == 7:
            newPos = (X+1, Y, Z)
        elif ran == 8:
            newPos = (X+1, Y+1, Z)
            
        elif ran == 9:
            newPos = (X-1, Y-1, Z-1)
        elif ran == 10:
            newPos = (X-1, Y, Z-1)
        elif ran == 11:
            newPos = (X-1, Y+1, Z-1)
        elif ran == 12:
            newPos = (X, Y-1, Z-1)
        elif ran == 13:
            newPos = (X, Y, Z-1)
        elif ran == 14:
            newPos = (X, Y+1, Z-1)
        elif ran == 15:
            newPos = (X+1, Y-1, Z-1)
        elif ran == 16:
            newPos = (X+1, Y, Z-1)
        elif ran == 17:
            newPos = (X+1, Y+1, Z-1)
            
    elif X == 0: #top side
        ran = random.randrange(1,18)
        if ran == 1:
            newPos = (X, Y-1, Z-1)
        elif ran == 2:
            newPos = (X, Y, Z-1)
        elif ran == 3:
            newPos = (X, Y+1, Z-1)
        elif ran == 4:
            newPos = (X, Y-1, Z)
        elif ran == 5:
            newPos = (X, Y+1, Z)
        elif ran == 6:
            newPos = (X, Y-1, Z+1)
        elif ran == 7:
            newPos = (X, Y, Z+1)
        elif ran == 8:
            newPos = (X, Y+1, Z+1)
            
        elif ran == 9:
            newPos = (X+1, Y-1, Z-1)
        elif ran == 10:
            newPos = (X+1, Y, Z-1)
        elif ran == 11:
            newPos = (X+1, Y+1, Z-1)
        elif ran == 12:
            newPos = (X+1, Y-1, Z)
        elif ran == 13:
            newPos = (X+1, Y, Z)
        elif ran == 14:
            newPos = (X+1, Y+1, Z)
        elif ran == 15:
            newPos = (X+1, Y-1, Z+1)
        elif ran == 16:
            newPos = (X+1, Y, Z+1)
        elif ran == 17:
            newPos = (X+1, Y+1, Z+1)
            
    elif X == Xlength - 1: # bottom side
        ran = random.randrange(1,18)
        if ran == 1:
            newPos = (X, Y-1, Z+1)
        elif ran == 2:
            newPos = (X, Y, Z+1)
        elif ran == 3:
            newPos = (X, Y+1, Z+1)
        elif ran == 4:
            newPos = (X, Y-1, Z)
        elif ran == 5:
            newPos = (X, Y+1, Z)
        elif ran == 6:
            newPos = (X, Y-1, Z-1)
        elif ran == 7:
            newPos = (X, Y, Z-1)
        elif ran == 8:
            newPos = (X, Y+1, Z-1)
            
        elif ran == 9:
            newPos = (X-1, Y-1, Z+1)
        elif ran == 10:
            newPos = (X-1, Y, Z+1)
        elif ran == 11:
            newPos = (X-1, Y+1, Z+1)
        elif ran == 12:
            newPos = (X-1, Y-1, Z)
        elif ran == 13:
            newPos = (X-1, Y, Z)
        elif ran == 14:
            newPos = (X-1, Y+1, Z)
        elif ran == 15:
            newPos = (X-1, Y-1, Z-1)
        elif ran == 16:
            newPos = (X-1, Y, Z-1)
        elif ran == 17:
            newPos = (X-1, Y+1, Z-1)
            
    elif Y == 0: #left side
        ran = random.randrange(1,18)
        if ran == 1:
            newPos = (X-1, Y, Z+1)
        elif ran == 2:
            newPos = (X-1, Y, Z)
        elif ran == 3:
            newPos = (X-1, Y, Z-1)
        elif ran == 4:
            newPos = (X, Y, Z+1)
        elif ran == 5:
            newPos = (X, Y, Z-1)
        elif ran == 6:
            newPos = (X+1, Y, Z+1)
        elif ran == 7:
            newPos = (X+1, Y, Z)
        elif ran == 8:
            newPos = (X+1, Y, Z-1)
            
        elif ran == 9:
            newPos = (X-1, Y+1, Z+1)
        elif ran == 10:
            newPos = (X-1, Y+1, Z)
        elif ran == 11:
            newPos = (X-1, Y+1, Z-1)
        elif ran == 12:
            newPos = (X, Y+1, Z+1)
        elif ran == 13:
            newPos = (X, Y+1, Z)
        elif ran == 14:
            newPos = (X, Y+1, Z-1)
        elif ran == 15:
            newPos = (X+1, Y+1, Z+1)
        elif ran == 16:
            newPos = (X+1, Y+1, Z)
        elif ran == 17:
            newPos = (X+1, Y+1, Z-1)
            
    elif Y == Yheight - 1: # right side
        ran = random.randrange(1,18)
        if ran == 1:
            newPos = (X-1, Y, Z-1)
        elif ran == 2:
            newPos = (X-1, Y, Z)
        elif ran == 3:
            newPos = (X-1, Y, Z+1)
        elif ran == 4:
            newPos = (X, Y, Z-1)
        elif ran == 5:
            newPos = (X, Y, Z+1)
        elif ran == 6:
            newPos = (X+1, Y, Z-1)
        elif ran == 7:
            newPos = (X+1, Y, Z)
        elif ran == 8:
            newPos = (X+1, Y, Z+1)
            
        elif ran == 9:
            newPos = (X-1, Y-1, Z-1)
        elif ran == 10:
            newPos = (X-1, Y-1, Z)
        elif ran == 11:
            newPos = (X-1, Y-1, Z+1)
        elif ran == 12:
            newPos = (X, Y-1, Z-1)
        elif ran == 13:
            newPos = (X, Y-1, Z)
        elif ran == 14:
            newPos = (X, Y-1, Z+1)
        elif ran == 15:
            newPos = (X+1, Y-1, Z-1)
        elif ran == 16:
            newPos = (X+1, Y-1, Z)
        elif ran == 17:
            newPos = (X+1, Y-1, Z+1)

    else: #everywhere else
        ran = random.randrange(1,27)
        if ran == 1:
            newPos = (X-1, Y-1, Z-1)
        elif ran == 2:
            newPos = (X-1, Y, Z-1)
        elif ran == 3:
            newPos = (X-1, Y+1, Z-1)
        elif ran == 4:
            newPos = (X, Y-1, Z-1)
        elif ran == 5:
            newPos = (X, Y, Z-1)
        elif ran == 6:
            newPos = (X, Y+1, Z-1)
        elif ran == 7:
            newPos = (X+1, Y-1, Z-1)
        elif ran == 8:
            newPos = (X+1, Y, Z-1)
        elif ran == 9:
            newPos = (X+1, Y+1, Z-1)
            
        elif ran == 10:
            newPos = (X-1, Y-1, Z)
        elif ran == 11:
            newPos = (X-1, Y, Z)
        elif ran == 12:
            newPos = (X-1, Y+1, Z)
        elif ran == 13:
            newPos = (X, Y-1, Z)
        elif ran == 14:
            newPos = (X, Y+1, Z)
        elif ran == 15:
            newPos = (X+1, Y-1, Z)
        elif ran == 16:
            newPos = (X+1, Y, Z)
        elif ran == 17:
            newPos = (X+1, Y+1, Z)
            
        elif ran == 18:
            newPos = (X-1, Y-1, Z+1)
        elif ran == 19:
            newPos = (X-1, Y, Z+1)
        elif ran == 20:
            newPos = (X-1, Y+1, Z+1)
        elif ran == 21:
            newPos = (X, Y-1, Z+1)
        elif ran == 22:
            newPos = (X, Y, Z+1)
        elif ran == 23:
            newPos = (X, Y+1, Z+1)
        elif ran == 24:
            newPos = (X+1, Y-1, Z+1)
        elif ran == 25:
            newPos = (X+1, Y, Z+1)
        elif ran == 26:
            newPos = (X+1, Y+1, Z+1)

    return newPos

def drawSphere(positon):
    ## position is an (x, y, z) coordinate

    vp.sphere(pos = position, radius = 1, color = vp.color.blue)
    
def emptySpace(Xlength, Yheight, Zwidth):

    space = [[[EMPTY for row in range(Xlength)]for col in range(Yheight)\
             ]for Z in range(Zwidth)]
    
    X = int(Xlength/2)
    Y = int(Yheight/2)
    Z = int(Zwidth/2)
    
    for x in range(len(space)):
        for y in range(len(space[x])):
            for z in range(len(space[x][y])):
                if (X,Y,Z) == (x,y,z):
                    space[x][y][z] = FILLED
                
            
    return space

def initialize(space):
    emptyList = []
    
    X = int(Xlength/2)
    Y = int(Yheight/2)
    Z = int(Zwidth/2)

    sphere = vp.sphere(pos = (X,Y,Z), radius = 1, color = vp.color.blue)
   
    
    for x in range(len(space)):
        for y in range(len(space[x])):
            for z in range(len(space[x][y])):
                if (x,y,z) != (X,Y,Z):
                    emptyList.append((x,y,z))
                    

    return emptyList

def neighborhood(space, position):
    offsets = [(-1, -1, -1), (-1, 0, -1), (-1, 1, -1),
               (0, -1, -1), (0, 0, -1), (0, 1, -1),
               (1, -1, -1), (1, 0, -1), (1, 1, -1),

               (-1, -1, 0), (-1, 0, 0), (-1, 1, 0),
               (0, -1, 0),            (0, 1, 0),
               (1, -1, 0), (1, 0, 0), (1, 1, 0),

                (-1, -1, 1), (-1, 0, 1), (-1, 1, 1),
               (0, -1, 1), (0, 0, 1),  (0, 1, 1),
               (1, -1, 1), (1, 0, 1), (1, 1, 1)]

    (X, Y, Z) = position # where X is rows, Y is cols, Z is z dimension
    count = 0
    
    for offset in offsets:
        
        x = X + offset[0]
        y = Y + offset[1]
        z = Z + offset[2]

        if (x >= 0 and x < Xlength) and (y >= 0 and y < Yheight) and (z >= 0 and z < Zwidth):
            if space[x][y][z] == FILLED:
                count = count + 1

    return count

def distance(position):
    x = int(Xlength/2)
    y = int(Yheight/2)
    z = int(Zwidth/2)

    (X, Y, Z) = position

    difX = (X - x)**2
    difY = (Y - y)**2
    difZ = (Z - z)**2

    dist = math.sqrt(difX + difY + difZ)

    return dist

def rPlusOne(emptyList, radius):
    newEList = []

    for item in emptyList:
        if distance(item) == (radius + 1):
            newEList.append(item)

    return newEList

def DLA(Xlength, Yheight, Zwidth, moveLimit, radius, particles):
    '''
    Purpose:
    Author:
    Parameters:
        Xlength: the x dimension of the 3d space
        Yheight: the y dimension of the 3d space
        Zwidth: the z dimension of the 3d space
        moveLimit: the maximum number of times a particle will move, remaining
            unstuck, before it is abandoned
        radius: stores the maximum distance from the origin, starts at 0
        particles: the number of particles that will stick before the simulation
            is complete
    Return Value: the final 3D list 'space'

    '''
    space = emptySpace(Xlength, Yheight, Zwidth)
    emptyList = initialize(space)
    numParts = particles
        
    while numParts > 0:
        newEList = rPlusOne(emptyList, radius)
        newSpace = copy.deepcopy(space)
        ELIST = copy.deepcopy(emptyList)
        (startX, startY, startZ) = random.choice(newEList)
        newSpace[startX][startY][startZ] = FILLED
        sphere = vp.sphere(pos = (startX,startY,startZ), radius = 1, color = vp.color.blue)

        XC = startX
        YC = startY
        ZC = startZ
        stuck = False

        counter = 0

        while (not stuck) and (counter < moveLimit):
            vp.rate()
            (newX, newY, newZ) = randomMovement((XC, YC, ZC))
            newSpace[XC][YC][ZC] = EMPTY
            newSpace[newX][newY][newZ] = FILLED
            sphere.pos = (newX, newY, newZ)
            count = neighborhood(newSpace, (newX,newY,newZ))

            if count > 0:
                stuck = True

                if (newX,newY,newZ) not in ELIST:
                    print('broken')
                    break
                else:
                    ELIST.remove((newX, newY, newZ))
                    ELIST.append((XC, YC, ZC))

                    if distance((newX, newY, newZ)) > radius:
                        radius = radius + 1

                    numParts = numParts - 1

            XC = newX
            YC = newY
            ZC = newZ

            space = newSpace
            counter = counter + 1
            emptyList = ELIST
            

        if not stuck:
            space[XC][YC][ZC] = EMPTY
            emptyList.append((XC, YC, ZC))
            sphere.visible = False
    
    return space

             
def main():
    DLA(Xlength, Yheight, Zwidth, 200, 0, 5)
    
main()


