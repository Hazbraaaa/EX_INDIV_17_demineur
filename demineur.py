import random
import math

# init variables

empty = 'O'
mine = 'X'
hidden = '.'
grid = []

# init functions

def createGrid(row, col):
    count = 0
    nbOfMine = calculcateNbOfMine(row, col)

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

    showGrid()

def showGrid():
    for row in grid:
        line = ''
        for elem in row:
            line += elem
        print(line)

def calculcateNbOfMine(row, col):
    return round(row * col * 0.15)

# execute code

createGrid(5, 7)
print('')
print(f"Number of mine = {calculcateNbOfMine(5,7)}")