from Source.Game.Util import MyEntity

class Player(MyEntity):

    def __init__(self, positionX : int = 0, positionY : int = 0, positionZ : int = 0, bodyWidth : int = 100, bodyHeight : int = 100):

        super().__init__(positionX, positionY, positionZ, bodyWidth, bodyHeight)
        self.anchorPoints : list = []    
        self.positionRelative = (self.positionX, self.positionY, self.positionZ)


    def signal(self, str = "Coin", coords = (0,0), labCoords = [500,200], labLineWidth = 20):
        
        pass


    def updateGameState(self, enemyPos : tuple, enemyPoints : int, thisPoints : int):
        
        self.positionRelative = (self.positionX, self.positionY, self.positionZ)
        


    def setup(self, labyrinth):

        pass