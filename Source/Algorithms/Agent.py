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
        
        self.viewSpace = viewSpace_

        if self.algorithm != None : self.algorithm.reset()

        self.marked = False
        self.currentPath = 0
        self.rethoughtPaths = []
        self.visited = []

        start = -1
        end = -1

        #Process Viewspace
        viewSpace = viewSpace_.copy()

        relevantPoints = []
        for y in range(len(viewSpace)):
            for x in range(len(viewSpace[0])):
                if viewSpace[y][x] == self.symbols["Start"]:
                    #relevantPoints.append((x,y))
                    start = (x,y)
                if viewSpace[y][x] == self.symbols["End"]:
                    relevantPoints.append((x,y))
                    end = (x,y)

        self.start = start
        self.end = end

        #Testing TSP solver-------
        for anchor in self.anchorPoints:
            relevantPoints.append(anchor)
        
        self.algorithm = EvoAlgo(populationCount=10, points=relevantPoints, bestEstimate=None, maxIterations=600)
        self.algorithm.fixedStart = start
        self.algorithm.update()

        #Pre process Labyrinth map to resemble start and end as the first points
        #of the optimal found route
        viewSpace[end[1]][end[0]] = 0
        viewSpace[start[1]][start[0]] = 0

        self.paths = []
        self.currentPoint = 0

        self.relativeStart = list(self.algorithm.fixedStart)
        self.relativeEnd = self.algorithm.globalBest[0].genes[0]

        self.currentPath = self.getPath(self.relativeStart, self.relativeEnd)

        self.positionRelative = start
            

    def update(self) -> None:
        
        self.tick += 1

        if self.tick < self.tickMax : return

        if self.currentPoint >= len(self.algorithm.globalBest[0].genes):
            return

        if len(self.currentPath) == 0:
            
            self.currentPoint += 1
            self.relativeEnd = self.algorithm.globalBest[0].genes[self.currentPoint]

            self.currentPath = self.getPath(self.positionRelative, self.relativeEnd)
        
        choice = self.currentPath[-1]
        self.currentPath.remove(choice)

        self.shiftPosition((choice[0] - self.positionRelative[0]) * self.stepWidth, (choice[1] - self.positionRelative[1]) * self.stepWidth)
        self.positionRelative = choice

        self.visited.append(choice)

        self.tick = 0
     

    def getPath(self, start, end) -> list:

        aStar = AStar()

        viewSpace = self.viewSpace.copy()

        viewSpace[self.start[1]][self.start[0]] = 0
        viewSpace[self.end[1]][self.end[0]] = 0

        viewSpace[end[1]][end[0]] = self.symbols["End"]
        viewSpace[start[1]][start[0]] = self.symbols["Start"]

        aStar.setViewSpace(viewSpace)

        aStar.execRoutine()
        path = aStar.getPath()
        path.remove(path[0])
        path.reverse()

        aStar.__del__()

        return path
