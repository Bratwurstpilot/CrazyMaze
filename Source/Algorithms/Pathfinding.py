from abc import ABC, abstractmethod, abstractproperty
from math import sqrt


class Algorithm(ABC):

    def __init__(self):

        self.viewSpace : list = []
        self.position : list = []
        self.paths : list = []
        self.neighbourhood : list = []

        self.choice : str = ""


    @abstractmethod
    def execRoutine(self) -> None:

        pass

    
    def update(self) -> None:

        self.execAlgorithm()


    def setViewSpace(self, space : list) -> None:

        self.viewSpace = space

    
    def getPositionChoice(self) -> str:

        return self.choice
    

    def getNeighbourhood(self) -> list:

        neighbourhood : list = []

        #Upper neighbour
        neighbourhood[0] = self.viewSpace[self.position[1]-1][self.position[0]] 

        #Left neighbour
        neighbourhood[2] = self.viewSpace[self.position[1]][self.position[0]-1] 

        #Right neighbour
        neighbourhood[2] = self.viewSpace[self.position[1]][self.position[0]+1] 

        #Lower neighbour
        neighbourhood[3] = self.viewSpace[self.position[1]+1][self.position[0]] 

        return neighbourhood
    

class AStar(Algorithm):

    def __init__(self):

        super().__init__()


    def execRoutine(self) -> None:
        pass        


    def heuristic(self, position : list, endPoint : list):
        
        distance : float = (position[0] - endPoint[0]) ** 2 + (position[0] - endPoint[0]) ** 2

        # try skipping the square root operation as it is high cost
        return distance