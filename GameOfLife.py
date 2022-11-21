import random
import numpy as np
import cv2

def printGrid(grid):
    ngrid = np.array(grid)
    img = np.zeros((len(ngrid[0]), len(ngrid), 3))
    img[ngrid>0.5] = [1,1,1]
    img[ngrid<0.5] = [0,0,0]
    frame = cv2.resize(img, (len(ngrid[0]) * 20, len(ngrid) * 20), interpolation = cv2.INTER_AREA)
    cv2.imshow("GameOfLife", frame)

def rules(grid, y, x):
    cell = grid[y][x]
    neighbors = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if (dy != 0 or dx != 0) and 0 <= x + dx and x + dx < width and 0 <= y + dy and y + dy < height:
                neighbors += grid[y + dy][x + dx]
    if (cell == 1 and (neighbors == 2 or neighbors == 3)) or (cell == 0 and neighbors == 3):
        return 1
    else: return 0          

if __name__ == "__main__":
    width = 40
    height = 40
    grid = [[random.randrange(2) for j in range(width)] for i in range(height)]
    while True:
        printGrid(grid)
        if cv2.waitKey(100) & 0xFF == ord('q'):
                break
        newGrid = [[0 for j in range(width)] for i in range(height)]
        for y in range(height):
            for x in range(width):
                newGrid[y][x] = rules(grid, y, x)
        grid = newGrid
        
        

