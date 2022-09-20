#!/bin/python3
import turtle ## for drawing
import random ## for random walk
import math ## distance formula (square root)
import copy ##copying lists so they won't be bound together
import time
import sys
import argparse

EMPTY = 0
FILLED = 1

## currently all circle related functions draw squares instead
def drawGrid(rows, columns, tortoise):
    """Draws an empty grid using turtle graphics.
    Parameters: 
        rows: the number of rows in the grid
        columns: the number of columns in the grid
        tortoise: a Turtle object
    Return value: None
    """
    
    tortoise.pencolor('lightblue')
    
    for row in range(rows + 1):
        tortoise.up()
        tortoise.goto(0, row)
        tortoise.down()
        tortoise.goto(columns, row)
    for column in range(columns + 1):
        tortoise.up()
        tortoise.goto(column, 0)
        tortoise.down()
        tortoise.goto(column, rows)

def emptyGrid(rows, columns):
    """Create a rows x columns grid of zeros.
    Parameters:
        rows: the number of rows in the grid
        columns: the number of columns in the grid
    Return value: a list of ROWS lists of COLUMNS zeros
    """
    grid = []
    for r in range(rows):
        row = [EMPTY] * columns
        grid.append(row)
    return grid

def createCircles(screen, colors, scale):

    square = ((0, 0), (0, scale), (scale, scale), (scale, 0))
    for color in colors:
        squareShape = turtle.Shape('compound')
        squareShape.addcomponent(square, color, 'lightblue')
        screen.register_shape(color, squareShape)

def drawCircle(pos, color, tortoise):
    
    (row, column) = pos
    screen = tortoise.getscreen()
    rows = int(screen.canvheight / screen.yscale)
    row = rows - row - 1
    tortoise.shape(color)
    tortoise.up()
    tortoise.goto(column, row + 1)
    tortoise.stamp()
    
#############################

def initialize(grid, rows, columns):
    '''
    Set the center square of the 2d array 'grid' as filled.
    Return a map containing all of the empty squares where key is a tuple
    with the coords of said square and value is True (value is arbitrary
    and not used)
    '''

    r = int(rows/2 )
    c = int(columns/2 )

    grid[r][c] = FILLED
    
    empty = {}
    
    for row in range(rows):
        for col in range(columns):
            if (row, col) != (r,c):
                empty[(row, col)] = True

    return empty


def neighborhood(grid, row, column):
    
    offsets = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1),           (0, 1),
               (1, -1), (1, 0), (1, 1)]

    count = 0

    Rows = len(grid)
    Columns = len(grid[0])
    
    for offset in offsets:
        r = row + offset[0]
        c = column + offset[1]
        if (r >= 0 and r < Rows) and (c >= 0 and c < Columns):
            if grid[r][c] == FILLED:
                count = count + 1

    return count

