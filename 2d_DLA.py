import turtle ## for drawing
import random ## for random walk
import math ## distance formula (square root)
import copy ##copying lists so they won't be bound together
import time
import sys

EMPTY = 0
FILLED = 1

Rows = 200
Columns = 200


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


def initialize(grid):

    r = int(Rows/2 )
    c = int(Columns/2 )

    grid[r][c] = FILLED
    
    empty = {}
    
    for row in range(Rows):
        for col in range(Columns):
            if (row, col) != (r,c):
                empty[(row, col)] = True

    return empty


def neighborhood(grid, row, column):
    
    offsets = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1),           (0, 1),
               (1, -1), (1, 0), (1, 1)]

    count = 0
    
    for offset in offsets:
        r = row + offset[0]
        c = column + offset[1]
        if (r >= 0 and r < Rows) and (c >= 0 and c < Columns):
            if grid[r][c] == FILLED:
                count = count + 1

    return count

def randomMovement(pos):
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

   
def DLA(rows, columns, moveLimit, radius, particles):
    grid = emptyGrid(rows, columns)
    empty = initialize(grid)

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
            newR, newC = randomMovement((R, C))
            # it's possible that random movement tells us to move to a squat that isn't empty
            # loop until we've got a square that is
            while (newR, newC) not in ELIST:
                newR, newC = randomMovement((R, C))
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
    
def main():
    numParticles = int(input("How many particles would you like for the simulation?: ").strip())
    moveLimit = int(input("What movelimit would you like?: ").strip())

    if moveLimit < Rows / 2 + 25:
        print("That's a pretty small move limit! When the radius gets big particles might have trouble finding a sticking point...")
        ans = input("Are you sure you want to run? (y/n): ").strip()
        if ans != 'y':
            print("Quitting Simulation. . .")
            exit(0)

    print("---- Starting DLA simulation with %s particles ----"%(numParticles))
    radius = 5
    start_time = time.time()
    grid = DLA(Rows, Columns, moveLimit, radius, numParticles)
    end_time = time.time()
    print("Simulation for: %s particles with move limit: %s took %s seconds"%(numParticles, moveLimit, int(end_time - start_time)))


    scale = 6 #int(input("Screen scale?: "))
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
                

