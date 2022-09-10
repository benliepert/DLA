import turtle ## for drawing
import random ## for random walk
import math ## distance formula (square root)
import copy ##copying lists so they won't be bound together

EMPTY = 0
FILLED = 1
SCALE = 3 ## width of boxes

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

def createCircles(screen, colors):

    square = ((0, 0), (0, SCALE), (SCALE, SCALE), (SCALE, 0))
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
##    direction = random.randrange(1,9)
    
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

def rPlusOne(empty, radius):
    '''
    Return a dictionary of points that are (radius + 1) from the center
    '''
    newEmptyList = {}

    for item in empty:
        if distance(item) == (radius + 1):
            newEmptyList[item] = True

    # TODO: try spawning particles at any random spot on the grid and setting the move limit high

    return newEmptyList

   
def DLA(rows, columns, moveLimit, radius, particles):
    grid = emptyGrid(rows, columns)
    emptyList = initialize(grid)
    numParts = particles
    
    numUnstuck = 1
    while numParts > 0:
        newEmptyList = rPlusOne(emptyList, radius) # list of pts that's radius distance from the center
        newGrid = copy.deepcopy(grid)
        ELIST = emptyList
        startR, startC = random.choice(list(newEmptyList.keys()))
        newGrid[startR][startC] = FILLED

        R = startR
        C = startC
        stuck = False

        counter = 0
  
        while not stuck and counter < moveLimit:
            newR, newC = randomMovement((R, C))
            newGrid[R][C] = EMPTY # the particle used to be at this spot
            newGrid[newR][newC] = FILLED # the particle moved to this spot

            count = neighborhood(grid, newR, newC)
                
            if count > 0:
                stuck = True

                if (newR, newC) not in list(ELIST.keys()):
                    break
                else:
                    del ELIST[(newR, newC)]
                    ELIST[(R, C)] = True
                    if distance((newR, newC)) > radius and radius + 1 < Rows // 2:
                        radius += 1
                        # TODO: add less and less to the radius as more particles stick
                        # this should reduce the amount of straight strands that appear
                        # could also spawn particles at any random spot in the grid...
                        
                    numParts -= 1 
                    print("Particle stuck in %s moves. Radius is %s. Particles remaining = %s"%(counter, radius, numParts))
                    
            R, C = newR, newC # new point becomes the current point
            grid = newGrid
            counter += 1 
            emptyList = ELIST

        if not stuck:
            # the loop has finished. So we know we reached the move limit. Spawn another point
            print("- - - Unstuck particle #%s"%(numUnstuck))
            numUnstuck += 1
            newGrid[R][C] = EMPTY
            ELIST[(R, C)] = True

        grid = newGrid
        
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
    moveLimit = 100
    numParticles = int(input("How many particles would you like for the simulation?: ").strip())
    moveLimit = int(input("What movelimit would you like?: ").strip())

    print("---- Starting DLA simulation with %s particles ----"%(numParticles))
    grid = DLA(Rows, Columns, moveLimit, 0, numParticles)
    print("---- DLA simulation completed... Drawing grid ----")

    george = turtle.Turtle()
    screen = george.getscreen()
    screen.setup(Columns * SCALE + 20, Rows * SCALE + 20) # page 707
    screen.setworldcoordinates(0, 0, Columns, Rows)
    screen.tracer(100)
    george.hideturtle()
    createCircles(screen, ['blue', 'white'])

    drawGrid(Rows, Columns, george)
    fillGrid(george, grid)

    screen.update()
    x = input("Press any button to quit . . .")
    
main()
                

