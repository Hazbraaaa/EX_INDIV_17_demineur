import random
import math

# init variables

empty = '.'
mine = 'X'
hidden = 'O'


# init functions

def game(row, col):
    gridToSolve = createGridToSolve(row, col)

    gridYouSee = createGridYouSee(row, col)
    showGrid(gridYouSee)

    answer = 0
    while answer < 10:
        print(f"Enter row (between 1 and {row}):")
        rowTried = int(input()) - 1
        print(f"Enter col (between 1 and {col}):")
        colTried = int(input()) - 1
        gridYouSee[rowTried][colTried] = gridToSolve[rowTried][colTried]
        if gridToSolve[rowTried][colTried] == mine:
            break
        answer += 1
        showGrid(gridYouSee)
    showGrid(gridYouSee)
    

def createGridToSolve(row, col):
    count = 0
    nbOfMine = calculcateNbOfMine(row, col)
    grid = []

    for i in range(row):
        line = []
        for i in range(col):
            line.append(empty)
        grid.append(line)

    while count < nbOfMine:
        randomRow = math.floor(random.random() * row)
        randomCol = math.floor(random.random() * col)
        if grid[randomRow][randomCol] == empty:
            grid[randomRow][randomCol] = mine
            count += 1
    return grid

def createGridYouSee(row, col):
    grid = []

    for i in range(row):
        line = []
        for i in range(col):
            line.append(hidden)
        grid.append(line)
    return grid

def showGrid(grid):
    for row in grid:
        line = ''
        for elem in row:
            line += elem
        print(line)
    print('')

def calculcateNbOfMine(row, col):
    return round(row * col * 0.15)


# execute code

game(4, 4)