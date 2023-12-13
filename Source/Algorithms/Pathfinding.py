from abc import ABC, abstractmethod, abstractproperty
from math import sqrt


class Algorithm(ABC):

    def __init__(self, symbols : dict):
        '''
        Baseclass for all algorithims to work
        with the structure of crazymaze.

        symbols needs to contain the key:

        "Start" : sym
        "End" : sym
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
    
''' TESTS
import random
labyrinth = [[random.randint(0,1) for _ in range(10)] for __ in range(10)]
for element in labyrinth:
    print(element)
print("\n")

algo = Algorithm()
algo.setViewSpace([labyrinth[0][1:4], labyrinth[1][1:4], labyrinth[2][1:4]])
for element in algo.viewSpace:
    print(element)
'''

class Node:

        def __init__(self, x, y):
            
            self.coords = (x,y)
            self.succ = []
            self.value : int = 1000
            self.iter = 0

        def setSucc(self, succ):
            
            self.succ.append(succ)


class AStar(Algorithm):

    def __init__(self, symbols : dict = {"Start" : 2, "End" : 3, "Obstacle" : 1}):

        super().__init__(symbols)

        self.open : list = []
        self.closed : list = []

        self.start : tuple = None
        self.end : tuple = None


    def execRoutine(self) -> None:
        
        self.setup()

        iter = 0
        while len(self.open) > 0:
            #print(self.open)
            iter += 1
            currentNode = self.getMin()
            
            if currentNode.coords == self.end.coords:
                print("path found")
                return self.closed

            self.closed.append(currentNode)
            self.expandNode(currentNode, iter)            


    def expandNode(self, node : Node, iter : int) -> list:
        
        nodes : list = self.getNeighbourhoodNode(node.coords)
        if len(nodes) == 0: return

        for i in range(len(nodes)):
            succNode = Node(*nodes[i])
            succNode.iter = node.iter + 1
            node.setSucc(succNode)

            g = succNode.iter
            h = self.heuristic(succNode.coords, self.end.coords)
            f = g + h
            succNode.value = f
            
            flag = False

            #Was node already a successor in its neighbourhood?
            for element in self.closed:

                if node in element.succ:
                    coords = element.coords
                    for succ in node.succ:
                        if succ.coords == coords:
                            node.succ.remove(succ)
                            break
                
                if succNode.coords == element.coords:
                    flag = True

            if not flag:
                self.open.append(succNode)


    def getMin(self) -> tuple:

        minIndx = 0

        for i in range(1, len(self.open)):
            if self.open[i].value < self.open[minIndx].value:
                minIndx = i

        element = self.open[minIndx]
        self.open.remove(element)

        return element


    def setup(self) -> None:

        for i in range(len(self.viewSpace)):
            for j in range(len(self.viewSpace[0])):
                if self.viewSpace[i][j] == self.symbol["Start"]:
                    self.start = Node(j,i)
                elif self.viewSpace[i][j] == self.symbol["End"]:
                    self.end = Node(j,i)
                
        self.open.append(self.start)


    def heuristic(self, position : tuple, endPoint : tuple):
        
        distance : float = (position[0] - endPoint[0]) ** 2 + (position[1] - endPoint[1]) ** 2

        # try skipping the square root operation as it is high cost
        return distance
    

    def getPath(self):

        queue : list = []

        def getMin(node : Node):
            if len(node.succ) == 0:
                return
            min = node.succ[0]
            for element in node.succ:
                if element.value < min.value:
                    min = element
            node.succ.remove(min)
            return min
        
        path = []
        current = astar.start
        queue.append(current)

        while True:

            current = getMin(current)

            if current == None:
                try:
                    path.remove(queue[-1])
                except ValueError: 
                    pass
                queue.remove(queue[-1])
                current = queue[-1]

            else:
                path.append(current)
                queue.append(current)

            if current.coords == self.end.coords:
                path.remove(path[-1])
                break

        return path
    

import random
labyrinth = [[0 for _ in range(10)] for __ in range(10)]
labyrinth[0][0] = 2
labyrinth[-1][-1] = 3

'''
labyrinth = [
    [2, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 1, 0, 3]
]
'''

'''
Solution:

    [2, 7, 1, 1, 0, 0, 0, 0, 0, 1]
    [1, 7, 0, 0, 1, 1, 0, 1, 0, 0]
    [1, 7, 7, 1, 1, 1, 1, 0, 0, 1]
    [0, 1, 7, 7, 0, 1, 0, 0, 1, 0]
    [1, 0, 0, 7, 7, 0, 0, 0, 1, 1]
    [0, 0, 1, 1, 7, 7, 1, 0, 0, 0]
    [0, 1, 0, 0, 0, 7, X, X, X, X] 
    [0, 0, 1, 0, 0, 7, 1, 1, 1, 1]
    [0, 0, 0, 0, 0, 7, 7, 7, 7, 0]
    [0, 0, 0, 1, 1, 0, 1, 1, 7, 3]
'''

for y in range(len(labyrinth)):
    for x in range(len(labyrinth[0])):
        choice = random.randint(1,10)
        if choice >= 9 and labyrinth[y][x] == 0:
            labyrinth[y][x] = 1

for element in labyrinth:
    print(*element)

astar = AStar()
astar.setViewSpace(labyrinth)
astar.execRoutine()

path = astar.getPath()

for node in path:
    labyrinth[node.coords[1]][node.coords[0]] = 7

for element in labyrinth:
    print(*element)