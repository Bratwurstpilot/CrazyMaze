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

        aStar = AStar(symbols=self.symbols)

        #Pre process Labyrinth map to resemble start and end as the first points
        #of the optimal found route
        viewSpace[end[1]][end[0]] = 0
        viewSpace[start[1]][start[0]] = 0


        self.paths = []
        currentPoint = 0

        relativeStart = list(self.algorithm.fixedStart)

        while True:
            
            aStar.reset()

            relativeEnd = self.algorithm.globalBest[0].genes[currentPoint]

            viewSpace[relativeEnd[1]][relativeEnd[0]] = self.symbols["End"]
            viewSpace[relativeStart[1]][relativeStart[0]] = self.symbols["Start"]

            aStar.setViewSpace(viewSpace)

            aStar.execRoutine()
            self.path = aStar.getPath()
            self.path.reverse()

            if self.path == []:
                return
            self.positionRelative = self.path[0]
            self.path.remove(self.path[0])
            self.paths.append(self.path.copy())

            currentPoint += 1
            
            viewSpace[relativeEnd[1]][relativeEnd[0]] = 0
            viewSpace[relativeStart[1]][relativeStart[0]] = 0

            relativeStart = list(relativeEnd).copy()

            if currentPoint >= len(self.algorithm.globalBest[0].genes):
                break
            
        self.positionRelative = start
            

    def update(self) -> None:
        
        self.tick += 1

        if self.tick < self.tickMax : return

        if len(self.paths[self.currentPath]) > 0:
            if self.paths[self.currentPath][-1] == self.end:
                self.marked = True

        try:
            choice = list(self.paths[self.currentPath][0])
            self.paths[self.currentPath].remove(tuple(choice))

            self.position_ = choice.copy()

            self.shiftPosition((choice[0] - self.positionRelative[0]) * self.stepWidth, (choice[1] - self.positionRelative[1]) * self.stepWidth)
            self.positionRelative = choice.copy()

            if choice not in self.visited: 
                self.visited.append(choice.copy())

            self.tick = 0

        except IndexError:

            if len(self.paths) < 1:
                return
            
            if self.marked:
                return
            
            self.tick = 0
            self.currentPath += 1

            if self.currentPath >= len(self.paths) - 1 :
                return
                   
            if len(self.paths[self.currentPath]) == 0:
                return
            
            mark = False

            while True:
                if list(self.paths[self.currentPath][-1]) in self.visited and list(self.paths[self.currentPath][-1]) not in self.rethoughtPaths:
                    self.paths.remove(self.paths[self.currentPath])
                    mark = True

                else:
                    break
                print("Let me rethink that...")
            
            if mark:
                self.paths[self.currentPath] = self.getPath(self.position_, list(self.paths[self.currentPath][-1]))
                self.rethoughtPaths.append(self.paths[self.currentPath])
            

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
        #path.reverse()

        aStar.__del__()

        return path
