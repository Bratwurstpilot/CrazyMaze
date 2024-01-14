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
        self.bot = []
        
        labyrinth = Labyrinth(45,31).getLabyrinth()

        WIDTH = len(labyrinth[0])
        HEIGHT = len(labyrinth)
        LINEWIDTH = 20
        playernum = 0
        START = [300,200]

        

        aBot = Agent(START[0] + (1-playernum) * LINEWIDTH + (WIDTH-2) * LINEWIDTH * playernum, START[1] + (1-playernum) * LINEWIDTH + (HEIGHT-2) * LINEWIDTH * playernum, 1, LINEWIDTH, LINEWIDTH, playerNumber=playernum)
        aBot.setup(labyrinth)

        self.entities.append(aBot)
        aBot.getTextureComponent().color = (255,0, 0)
        self.bot.append(aBot)

        playernumB = 1

        bBot = Agent(START[0] + (1-playernumB) * LINEWIDTH + (WIDTH-2) * LINEWIDTH * playernumB, START[1] + (1-playernumB) * LINEWIDTH + (HEIGHT-2) * LINEWIDTH * playernumB, 1, LINEWIDTH, LINEWIDTH, playerNumber=playernumB)
        bBot.setup(labyrinth)
        self.entities.append(bBot)
        bBot.getTextureComponent().color = (255,255, 0)
        self.bot.append(bBot)
    

        endPoint = aBot.algorithm.end.coords
        end = MyEntity(START[0] + LINEWIDTH * endPoint[0], START[1] + LINEWIDTH * endPoint[1], bodyWidth=LINEWIDTH, bodyHeight=LINEWIDTH)
        self.end = end
        end.getTextureComponent().color = (0,255,0)
        self.entities.append(end)
        

        for y in range(len(labyrinth)):
            for x in range(len(labyrinth[0])):
                if labyrinth[y][x] == 1:
                    self.entities.append(MyEntity(START[0] + x * LINEWIDTH, START[1] + y * LINEWIDTH, 0, LINEWIDTH, LINEWIDTH))