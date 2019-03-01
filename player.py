class Player:
    def __init__(self):
        self.stoneCount = 21
        self.capCount = 1

    def placeFlat(self,x,y):
        if(self.stoneCount>=1):
            board[posToArray(x,y)]=Stone(self, 'F')
            self.stoneCount= self.stoneCount-1

    def placeWall(self,x,y):
        if(self.stoneCount>0):
            board[posToArray(x,y)]=Stone(self, 'W')
            stoneCount= stoneCount-1

    def placeCap(self,x,y):
        global capCount
        if(capCount>=1):
            board[posToArray(x,y)]=Capstone()
            capCount = capCount-1

    def promptMove(self):
        pass

    def movePiece(self,x,y):
        pass
