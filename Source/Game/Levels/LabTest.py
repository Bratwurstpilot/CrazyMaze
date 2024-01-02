from Source.Game.Util import *
from Source.Algorithms.Agent import Agent
from Source.Game.Labyrinth import Labyrinth
import pygame 

class LabTest:

    def __init__(self):

        self.entities = []
        self.end = None
    
    def setupLab(self):

        self.entities = []
        self.end = None
        self.bot = None
        
        labyrinth = Labyrinth(40,25).getLabyrinth()

        START = [400,200]
        LINEWIDTH = 30

        aBot = Agent(START[0] + LINEWIDTH, START[1] + LINEWIDTH, 1, LINEWIDTH, LINEWIDTH)
        aBot.setup(labyrinth)
        self.entities.append(aBot)
        aBot.getTextureComponent().color = (255,0, 0)
        self.bot = aBot

        endPoint = aBot.algorithm.end.coords
        end = MyEntity(START[0] + LINEWIDTH * endPoint[0], START[1] + LINEWIDTH * endPoint[1], bodyWidth=LINEWIDTH, bodyHeight=LINEWIDTH)
        self.end = end
        end.getTextureComponent().color = (0,255,0)
        self.entities.append(end)

        for y in range(len(labyrinth)):
            for x in range(len(labyrinth[0])):
                if labyrinth[y][x] == 1:
                    self.entities.append(MyEntity(START[0] + x * LINEWIDTH, START[1] + y * LINEWIDTH, 0, LINEWIDTH, LINEWIDTH))
        
