def detectBombs(grid):
    height = len(grid)
    width = len(grid[0])
    # need to have initialized array where to put bomb count    
    bombCount  = [[0] * len(row) for row in grid]    
    for y in range(0, height):
        for x in range(0, width):
            if y+1 < height and grid[y+1][x] == True:
                bombCount[y][x] += 1
            if y-1 >= 0 and grid[y-1][x] == True:
                bombCount[y][x] += 1
            if x+1 < width and grid[y][x+1] == True:
                bombCount[y][x] += 1
            if x-1 >= 0 and grid[y][x-1] == True:
                bombCount[y][x] += 1
            if y+1 < height and x+1 < width and grid[y+1][x+1] == True:
                bombCount[y][x] += 1
            if y+1 < height and x-1 >= 0 and grid[y+1][x-1] == True:
                bombCount[y][x] += 1
            if y-1 >= 0 and x+1 < width and grid[y-1][x+1] == True:
                bombCount[y][x] += 1
            if y-1 >= 0 and x-1 >= 0 and grid[y-1][x-1] == True:
                bombCount[y][x] += 1
    print("[")
    for row in bombCount:
        print(f"  {row},")
    print("]")
    


detectBombs([
    [True, False, False],
    [False, True, False],
    [False, False, False]
])

detectBombs([
  [True, False],
  [False, False]
])

detectBombs([
  [True, True],
  [False, False],
  [True, True]
])
