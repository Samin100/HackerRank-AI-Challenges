#!/usr/bin/python
def displayPathtoPrincess(n,grid):

    mario = []
    peach = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 'm':
                mario.append(x)
                mario.append(y)
            if grid[x][y] == 'p':
                peach.append(x)
                peach.append(y)


    rowDif = mario[0] - peach[0]
    colDif = mario[1] - peach[1]

    if rowDif > 0:
        for x in range(abs(rowDif)):
            print('UP')
    elif rowDif < 0:
        for x in range(abs(rowDif)):
            print('DOWN')

    if colDif > 0:
        for x in range(abs(colDif)):
            print('LEFT')
    elif colDif < 0:
        for x in range(abs(colDif)):
            print('RIGHT')


#print all the moves here
m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m,grid)