def randomMovement(pos, Rows, Columns):
    # for anywhere besides edges (including corners)
    # 1 is NORTH
    # 2 is NORTHEAST
    # 3 is EAST
    # 4 is SOUTHEAST
    # 5 is SOUTH
    # 6 is SOUTHWEST
    # 7 is WEST
    # 8 is NORTHWEST
    
    row, col = pos

    ## corners -- 3 options
    if row == 0 and col == 0: #top left corner
        direction = random.randrange(1,4)
        if direction == 1:
            newPos = (row, col+1)
        elif direction == 2:
            newPos = (row+1,col+1)
        elif direction == 3:
            newPos = (row+1, col)

    elif row == Rows - 1 and col == 0: #bottom left corner
        direction = random.randrange(1,4)
        if direction == 1:
            newPos = (row-1, col)
        elif direction == 2:
            newPos = (row-1, col+1)
        elif direction == 3:
            newPos = (row, col+1)

    elif row == Rows - 1 and col == Columns - 1: #bottom right corner
        direction = random.randrange(1,4)
        if direction == 1:
            newPos = (row, col-1)
        elif direction == 2:
            newPos = (row-1, col-1)
        elif direction == 3:
            newPos = (row-1, col)

    elif row == 0 and col == Columns - 1: #top right corner
        direction = random.randrange(1,4)
        if direction == 1:
            newPos = (row+1, col)
        elif direction == 2:
            newPos = (row+1, col-1)
        elif direction == 3:
            newPos = (row, col-1)

    ## edges -- 5 options
    elif col == Columns - 1: #right edge
        direction = random.randrange(1,6)
        if direction == 1:
            newPos = (row+1, col)
        elif direction == 2:
            newPos = (row+1, col-1)
        elif direction == 3:
            newPos = (row, col-1)
        elif direction == 4:
            newPos = (row-1, col-1)
        elif direction == 5:
            newPos = (row-1, col)

    elif row == Rows - 1: #bottom edge
        direction = random.randrange(1,6)
        if direction == 1:
            newPos = (row, col-1)
        elif direction == 2:
            newPos = (row-1, col-1)
        elif direction == 3:
            newPos = (row-1, col)
        elif direction == 4:
            newPos = (row-1, col+1)
        elif direction == 5:
            newPos = (row, col+1)

    elif row == 0: #top edge
        direction = random.randrange(1,6)
        if direction == 1:
            newPos = (row, col+1)
        elif direction == 2:
            newPos = (row+1, col+1)
        elif direction == 3:
            newPos = (row+1, col)
        elif direction == 4:
            newPos = (row+1, col-1)
        elif direction == 5:
            newPos = (row, col-1)

    elif col == 0: #left edge
        direction = random.randrange(1,6)
        if direction == 1:
            newPos = (row-1, col)
        elif direction == 2:
            newPos = (row-1, col+1)
        elif direction == 3:
            newPos = (row, col+1)
        elif direction == 4:
            newPos = (row+1, col+1)
        elif direction == 5:
            newPos = (row+1, col)
        
    ## anywhere else
    else: 
        direction = random.randrange(1,9)
        if direction == 1:
            newPos = (row-1, col)
        elif direction == 2:
            newPos = (row-1, col+1)
        elif direction == 3:
            newPos = (row, col+1)
        elif direction == 4:
            newPos = (row+1, col+1)
        elif direction == 5:
            newPos = (row+1, col)
        elif direction == 6:
            newPos = (row+1, col-1)
        elif direction == 7:
            newPos = (row, col-1)
        elif direction == 8:
            newPos = (row-1, col-1)

    return newPos

def distance(pos):
    r = int(Rows/2 )
    c = int(Columns/2 )

    R, C = pos
    
    difX_Sq = (R - r)**2
    difY_Sq = (C - c)**2

    dist = math.sqrt(difX_Sq + difY_Sq)
    
    return dist

def getSpawnOptions(empty, radius):
    '''
    Return a dictionary of points that are (radius + 1) from the center
    '''
    spawnOptions = {}

    for item in empty:
        if distance(item) == (radius + 1):
            spawnOptions[item] = True

    return spawnOptions

   
def DLA(grid, rows, columns, moveLimit, particles):
    empty = initialize(grid, rows, columns)

    numParts = particles
    numUnstuck = 1
    partsToIncreaseRadius = 5
    movesToStickList = [] #TODO: graph this at the end
    tempCounter = 0

    # so our logging is there right away, even if it takes a sec to see particles
    sys.stdout.write("Particles remaining = %d      \r"%(numParts))
    sys.stdout.flush()

    while numParts > 0:
        newGrid = copy.deepcopy(grid)
        ELIST = empty
        startR, startC = random.choice(list(ELIST.keys()))
        newGrid[startR][startC] = FILLED

        R = startR
        C = startC
        stuck = False

        counter = 0
  
        while not stuck and counter < moveLimit:
            newR, newC = randomMovement((R, C), rows, columns)
            # it's possible that random movement tells us to move to a squat that isn't empty
            # loop until we've got a square that is
            while (newR, newC) not in ELIST:
                newR, newC = randomMovement((R, C), rows, columns)
                tempCounter += 1

            newGrid[R][C] = EMPTY # the particle used to be at this spot
            newGrid[newR][newC] = FILLED # the particle moved to this spot

            numNeighbors = neighborhood(grid, newR, newC)
                
            if numNeighbors > 0:
                stuck = True

                del ELIST[(newR, newC)]
                ELIST[(R, C)] = True
                numParts -= 1 

                movesToStickList.append(counter)

                sys.stdout.write("Particles remaining = %d      \r"%(numParts))
                sys.stdout.flush()
                    
            R, C = newR, newC # new point becomes the current point
            grid = newGrid
            counter += 1 
            empty = ELIST

        if not stuck:
            #print("- - - Unstuck particle #%s. %s remain"%(numUnstuck, numParts))
            numUnstuck += 1
            newGrid[R][C] = EMPTY
            ELIST[(R, C)] = True

        grid = newGrid
        
    print("\n\nTempCounter = %d"%(tempCounter))
    return grid

