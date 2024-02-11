def gridChallenge(grid):
    orderedGrid = [sorted(row) for row in grid]
    
    for i in range(len(orderedGrid[0])):
        column = [row[i] for row in orderedGrid]
        if column != sorted(column):
            return 'NO'
    
    return 'YES'