import pygame
import random

from Source.Game.Util import *
from Source.Algorithms.Agent import Agent
from Source.Game.Labyrinth import Labyrinth
from Source.Engine.Scene import Scene


class LabTest:

    def __init__(self):

        self.entities = []
        self.end = None
    
    def teleportation(self):
        pass
    
    def setupLab(self):

        self.entities = []
        self.end = None
        self.bot = []
        self.portalBlue = None
        self.portalOrange = None
        
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
                choice = random.randint(0,100)

                if labyrinth[y][x] == 1:

                    self.entities.append(MyEntity(START[0] + x * LINEWIDTH, START[1] + y * LINEWIDTH, 0, LINEWIDTH, LINEWIDTH))

                if choice >= 95 and labyrinth[y][x] == 0 and self.portalBlue == None:
    
                    self.portalBlue = MyEntity(START[0] + x * LINEWIDTH, START[1] + y * LINEWIDTH, 0, LINEWIDTH, LINEWIDTH)
                    self.portalBlue.getTextureComponent().color = (0, 0, 255) #blue
                    self.entities.append(self.portalBlue)

                if choice >= 95 and y > (len(labyrinth) / 1.25) and labyrinth[y][x] == 0 and self.portalOrange == None:
                    self.portalOrange = MyEntity(START[0] + x * LINEWIDTH, START[1] + y * LINEWIDTH, 0, LINEWIDTH, LINEWIDTH)
                    self.portalOrange.getTextureComponent().color = (255, 165, 0) #orange
                    self.entities.append(self.portalOrange)
                    

#------------Setup-------------------------------
    
def customFunc(package : dict, gameInfo):
    
    bot = package["bot"]
    bot.tickMax = (2 - gameInfo.botDifficulty[0] + 1) * 144 * 0.1
    bBot = package["bot2"]
    bBot.tickMax = (2 - gameInfo.botDifficulty[1] + 1) * 144 * 0.1
    botPos = package["pos"]
    bBotPos = package["pos2"]
    botPlayScene = package["scene"]

    portalBlue = package["blue"]
    portalOrange = package["orange"]

    if botPos[0] == portalBlue.getPosition()[0] and botPos[1] == portalBlue.getPosition()[1]:
        botPos[0] = portalOrange.getPosition()[0]
        botPos[1] = portalOrange.getPosition()[1]

    if botPos[0] == portalOrange.getPosition()[0] and botPos[1] == portalOrange.getPosition()[1]:
        botPos[0] = portalBlue.getPosition()[0]
        botPos[1] = portalBlue.getPosition()[1]
        
    if botPos[0] != bot.getPosition()[0] or botPos[1] != bot.getPosition()[1]:
        elem = MyEntity(botPos.copy()[0], botPos.copy()[1], -1 ,bodyWidth=bot.bodyWidth, bodyHeight=bot.bodyHeight)
        elem.getTextureComponent().color = (0,100,255)
        botPlayScene.elements.append(elem)
        botPos = bot.getPosition().copy()
    
    if bBotPos[0] != bBot.getPosition()[0] or bBotPos[1] != bBot.getPosition()[1]:
        elem = MyEntity(bBotPos.copy()[0], bBotPos.copy()[1], -1 ,bodyWidth=bBot.bodyWidth, bodyHeight=bBot.bodyHeight)
        elem.getTextureComponent().color = (0, 255, 0)
        botPlayScene.elements.append(elem)
        bBotPos = bBot.getPosition().copy()

    return [botPos, bBotPos]


#------------------------------------------------

object = LabTest()
object.setupLab()
gameScene = None
botPackage = {}
background = pygame.image.load("Source/Game/Files/createBackground.png")
controllers = []


def setup(screen, func = None, param = None):

    global gameScene
    global botPackage
    global controllers
    global knight
    
    bot = object.bot[0]
    bBot = object.bot[1]
    botPos = bot.getPosition().copy()
    bBotPos = bBot.getPosition().copy()
    portalBlue = object.portalBlue
    portalOrange = object.portalOrange
    botPackage = {"bot" : bot, "bot2" : bBot, "pos" : botPos, "pos2" : bBotPos, "scene" : gameScene, "blue" : portalBlue, "orange" : portalOrange}

    knight = MyEntity(300, 300, 1, 20, 20)
    knight.getTextureComponent().color = (255, 255, 255)
    object.entities.append(knight)

    controller = MyController([knight])
    controllers.append(controller)

    gameScene = Scene(screen, object.entities, [], background)





    