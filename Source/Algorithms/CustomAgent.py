from Source.Engine.Entity import Entity

class CustomAgent(Entity):

    def __init__(self, xPosition = 500, yPosition = 500, zPosition = 1, bodyWidth = 50, bodyHeight = 50, playerNumber : int = 0, start : int = None, end : int = None, obstacle : int = 1, transport : list = []):

        super().__init__(xPosition, yPosition, zPosition, bodyWidth, bodyHeight, True, True, True)
        self.tick = 0
        self.tickMax = 144 * 0.1

        if start == None:
            start = 2 + playerNumber
        if end == None:
            end = 3 - playerNumber

        self.symbols = {"Start" : start, "End" : end, "Obstacle" : obstacle, "Transport" : transport}
        self.anchorPoints = []
        
    def setup(self, viewSpace : list) -> None:
        
        pass
        #your implementation


    def update(self) -> None:
        
        self.tick += 1
        
        if self.tick < self.tickMax : return
        #your implementation
    
    
    def signal(self, str = "Coin", coords = (0,0), labCoords : list = [500,200], labLineWidth : int = 20):
        
        pass
        #your implementation


    def updateGameState(self, enemyPos : tuple, enemyPoints : int, thisPoints : int):
        
        pass
        #your implementation