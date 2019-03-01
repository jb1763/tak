class Board:
    def __init__(self):
        board = [0]*(boardSize**2)

    def showBoard():
        for i in xrange(len(board)):
            if(i%5 == 0):
                sys.stdout.write('\n')
            if(board[i] is not None):
                sys.stdout.write(str(board[i].type)+" ")
            else:
                sys.stdout.write(str(board[i])+" ")
    def posToArray(x,y):
        return int((x-1) + (y-1)*(len(board)**.5))
