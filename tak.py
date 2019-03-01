import sys
boardSize = 5
board = [None]*(boardSize**2)

class Player:
    def __init__(self):
        self.stoneCount = 21
        self.capCount = 1

    def placeFlat(self,x,y):
        if(self.stoneCount>=1):
            board[posToArray(x,y)]=Stone(self, 'F')
            self.stoneCount= self.stoneCount-1

    def placeWall(self,x,y):
        global stoneCount
        if(stoneCount>=1):
            board[posToArray(x,y)]=Stone(self, 'W')
            stoneCount= stoneCount-1

    def placeCap(self,x,y):
        global capCount
        if(capCount>=1):
            board[posToArray(x,y)]=Capstone()
            capCount = capCount-1

    def movePiece(self,x,y):
        pass

class Gamepiece:
    def __init__(self, owner, type):
        self.beneath = None
        self.owner = owner
        self.type = type

    def toString(self):
        sys.stdout.write(owner + ": " +type+"\n")
        if(self.beneath is not None):
            self.beneath.toString()

class Stone(Gamepiece):
    pass

class Capstone(Gamepiece):
    def __init__():
        super(self,'C')
    

def posToArray(x,y):
    return int((x-1) + (y-1)*(len(board)**.5))

def showBoard():
    for i in xrange(len(board)):
        if(i%5 == 0):
            sys.stdout.write('\n')
        if(board[i] is not None):
            sys.stdout.write(str(board[i].type)+" ")
        else:
            sys.stdout.write(str(board[i])+" ")

    
