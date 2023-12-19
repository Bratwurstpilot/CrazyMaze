from abc import ABC, abstractmethod, abstractproperty
from math import sqrt


class Algorithm(ABC):

    def __init__(self, symbols : dict):
        '''
        Baseclass for all algorithims to work
        with the structure of crazymaze.

        symbols needs to contain the key:

        "Start"    : sym
        "End"      : sym
        "Obstacle" : sym
        '''

        self.viewSpace : list = []
        self.position : list = []
        self.paths : list = []
        self.neighbourhood : list = []

        self.choice : str = ""

        self.symbol : dict = symbols


    @abstractmethod
    def execRoutine(self) -> None:

        pass

    
    def update(self) -> None:

        self.execAlgorithm()


    def setViewSpace(self, space : list) -> None:

        self.viewSpace = space

    
    def getPositionChoice(self) -> str:

        return self.choice
    

    def getNeighbourhoodView(self) -> list:

        return self.getNeighbourhoodNode(tuple(self.position))
    

    def getNeighbourhoodNode(self, index : tuple) -> list:

        def isValid(node : tuple):

            return (node[0] >= 0 and node[0] < len(self.viewSpace[0]) and node[1] >= 0 and node[1] < len(self.viewSpace) and self.viewSpace[node[1]][node[0]] != self.symbol["Obstacle"])
    
        neighbourhood : list = [None for _ in range(4)]

        #Upper neighbour
        #neighbourhood[0] = self.viewSpace[index[1]-1][index[0]] 
        if isValid((index[0], index[1]+1)) : neighbourhood[0] = (index[0], index[1]+1)
        #Left neighbour
        #neighbourhood[2] = self.viewSpace[index[1]][index[0]]
        if isValid((index[0]-1, index[1])) : neighbourhood[1] = (index[0]-1, index[1])
        #Right neighbour
        #neighbourhood[2] = self.viewSpace[index[1]][index[0]] 
        if isValid((index[0]+1, index[1])) : neighbourhood[2] = (index[0]+1, index[1])
        #Lower neighbour
        #neighbourhood[3] = self.viewSpace[index[1]+1][index[0]]
        if isValid((index[0], index[1]-1)) : neighbourhood[3] = (index[0], index[1]-1)
        
        #Clean up
        for i in range(len(neighbourhood)-1, -1, -1):
            if neighbourhood[i] == None : neighbourhood.remove(neighbourhood[i])

        return neighbourhood

class Node:

        def __init__(self, x, y):
            
            self.coords : tuple = (x,y)
            self.pred : list = []
            self.value : int = 1000
            self.iter : int = 0

            self.neighbours = []
            
        
        def setPred(self, pred) -> None:

            self.pred.append(pred)

        
        def getNeighbours(self) -> list:

            return self.neighbours


class AStar(Algorithm):

    def __init__(self, symbols : dict = {"Start" : 2, "End" : 3, "Obstacle" : 1}):

        super().__init__(symbols)

        self.open : list = []
        self.closed : list = []

        self.nodes : list = []

        self.start : tuple = None
        self.end : tuple = None


    def execRoutine(self) -> None:
        
        self.setup()

        while len(self.open) > 0:

            currentNode = self.getMin()
            self.expandNode(currentNode)  
            self.closed.append(currentNode)          


    def expandNode(self, node : Node) -> list:
        
        nodes : list = node.neighbours

        for succNode in nodes:
            if succNode in node.pred:
                continue

            g : float = node.iter+1
            h : float = self.heuristic(succNode.coords, self.end.coords)
            f : float = g + h

            value : float = f

            if succNode in self.open or succNode in self.closed: 
                if value > succNode.value:
                    continue

            succNode.value = value
            succNode.iter = node.iter+1
            succNode.setPred(node)

            self.open.append(succNode)


    def getMin(self) -> tuple:

        minIndx = 0

        for i in range(1, len(self.open)):
            if self.open[i].value <= self.open[minIndx].value:
                minIndx = i

        element = self.open[minIndx]
        self.open.remove(element)

        return element


    def setup(self) -> None:

        def getNodeNeighbours(x : int, y : int) -> list:

            neighbours : list = []
            for node in self.nodes:
                if node.coords[0] == x - 1 and node.coords[1] == y:
                    neighbours.append(node)
                elif node.coords[0] == x + 1 and node.coords[1] == y:
                    neighbours.append(node)
                elif node.coords[0] == x and node.coords[1] == y - 1:
                    neighbours.append(node)
                elif node.coords[0] == x and node.coords[1] == y + 1:
                    neighbours.append(node)
            
            return neighbours

        for i in range(len(self.viewSpace)):
            for j in range(len(self.viewSpace[0])):
                node = Node(j,i)
                if self.viewSpace[i][j] == self.symbol["Start"]:
                    self.start = node
                elif self.viewSpace[i][j] == self.symbol["End"]:
                    self.end = node
                elif self.viewSpace[i][j] == self.symbol["Obstacle"]:
                    node = Node(-10,-10)
                self.nodes.append(node)

        for node in self.nodes:
            neighbours = getNodeNeighbours(*node.coords)
            node.neighbours = neighbours
                
        self.open.append(self.start)


    def heuristic(self, position : tuple, endPoint : tuple) -> float:
        
        #Euclidean distance
        return sqrt((endPoint[0] - position[0]) ** 2 + (endPoint[1] - position[1]) ** 2)
    

    def getPath(self) -> list:

        path : list = [self.end.coords]
        current : Node = self.end
        
        while True:
            if current == self.start:
                break

            predList : list = current.pred
            maxNode : Node = predList[0]

            for node in predList:
                if node.value <= maxNode.value:
                    maxNode = node

            path.append(maxNode.coords)
            current = maxNode

        return path