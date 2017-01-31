#!/bin/python3
def nextMove(posr, posc, board):
    dirtyR = 0
    dirtyC = 0
    found = False

    for x in range(5):

        if not found:
            for y in range(5):

                if board[x][y] == 'd':
                    dirtyR = x
                    dirtyC = y
                    found = True
                    break
        else:
            break

    colDif = posr - dirtyR
    rowDif = posc - dirtyC

    if colDif == 0 and rowDif == 0:
        print('CLEAN')
        return

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
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
