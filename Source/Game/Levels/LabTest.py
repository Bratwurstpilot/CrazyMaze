import pygame
import random

from Source.Game.Util import *
from Source.Algorithms.Agent import Agent, AgentEvo
from Source.Game.Labyrinth import Labyrinth
from Source.Engine.Scene import Scene


from random import randint

class LabTest:

    def __init__(self):

        self.entities : list = []
        self.end : list = None
        self.bot : list = []
    

    def setupLab(self):

        self.entities = []
        self.end = []
        self.bot = []
        self.portalBlue = None
        self.portalOrange = None
        
        labyrinth = Labyrinth(45,31).getLabyrinth()

        WIDTH = len(labyrinth[0])
        HEIGHT = len(labyrinth)
        LINEWIDTH = 20
        playernum = 0
        START = [500 ,200] #x = 1920//4 + 20

        labBG = MyEntity(START[0], START[1], 0, 47*LINEWIDTH, 33*LINEWIDTH)
        labBG.getTextureComponent().color = (100,100,100)
        self.entities.append(labBG)

        #TP Test--------------------------

        tpSpots = ["T1"]

        #---------

        for y in range(len(labyrinth)):
            for x in range(len(labyrinth[0])):
                choice = random.randint(0,100)

                if labyrinth[y][x] == 1:
                    wallEntt = MyEntity(START[0] + x * LINEWIDTH, START[1] + y * LINEWIDTH, 0, LINEWIDTH, LINEWIDTH)
                    self.entities.append(wallEntt)

                if choice >= 95 and labyrinth[y][x] == 0 and self.portalBlue == None:
                    
                    labyrinth[y][x] = "T1" #change value, dont interrupt with coins
                    self.portalBlue = MyEntity(START[0] + x * LINEWIDTH, START[1] + y * LINEWIDTH, 0, LINEWIDTH, LINEWIDTH)
                    self.portalBlue.getTextureComponent().color = (0, 0, 255) #blue
                    self.entities.append(self.portalBlue)

                if choice >= 95 and y > (len(labyrinth) * 0.80) and labyrinth[y][x] == 0 and self.portalOrange == None:

                    labyrinth[y][x] = "T1"
                    self.portalOrange = MyEntity(START[0] + x * LINEWIDTH, START[1] + y * LINEWIDTH, 0, LINEWIDTH, LINEWIDTH)
                    self.portalOrange.getTextureComponent().color = (255, 165, 0) #orange
                    self.entities.append(self.portalOrange)


        aBot = Agent(START[0] + (1-playernum) * LINEWIDTH + (WIDTH-2) * LINEWIDTH * playernum, START[1] + (1-playernum) * LINEWIDTH + (HEIGHT-2) * LINEWIDTH * playernum, 1, LINEWIDTH, LINEWIDTH, playerNumber=playernum, transport = tpSpots)
        aBot.setup(labyrinth)
        self.entities.append(aBot)
        aBot.getTextureComponent().color = (255,0, 0)
        self.bot.append(aBot)
        self.end.append(aBot.getPosition())

        playernumB = 1

        bBot = AgentEvo(START[0] + (1-playernumB) * LINEWIDTH + (WIDTH-2) * LINEWIDTH * playernumB, START[1] + (1-playernumB) * LINEWIDTH + (HEIGHT-2) * LINEWIDTH * playernumB, 1, LINEWIDTH, LINEWIDTH, playerNumber=playernumB, transport=tpSpots)
        
        #------Testing Tsp Solver
        
        coins = 0
        for y in range(len(labyrinth)):
            for x in range(len(labyrinth[0])):
                if randint(0,100) >= 95 and labyrinth[y][x] == 0 and coins < 10:
                    coins += 1
                    bBot.anchorPoints.append((x,y))
                    entt = MyEntity(START[0] + x * LINEWIDTH, START[1] + y * LINEWIDTH, 0, LINEWIDTH, LINEWIDTH)
                    entt.textureComp.color = (138,43,226) #violet
                    self.entities.append(entt)
        #-----------------------
                    
        bBot.setup(labyrinth)
        self.entities.append(bBot)
        bBot.getTextureComponent().color = (255,255, 0)
        self.bot.append(bBot)
        self.end.append(bBot.getPosition())

        #UI Elements (sprites, infotables, etc)

        towerLeft = MyEntity(-50, 500)
        towerLeft.getTextureComponent().setTextureSet(["Source/Game/Files/Tower.png"], (600,600))
        self.entities.append(towerLeft)

        playerLeft = MyEntity(50, 460)
        playerLeft.getTextureComponent().setTextureSet(["Source/Game/Files/KnightSprite1.png", "Source/Game/Files/KnightSprite2.png"], (400,400))
        playerLeft.getTextureComponent().setFrameInterval(0.5)
        self.entities.append(playerLeft)

        towerRight = MyEntity(1370, 500)
        towerRight.getTextureComponent().setTextureSet(["Source/Game/Files/Tower.png"], (600,600))
        self.entities.append(towerRight)

        playerRight = MyEntity(1470, 420)
        playerRight.getTextureComponent().setTextureSet(["Source/Game/Files/Echse_1.png", "Source/Game/Files/Echse_2.png"], (400,400))
        playerRight.getTextureComponent().setFrameInterval(0.5)
        self.entities.append(playerRight)




        #------------------------
                    
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
background = pygame.image.load("Source/Game/Files/CreateBackground.png")
controllers = []


def setup(screen, func = None, param = None):

    global gameScene
    global botPackage
    
    bot = object.bot[0]
    bBot = object.bot[1]
    botPos = bot.getPosition().copy()
    bBotPos = bBot.getPosition().copy()
    portalBlue = object.portalBlue
    portalOrange = object.portalOrange
    botPackage = {"bot" : bot, "bot2" : bBot, "pos" : botPos, "pos2" : bBotPos, "scene" : gameScene, "blue" : portalBlue, "orange" : portalOrange}

    gameScene = Scene(screen, object.entities, [], background)