def fillGrid(tortoise, grid):
    for r in range(len(grid)):
        row = grid[r]
        for c in range(len(row)):
            square = row[c]
            if square == FILLED:
                drawCircle((r,c), 'blue', tortoise)
            else:
                drawCircle((r,c), 'white', tortoise)

def writeToFile(grid, fileName):

    with open(fileName, 'w') as f:
        for row in grid:
            for thing in row:
                f.write(str(thing))
            f.write("\n")

    
def readFromFile(fileName):
    grid = []
    with open(fileName, 'r') as f:
        for line in f:
            row = []
            for letter in line.strip():
                row.append(int(letter))
            grid.append(row)

    return grid
    
def main():

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-p", "--particles", help="the number of particles you'd like to run the simulation with", type=int, default=500)
    parser.add_argument("-m", "--movelimit", help="a spawned particle will take up to this many moves without sticking before it dies", type=int, default=2000)
    parser.add_argument("-r", "--rows", help="the number of rows in the simulation grid", type=int, default=200)
    parser.add_argument("-c", "--columns", help="the number of columns in the simulation grid", type=int, default=200)
    parser.add_argument("-f", "--file", help="read the grid in from this file, and display it. No simulation will be run.", type=str)
    parser.add_argument("-o", "--outfile", help="if running a simulaton, grid will be serialized into this file so you can view it again later", type=str)
    parser.add_argument("-s", "--scale", help="pixel scale of each square that's drawn. You may need to adjust this depending on number of rows/columns", type=int, default=8)
    parser.add_argument("-g", "--grow", help="continue generating on top of this grid", type=str)
    args = parser.parse_args()

    # TODO: make program infer size of grid you passed in and use those dimensions

    Rows    = args.rows
    Columns = args.columns
    scale   = args.scale

    if args.file is not None:
        # user specified a file. We read the grid in from there
        grid = readFromFile(args.file)
    else:
        # run the simulation
        numParticles = args.particles
        moveLimit    = args.movelimit

        # either init with an emptygrid, or one we'd like to grow
        if args.grow is not None:
            grid = readFromFile(args.grow)
        else:
            grid = emptyGrid(rows, columns)

        print("---- Starting DLA simulation with %s particles ----"%(numParticles))
        start_time = time.time()
        grid = DLA(grid, Rows, Columns, moveLimit, numParticles)
        end_time = time.time()
        print("Simulation for: %s particles with move limit: %s took %s seconds"%(numParticles, moveLimit, int(end_time - start_time)))

        if args.outfile is not None:
            outFile = args.outfile
            print("Writing grid out to file: %s"%(outFile))
            writeToFile(grid, outFile)

    george = turtle.Turtle()
    screen = george.getscreen()
    screen.setup(Columns * scale + 20, Rows * scale + 20) # page 707
    screen.setworldcoordinates(0, 0, Columns, Rows)
    screen.tracer(100)
    george.hideturtle()
    createCircles(screen, ['blue', 'white'], scale)

    drawGrid(Rows, Columns, george)
    fillGrid(george, grid)

    screen.update()

    x = input("Press any button to quit . . .")
    
main()
                

