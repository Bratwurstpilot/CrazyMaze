from Source.Game.Util import *
from Source.Algorithms.Agent import Agent
import pygame 

class LabTest:

    def __init__(self):

        self.entities = []
    
    def setupLab(self):

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

        aBot = Agent(300, 200)
        aBot.setup(labyrinth)
        self.entities.append(aBot)
        aBot.getTextureComponent().color = (255,0, 0)

        endPoint = aBot.algorithm.end.coords
        end = MyEntity(300 + 50 * endPoint[0], 200 + 50 * endPoint[1], bodyWidth=50, bodyHeight=50)
        end.getTextureComponent().color = (0,255,0)
        self.entities.append(end)

        for y in range(len(labyrinth)):
            for x in range(len(labyrinth[0])):
                if labyrinth[y][x] == 1:
                    self.entities.append(MyEntity(300 + x * 50, 200 + y * 50, 0, 50, 50))
        
