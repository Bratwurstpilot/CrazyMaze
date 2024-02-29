import pygame
import random

from Source.Game.Util import *
from Source.Algorithms.Agent import Agent
from Source.Game.Labyrinth import Labyrinth
from Source.Engine.Scene import Scene


class Tournament:

    def __init__(self):

        self.entities = []
        self.end = None
        
    
    def teleportation(self):
        pass
    
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


        aBot = Agent(START[0] + (1-playernum) * LINEWIDTH + (WIDTH-2) * LINEWIDTH * playernum, START[1] + (1-playernum) * LINEWIDTH + (HEIGHT-2) * LINEWIDTH * playernum, 1, LINEWIDTH, LINEWIDTH, playerNumber=playernum)
        aBot.setup(labyrinth)
        self.entities.append(aBot)
        aBot.getTextureComponent().color = (255,0, 0)
        self.bot.append(aBot)
        self.end.append(aBot.getPosition())

        playernumB = 1

        bBot = Agent(START[0] + (1-playernumB) * LINEWIDTH + (WIDTH-2) * LINEWIDTH * playernumB, START[1] + (1-playernumB) * LINEWIDTH + (HEIGHT-2) * LINEWIDTH * playernumB, 1, LINEWIDTH, LINEWIDTH, playerNumber=playernumB)
        bBot.setup(labyrinth)
        self.entities.append(bBot)
        bBot.getTextureComponent().color = (255,255, 0)
        self.bot.append(bBot)
        self.end.append(bBot.getPosition())

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
                    
    def checkWin(self):
        if self.bot[0].getPosition() == self.end[1]:
            print("Player1")
        if self.bot[1].getPosition() == self.end[0]:
            print("Player2")

#------------Setup-------------------------------
    
def customFunc(package : dict, gameInfo):
    
    bot = package["bot"]
    bot.tickMax = (0.001) * 144 * 0.1
    bBot = package["bot2"]
    bBot.tickMax = (0.001) * 144 * 0.1
    botPos = package["pos"]
    bBotPos = package["pos2"]

    return [botPos, bBotPos]


#------------------------------------------------

object = Tournament()
object.setupLab()
gameScene = None
botPackage = {}
background = pygame.image.load("Source/Game/Files/createBackground.png")
controllers = []


def setup(screen, func = None, param = None):

    global gameScene
    global botPackage
    global controllers
    
    bot = object.bot[0]
    bBot = object.bot[1]
    botPos = bot.getPosition().copy()
    bBotPos = bBot.getPosition().copy()
    portalBlue = object.portalBlue
    portalOrange = object.portalOrange
    botPackage = {"bot" : bot, "bot2" : bBot, "pos" : botPos, "pos2" : bBotPos, "scene" : gameScene, "blue" : portalBlue, "orange" : portalOrange}

    gameScene = Scene(screen, object.entities, [], background)