import random

from Source.Engine.Entity import Entity
from Source.Algorithms.Pathfinding import AStar
from Source.Algorithms.EvoAlgo import EvoAlgo

class Agent(Entity):

    def __init__(self, xPosition = 500, yPosition = 500, zPosition = 1, bodyWidth = 50, bodyHeight = 50, playerNumber : int = 0):
        
        super().__init__(xPosition, yPosition, zPosition, bodyWidth, bodyHeight, True, True, True)
        self.tick = 0
        self.tickMax = 144 * 5

        self.currentChoice = 0

        self.stepWidth = self.bodyWidth

        self.algorithm = AStar( {"Start" : 2 + playerNumber, "End" : 3 - playerNumber, "Obstacle" : 1} )
        self.path = None
        self.currentPositionRelative : tuple = (0,0)

        self.currentPath = 0

    
    def __del__(self) -> None:
        
        pass


    def setup(self, viewSpace : list) -> None:
        
        self.algorithm.setViewSpace(viewSpace)
        self.algorithm.execRoutine()
        self.path = self.algorithm.getPath()
        if self.path == []:
            return
        self.positionRelative = self.path[-1]
        self.path.remove(self.path[-1])


    def update(self) -> None:
        
        self.tick += 1
        
        if self.tick < self.tickMax : return
        try:
            choice = self.path[-1]
            self.path.remove(choice)

            self.shiftPosition((choice[0] - self.positionRelative[0]) * self.stepWidth, (choice[1] - self.positionRelative[1]) * self.stepWidth)
            self.positionRelative = choice

            self.tick = 0
        except IndexError:
            self.tick = 0


class AgentEvo(Entity):

    def __init__(self, xPosition = 500, yPosition = 500, zPosition = 1, bodyWidth = 50, bodyHeight = 50, playerNumber : int = 0):
        
        super().__init__(xPosition, yPosition, zPosition, bodyWidth, bodyHeight, True, True, True)
        self.tick = 0
        self.tickMax = 144 * 0.5

        self.symbols = {"Start" : 2 + playerNumber, "End" : 3 - playerNumber, "Obstacle" : 1}

        self.anchorPoints = []

        self.currentChoice = 0

        self.currentPath = 0

        self.stepWidth = self.bodyWidth

        self.algorithm = None
        self.path = None
        self.currentPositionRelative : tuple = (0,0)

        self.visited : list = []

        self.marked = False

        self.rethoughtPaths : list = []

    
    def __del__(self) -> None:
        
        pass


    def setup(self, viewSpace_ : list) -> None:
        
        self.viewSpace = [ [0 for _ in range(len(viewSpace_[0]))] for __ in range(len(viewSpace_)) ]

        if self.algorithm != None : self.algorithm.reset()

        self.marked = False
        self.currentPath = 0
        self.visited = []

        start = -1
        end = -1

        relevantPoints = []
        for y in range(len(viewSpace_)):
            for x in range(len(viewSpace_[0])):
                if viewSpace_[y][x] == self.symbols["Start"]:
                    start = (x,y)
                if viewSpace_[y][x] == self.symbols["End"]:
                    relevantPoints.append((x,y))
                    end = (x,y)
                if viewSpace_[y][x] == self.symbols["Obstacle"]:
                    self.viewSpace[y][x] = self.symbols["Obstacle"]

        self.start = start
        self.end = end

        #Testing TSP solver-------
        for anchor in self.anchorPoints:
            relevantPoints.append(anchor)
        
        self.algorithm = EvoAlgo(populationCount=10, points=relevantPoints, bestEstimate=None, maxIterations=600)
        self.algorithm.fixedStart = start
        self.algorithm.update()

        self.currentPoint = 0

        self.relativeStart = list(self.algorithm.fixedStart)
        self.relativeEnd = self.algorithm.globalBest[0].genes[0]

        self.currentPath = self.getPath(self.relativeStart, self.relativeEnd) 
        self.positionRelative = start
            

    def update(self) -> None:
        
        self.tick += 1

        if self.tick < self.tickMax : return

        if self.currentPoint >= len(self.algorithm.globalBest[0].genes) or self.positionRelative == self.end:
            return

        if len(self.currentPath) == 0 and self.currentPoint <= len(self.algorithm.globalBest[0].genes)-1:
            self.currentPoint += 1

            while self.algorithm.globalBest[0].genes[self.currentPoint] in self.visited:
                self.currentPoint += 1
                print("Let me rethink that...")

            self.relativeEnd = self.algorithm.globalBest[0].genes[self.currentPoint]
            self.currentPath = []
            self.currentPath = self.getPath(self.positionRelative, self.relativeEnd).copy()
        
        choice = self.currentPath[-1]
        self.currentPath.remove(choice)

        self.shiftPosition((choice[0] - self.positionRelative[0]) * self.stepWidth, (choice[1] - self.positionRelative[1]) * self.stepWidth)
        self.positionRelative = choice

        self.visited.append(choice)
    
        self.tick = 0
     

    def getPath(self, start_, end_) -> list:

        aStar = AStar(symbols=self.symbols)
        aStar.reset()

        viewSpace = []

        for element in self.viewSpace:
            viewSpace.append(element.copy())

        viewSpace[start_[1]][start_[0]] = self.symbols["Start"]
        viewSpace[end_[1]][end_[0]] = self.symbols["End"]

        aStar.viewSpace = viewSpace

        aStar.execRoutine()
        path = aStar.getPath().copy()

        path.remove(path[-1])
        aStar.__del__()

        return path