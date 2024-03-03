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
        

class TransportNode(Node):

    def __init__(self, x, y):

        super().__init__(x,y)

        self.partnerNode : TransportNode = None
        self.keyCode : str = None
    

    def setPartnerNode(self, node):
        
        self.partnerNode = node
        self.neighbours.append(self.partnerNode)

    
    def setKeyCode(self, code : str) -> None:

        if self.keyCode == None:
            self.keyCode = code
        else:
            print("Node already has a valid key code")


    def update(self):

        self.neighbours.append(self.partnerNode)


class AStar(Algorithm):

    def __init__(self, symbols : dict = {"Start" : 2, "End" : 3, "Obstacle" : 1}):

        super().__init__(symbols)

        self.open : list = []
        self.closed : list = []

        self.nodes : list = []

        self.start : tuple = None
        self.end : tuple = ()
        
        self.possibleEnds : list = []

        self.transportNodes : list = []


    def __del__(self):

        pass


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

            value : float = node.iter+1 + self.heuristic(succNode.coords, self.end.coords)

            if succNode in self.open or succNode in self.closed: 
                if value >= succNode.value:
                    continue
                else:
                    try:
                        self.open.remove(succNode)
                    except Exception:
                        pass
                    try:
                        self.closed.remove(succNode)
                    except Exception:
                        pass

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

        def getNodeNeighbours(cNode : Node, x : int, y : int) -> None:
            
            for node in self.nodes:

                if node.coords[0] == x - 1 and node.coords[1] == y:
                    if node not in cNode.neighbours:
                        cNode.neighbours.append(node)
                    if cNode not in node.neighbours:
                        node.neighbours.append(cNode)

                elif node.coords[0] == x + 1 and node.coords[1] == y:
                    if node not in cNode.neighbours:
                        cNode.neighbours.append(node)
                    if cNode not in node.neighbours:
                        node.neighbours.append(cNode)

                elif node.coords[0] == x and node.coords[1] == y - 1:
                    if node not in cNode.neighbours:
                        cNode.neighbours.append(node)
                    if cNode not in node.neighbours:
                        node.neighbours.append(cNode)

                elif node.coords[0] == x and node.coords[1] == y + 1:
                    if node not in cNode.neighbours:
                        cNode.neighbours.append(node)
                    if cNode not in node.neighbours:
                        node.neighbours.append(cNode)

        possibleEnds : list = []

        for i in range(len(self.viewSpace)):
            for j in range(len(self.viewSpace[0])):

                node = Node(j,i)

                if self.viewSpace[i][j] == self.symbol["Start"]:
                    self.start = node
                elif self.viewSpace[i][j] == self.symbol["End"]:
                    possibleEnds.append(node)
                elif self.viewSpace[i][j] == self.symbol["Obstacle"]:
                    continue
                elif self.viewSpace[i][j] in self.symbol["Transport"]:
                    node = TransportNode(j,i)
                    node.setKeyCode(self.viewSpace[i][j])
                    self.transportNodes.append(node)

                self.nodes.append(node)
                getNodeNeighbours(node, *node.coords)
        
        if type(self.start) == list:
            self.start = Node(-1, -1)
            return

        possibleEnds.sort(key=lambda x : self.heuristic(self.start.coords, x.coords))
        self.end = Node(len(self.viewSpace[0])-1, len(self.viewSpace)-1)
        self.possibleEnds = possibleEnds

        for transportNodeCurrent in self.transportNodes:
            for transportNodePartner in self.transportNodes:
                if transportNodeCurrent == transportNodePartner:
                    continue
                if transportNodeCurrent.keyCode == transportNodePartner.keyCode:
                    transportNodeCurrent.setPartnerNode(transportNodePartner)

        self.open.append(self.start)


    def reset(self) -> None: 

        self.open = []
        self.closed = []
        self.nodes = []
        self.start = []
        self.end = []
        self.possibleEnds = []


    def heuristic(self, position : tuple, endPoint : tuple) -> float:
        
        #Manhatten distance
        return abs(endPoint[0] - position[0]) + abs(endPoint[1] - position[1])
    

    def getPath(self) -> list:
        
        self.possibleEnds.sort(key=lambda x:x.value)
        self.end = self.possibleEnds[0]
        path : list = [self.end.coords]
        current : Node = self.end

        while True:
            if current.coords == self.start.coords:
                break

            predList : list = current.pred

            if len(predList) == 0:
                return []

            maxNode = predList[0]

            for node in predList:
                if node.value <= maxNode.value:
                    maxNode = node

            path.append(maxNode.coords)
            current = maxNode

        return path