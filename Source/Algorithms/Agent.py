import random

from Source.Engine.Entity import Entity
from Source.Algorithms.Pathfinding import AStar


class Agent(Entity):

    def __init__(self, xPosition = 500, yPosition = 500, zPosition = 1, bodyWidth = 50, bodyHeight = 50, playerNumber : int = 0):
        
        super().__init__(xPosition, yPosition, zPosition, bodyWidth, bodyHeight, True, True, True)
        self.tick = 0
        self.tickMax = 144 * 0.5

        self.currentChoice = 0

        self.stepWidth = self.bodyWidth

        self.algorithm = AStar( {"Start" : 2 + playerNumber, "End" : 3 - playerNumber, "Obstacle" : 1})
        self.path = None
        self.currentPositionRelative : tuple = (0,0)

    
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