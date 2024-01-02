from Source.Game.Util import *
from Source.Algorithms.Agent import Agent
import pygame 

class LabTest:

    def __init__(self):

        self.entities = []
        self.end = None
    
    def setupLab(self):

        self.entities = []
        self.end = None
        self.bot = None
        
        '''
        labyrinth = [
                        [2, 0, 1, 0, 0, 0, 1, 1, 1, 0],
                        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 1, 3]
                    ]
        '''

        import random

        labyrinth = [[0 for _ in range(10)] for __ in range(10)]
        labyrinth[0][0] = 2
        labyrinth[-1][-1] = 3


        for y in range(10):
            for x in range(10):
                choice = random.randint(0,100)
                if choice >= 85 and labyrinth[x][y] == 0:
                    labyrinth[x][y] = 1

        aBot = Agent(300, 200)
        aBot.setup(labyrinth)
        self.entities.append(aBot)
        aBot.getTextureComponent().color = (255,0, 0)
        self.bot = aBot

        for i in range(11):
            point = MyEntity(250, 150 + i * 50, 0, 50, 50)
            self.entities.append(point)
        for i in range(11):
            point = MyEntity(250 + 550, 150 + i * 50, 0, 50, 50)
            self.entities.append(point)
        for i in range(11):
            point = MyEntity(250 + i * 50, 150, 0, 50, 50)
            self.entities.append(point)
        for i in range(12):
            point = MyEntity(250 + i * 50, 150 + 550, 0, 50, 50)
            self.entities.append(point)

        endPoint = aBot.algorithm.end.coords
        end = MyEntity(300 + 50 * endPoint[0], 200 + 50 * endPoint[1], bodyWidth=50, bodyHeight=50)
        self.end = end
        end.getTextureComponent().color = (0,255,0)
        self.entities.append(end)

        for y in range(len(labyrinth)):
            for x in range(len(labyrinth[0])):
                if labyrinth[y][x] == 1:
                    self.entities.append(MyEntity(300 + x * 50, 200 + y * 50, 0, 50, 50))
        
