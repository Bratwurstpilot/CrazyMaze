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

        width = 20
        height = 15

        labyrinth = [[0 for _ in range(width)] for __ in range(height)]
        labyrinth[0][0] = 2
        labyrinth[-1][-1] = 3


        for y in range(height):
            for x in range(width):
                choice = random.randint(0,100)
                if choice >= 75 and labyrinth[y][x] == 0:
                    labyrinth[y][x] = 1

        aBot = Agent(400, 200)
        aBot.setup(labyrinth)
        self.entities.append(aBot)
        aBot.getTextureComponent().color = (255,0, 0)
        self.bot = aBot

        for i in range(height+1):
            point = MyEntity(350, 150 + i * 50, 0, 50, 50)
            self.entities.append(point)
        for i in range(height+1):
            point = MyEntity(350 + (width + 1) * 50, 150 + i * 50, 0, 50, 50)
            self.entities.append(point)
        for i in range(width+1):
            point = MyEntity(350 + i * 50, 150, 0, 50, 50)
            self.entities.append(point)
        for i in range(width+2):
            point = MyEntity(350 + i * 50, 150 + (height + 1) * 50, 0, 50, 50)
            self.entities.append(point)

        endPoint = aBot.algorithm.end.coords
        end = MyEntity(400 + 50 * endPoint[0], 200 + 50 * endPoint[1], bodyWidth=50, bodyHeight=50)
        self.end = end
        end.getTextureComponent().color = (0,255,0)
        self.entities.append(end)

        for y in range(len(labyrinth)):
            for x in range(len(labyrinth[0])):
                if labyrinth[y][x] == 1:
                    self.entities.append(MyEntity(400 + x * 50, 200 + y * 50, 0, 50, 50))
        
