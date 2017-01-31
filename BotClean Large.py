def next_move(posx, posy, dimx, dimy, board):

    bot = [posx, posy]
    grid = board
    dirtySpots = []

    for x in range(dimx):
        row = []

        for y in range(dimx):

            row.append(grid[x][y])
            if grid[x][y] == 'd':
                dirtySpots.append([x, y])

        grid.append(row)

    if bot in dirtySpots:
        print('CLEAN')
        return

    closestSpot = dimx * 2   # max number of possible moves + 2 (arbitrary max value)

    for spot in dirtySpots:
        distance = abs(bot[0] + spot[0]) + abs(bot[1] + spot[1])
        spot.append(distance)
        if distance < closestSpot:
            closestSpot = distance

    dirtySpots = sorted(dirtySpots, key=lambda i: i[2])  # sorted function returns a sorted list; it is not an in place sort

    colDif = bot[0] - dirtySpots[0][0]
    rowDif = bot[1] - dirtySpots[0][1]


    if colDif > 0:
        print('UP')
        return
    elif colDif < 0:
        print('DOWN')
        return

    if rowDif > 0:
        print('LEFT')
        return
    elif rowDif < 0:
        print('RIGHT')
        return

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)