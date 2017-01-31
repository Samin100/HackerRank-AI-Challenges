#!/usr/bin/python

# Head ends here
def next_move(posr, posc, board):

    bot = [posr, posc]
    grid = board
    dirtySpots = []

    for x in range(5):
        line = grid[x]
        row = []

        charIndex = 0
        for char in line:

            row.append(char)
            if char == 'd':
                dirtySpots.append([x, charIndex])

            charIndex += 1

        grid.append(row)

    if bot in dirtySpots:
        print('CLEAN')
        return

    closestSpot = 9  # max number of possible moves + 1 to nearest dirty block for a 5x5 grid

    for spot in dirtySpots:
        distance = abs(bot[0] + spot[0]) + abs(bot[1] + spot[1])
        spot.append(distance)
        if distance < closestSpot:
            closestSpot = distance

    # sorted function returns a sorted list - it is not an in place sort
    dirtySpots = sorted(dirtySpots, key=lambda i: i[2])

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

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
