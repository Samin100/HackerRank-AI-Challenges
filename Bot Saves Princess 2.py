#
def nextMove(n,r,c,grid):
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
        return 'UP'
    elif rowDif < 0:
        return 'DOWN'

    if colDif > 0:
        return 'LEFT'
    elif colDif < 0:
        return 'RIGHT'


n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
