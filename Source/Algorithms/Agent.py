import random

from Source.Engine.Entity import Entity
from Source.Algorithms.Pathfinding import AStar
from Source.Algorithms.EvoAlgo import EvoAlgo

class Agent(Entity):

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

        self.currentChoice = 0

        self.currentPath = 0

        self.stepWidth = self.bodyWidth

        self.viewSpaceOriginal = None

        self.algorithm = AStar(self.symbols)
        self.path = None
        self.currentPositionRelative : tuple = (0,0)

    
    def __del__(self) -> None:
        
        pass


    def defineViewSpace(self, viewSpace : list):

        if len(self.anchorPoints) < 1:
            return viewSpace
        
        newViewSpace : list = []
        for line in viewSpace:
            newViewSpace.append(line.copy())

        for anchor in self.anchorPoints:
            if newViewSpace[anchor[1]][anchor[0]] == self.symbols["Start"]:
                pass
            else:
                newViewSpace[anchor[1]][anchor[0]] = self.symbols["End"]
        
        return newViewSpace
    

    def setup(self, viewSpace : list) -> None:
        
        #Save initial viewSpace
        self.viewSpaceOriginal = []
        for line in viewSpace:
            self.viewSpaceOriginal.append(line.copy())

        self.algorithm.__del__()
        self.algorithm = AStar(self.symbols)
        self.algorithm.setViewSpace(self.defineViewSpace(self.viewSpaceOriginal))
        self.algorithm.execRoutine()
        self.path = self.algorithm.getPath()
        if self.path == []:
            return
        self.positionRelative = self.path[-1]
        self.path.remove(self.path[-1])
        if tuple(self.path[0]) not in self.anchorPoints:
            self.anchorPoints.clear()


    def update(self) -> None:
        
        self.tick += 1
        
        if self.tick < self.tickMax : return
        try:
            #Is the current endNode already taken by the enemy:
            if tuple(self.path[0]) != tuple(self.algorithm.end.coords) and tuple(self.path[0]) not in self.anchorPoints:
                self.path.clear()
            choice = self.path[-1]
            self.path.remove(choice)

            self.shiftPosition((choice[0] - self.positionRelative[0]) * self.stepWidth, (choice[1] - self.positionRelative[1]) * self.stepWidth)
            self.positionRelative = choice

            self.tick = 0

        except IndexError:
            #No Anchor Points - No need to restart update process
            if len(self.anchorPoints) < 1:
                return
            #Delete current anchor
            if tuple(self.algorithm.end.coords) in self.anchorPoints:
                self.anchorPoints.remove(tuple(self.algorithm.end.coords))
            #Set Start to current position
            self.viewSpaceOriginal[self.algorithm.start.coords[1]][self.algorithm.start.coords[0]] = 0
            self.viewSpaceOriginal[self.positionRelative[1]][self.positionRelative[0]] = self.symbols["Start"]
            #Compute path to next nearest coin or end node
            viewSpaceCopy = []
            for line in self.viewSpaceOriginal:
                viewSpaceCopy.append(line.copy())

            self.setup(viewSpaceCopy)
            self.tick = 0

    
    def signal(self, str = "Coin", coords = (0,0), labCoords = [500,200], labLineWidth = 20):
        #Remove Coins from Anchor points
        manipCoords = [int((coords[0]-labCoords[0]) // labLineWidth), int((coords[1]-labCoords[1]) // labLineWidth)]

        if tuple(manipCoords) in self.anchorPoints:
            self.anchorPoints.remove(tuple(manipCoords))
            #Set Start to current position
            self.viewSpaceOriginal[self.algorithm.start.coords[1]][self.algorithm.start.coords[0]] = 0
            self.viewSpaceOriginal[self.positionRelative[1]][self.positionRelative[0]] = self.symbols["Start"]
            #Compute path to next nearest coin or end node
            viewSpaceCopy = []
            for line in self.viewSpaceOriginal:
                viewSpaceCopy.append(line.copy())

            self.setup(viewSpaceCopy)


    def updateGameState(self, enemyPos : tuple, enemyPoints : int, thisPoints : int):
        '''
        Nothing happens here. AStar is greedy.
        '''
        pass


class AgentEvo(Entity):

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

        self.currentChoice = 0

        self.currentPath = 0

        self.stepWidth = self.bodyWidth

        self.algorithm = None
        self.path = None
        self.currentPositionRelative : tuple = (0,0)

        self.visited : list = []
        self.marked = False
        self.rethoughtPaths : list = []
        self.isGoingToGoal : bool = False
        self.flag = False

        self.positionSave = (-10, -10)
        
    
    def __del__(self) -> None:
        
        pass


    def setup(self, viewSpace_ : list) -> None:

        self.isGoingToGoal = False
        
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
                    #relevantPoints.append((x,y))
                    end = (x,y)
                if viewSpace_[y][x] == self.symbols["Obstacle"]:
                    self.viewSpace[y][x] = self.symbols["Obstacle"]
                if viewSpace_[y][x] in self.symbols["Transport"]:
                    self.viewSpace[y][x] = viewSpace_[y][x]

        self.start = start
        self.end = end

        #TSP solver-------
        for anchor in self.anchorPoints:
            relevantPoints.append(anchor)
        
        self.algorithm = EvoAlgo(populationCount=300, points=relevantPoints, bestEstimate=None, maxIterations=300, metric="Manhatten")
        self.algorithm.fixedStart = start
        self.algorithm.fixedEnd = end
        self.algorithm.setUp(self.viewSpace.copy(), self.symbols)
        self.algorithm.update()

        self.currentPoint = 0

        self.relativeStart = list(self.algorithm.fixedStart)
        self.relativeEnd = self.algorithm.globalBest[0].genes[0]

        self.currentPath = self.getPath(self.relativeStart, self.relativeEnd) 
        self.positionRelative = start
            

    def update(self) -> None:
        
        self.tick += 1

        if self.tick < self.tickMax :
            return

        if self.end in self.visited:
            self.visited.remove(self.end)

        #self.currentPoint >= len(self.algorithm.globalBest[0].genes) or 
        if self.positionRelative == self.end:
            return

        if len(self.currentPath) == 0 and self.currentPoint < len(self.algorithm.globalBest[0].genes)-1:
            self.flag = False
            self.currentPoint += 1
            self.getNextPath()

        try:
            choice = self.currentPath[-1] #Error potential
            self.currentPath.remove(choice)

            self.shiftPosition((choice[0] - self.positionRelative[0]) * self.stepWidth, (choice[1] - self.positionRelative[1]) * self.stepWidth)
            self.positionRelative = tuple(list(choice).copy())

            self.visited.append(choice)

        except IndexError:

            pass

        if self.positionRelative == self.positionSave:
            self.goToGoal()
        else:
            self.positionSave = tuple(list(self.positionRelative).copy())
    
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
    
    
    def signal(self, str : str = "Coin", coords : list = [0,0], labCoords : list = [500,200], labLineWidth : int = 20) -> None:
        
        if self.isGoingToGoal:
            return
        
        if str == "Coin":
            
            manipCoords = [int((coords[0]-labCoords[0]) // labLineWidth), int((coords[1]-labCoords[1]) // labLineWidth)]
            self.visited.append(tuple(manipCoords))

            #if len(self.currentPath) < 1:
            #    self.goToGoal()
            
            self.getNextPath()

    
    def getNextPath(self) -> None:

        try:
            while self.algorithm.globalBest[0].genes[self.currentPoint] in self.visited:
                self.currentPoint += 1
                #print("Let me rethink that... ")

            self.relativeEnd = self.algorithm.globalBest[0].genes[self.currentPoint]
            self.currentPath = []
            self.currentPath = self.getPath(self.positionRelative, self.relativeEnd).copy()
        except IndexError:
            self.goToGoal()


    def goToGoal(self) -> None:
        
        if self.isGoingToGoal:
            return
        print("Bot now goes to goal")
        self.isGoingToGoal = True

        #while tuple(self.algorithm.globalBest[0].genes[self.currentPoint]) != tuple(self.end) and self.currentPoint <= len(self.algorithm.globalBest[0].genes)-1:
        #    self.currentPoint += 1
        
        self.relativeEnd = tuple(self.end)
        self.currentPath = []
        self.currentPath = self.getPath(self.positionRelative, self.relativeEnd).copy()


    def updateGameState(self, enemyPos : tuple, enemyPoints : int, thisPoints : int, labCoords : list = [500,200], labLineWidth : int = 20) -> None:
        '''
        enemyPos -> (x,y)
        enemyPoints -> Current coin State of Enemy
        thisPoints -> Current coin State of this Agent 
        labCoords -> Dimensions of Labyrinth [width, height]
        labLineWidth -> lineWidth of labyrinth

        Assumption : there are 10 coins in the map and no penalty for being late to the goal
        '''

        manipCoords = [( (enemyPos[0]-labCoords[0]) / labLineWidth), ( (enemyPos[1]-labCoords[1]) / labLineWidth )]
        enemyPos = manipCoords

        def delta(this : tuple, enemy : tuple, epsilon : int = 0) -> bool:
            
            #Return true if the agent is closer to his goal than the enemy to his
            return ( abs(self.end[0] - this[0]) + abs(self.end[1] - this[1]) ) - epsilon >= ( abs(self.start[0] - enemy[0]) + abs(self.start[1] - enemy[1]) )

        if tuple(enemyPos) == tuple(self.start) and enemyPoints+2 <= thisPoints:
            return self.goToGoal()

        if thisPoints >= 5:
            if delta(self.positionRelative, enemyPos, 5):
                return self.goToGoal()
            else:
                #Enemy is closer to the goal
                if (10 - enemyPoints) < 5:
                    #There is still hope
                    return
                else:
                    return self.goToGoal()
        else:
            if (thisPoints + 2 > 6) and delta(self.positionRelative, enemyPos, 5):
                return self.goToGoal()
            else:
                return

        '''
        if thisPoints >= 6:
            self.goToGoal()
            return
        if thisPoints + enemyPoints >= 10:
            self.goToGoal()
            return
        if enemyPoints >= 5:
            self.goToGoal()
            return
        '''