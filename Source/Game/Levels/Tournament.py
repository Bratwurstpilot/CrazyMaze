import pygame
import random

from Source.Game.Util import *
from Source.Algorithms.Agent import Agent
from Source.Algorithms.Agent import AgentEvo
from Source.Game.Labyrinth import Labyrinth
from Source.Engine.Scene import Scene


class Tournament:

    def __init__(self):

        self.entities = []
        self.end = None
        self.bot : list = []
        self.gameInfo = None
        self.screen = None
        
    
    def setPlayer(self, gameInfo, start : list, linewidth : int, width : int, height : int, playernum : int, tpSpots : list):

        if gameInfo == "A Star":
            player = Agent(start[0] + (1-playernum) * linewidth + (width-2) * linewidth * playernum, start[1] + (1-playernum) * linewidth + (height-2) * linewidth * playernum, 1, linewidth, linewidth, playerNumber=playernum, transport = tpSpots)
        
        elif gameInfo == "TSP Solver":
            player = AgentEvo(start[0] + (1-playernum) * linewidth + (width-2) * linewidth * playernum, start[1] + (1-playernum) * linewidth + (height-2) * linewidth * playernum, 1, linewidth, linewidth, playerNumber=playernum, transport = tpSpots)
        
        return player
    

    def setPlayerTexture(self, gameInfo):

        if gameInfo == 0: #A Star Bot
            return ["Source/Game/Files/KnightSprite1.png", "Source/Game/Files/KnightSprite2.png"]
        elif gameInfo == 1: #TSP Solver Bot
            return ["Source/Game/Files/Echse_1.png", "Source/Game/Files/Echse_2.png"]
        

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
        START = [500 ,200] #x = 1920//4 + 20

        BGCOLOR = (10,10,10)
        labBG = MyEntity(START[0], START[1], -1, 47*LINEWIDTH, 33*LINEWIDTH)
        labBG.getTextureComponent().color = BGCOLOR
        self.entities.append(labBG)

        bg1 = MyEntity(0, 0, bodyWidth=1920, bodyHeight=1080)
        bg1.textureComp.color = BGCOLOR
        self.entities.append(bg1)

        bg2 = MyEntity(0,0)
        #bg2.textureComp.setTexture("Source/Game/Files/Gamefield.png", (1920,1080))
        self.entities.append(bg2)

        #TP Test--------------------------

        tpSpots = ["T1"]

        #---------

        #Wall Tex--
        TEX_WALL1WAY = "Source/Game/Files/wall1way.png"
        TEX_WALL2WAY = "Source/Game/Files/wall2way.png"
        TEX_WALL3WAY = "Source/Game/Files/wall3way.png"
        TEX_WALL4WAY = "Source/Game/Files/wall4way.png"

        def getSupposedTex(lab : list, wall : list):
            
            walls = []
            if wall[0] == 0 or wall[0] == len(lab[0])-1:
                return ["EDGE"]
            if wall[1] == 0 or wall[1] == len(lab)-1:
                return ["EDGE"]

            try:
                if lab[wall[1]][wall[0]+1] == 1:
                    walls.append("RIGHT")
            except IndexError: pass

            try:
                if lab[wall[1]][wall[0]-1] == 1:
                    walls.append("LEFT")
            except IndexError: pass

            try:
                if lab[wall[1]-1][wall[0]] == 1:
                    walls.append("UP")
            except IndexError: pass

            try:
                if lab[wall[1]+1][wall[0]] == 1:
                    walls.append("DOWN")
            except IndexError: pass

            #4way piece
            if "RIGHT" in walls and "LEFT" in walls and "UP" in walls and "DOWN" in walls:
                return [TEX_WALL4WAY, 0]
            
            #3way pieces
            if "RIGHT" in walls and "LEFT" in walls and "DOWN" in walls:
                return [TEX_WALL3WAY, 0] #Generic pieces
            if "UP" in walls and "LEFT" in walls and "DOWN" in walls:
                return [TEX_WALL3WAY, 90] #Rotated 90 degrees clockwise
            if "RIGHT" in walls and "LEFT" in walls and "UP" in walls:
                return [TEX_WALL3WAY, 180] #Rotated 180 degrees clockwise
            if "RIGHT" in walls and "UP" in walls and "DOWN" in walls:
                return [TEX_WALL3WAY, 270] #Rotated 270 degrees clockwise
            
            #2way piece
            if "DOWN" in walls and "RIGHT" in walls:
                return [TEX_WALL2WAY, 0] #Generic piece
            if "DOWN" in walls and "LEFT" in walls:
                return [TEX_WALL2WAY, 90] #Rotated 90 degrees clockwise
            if "UP" in walls and "LEFT" in walls:
                return [TEX_WALL2WAY, 180] #Rotated 180 degrees clockwise
            if "UP" in walls and "RIGHT" in walls:
                return [TEX_WALL2WAY, 270] #Rotated 270 degrees clockwise
            
            #1way pice
            if "DOWN" in walls and "UP" in walls:
                return [TEX_WALL1WAY, 0] #Generic piece
            if "LEFT" in walls and "RIGHT" in walls:
                return [TEX_WALL1WAY, 90] #Rotated 90 degrees clockwise
            
            return []
        
        for y in range(len(labyrinth)):
            for x in range(len(labyrinth[0])):
                choice = random.randint(0,100)

                if labyrinth[y][x] == 1:
                    wallEntt = MyEntity(START[0] + x * LINEWIDTH, START[1] + y * LINEWIDTH, 0, LINEWIDTH, LINEWIDTH)

                    TEXDATA = getSupposedTex(labyrinth, [x,y])
                    if len(TEXDATA) == 2:
                        wallEntt.textureComp.setTexture(TEXDATA[0], size=(LINEWIDTH,LINEWIDTH), rotate=-TEXDATA[1])
                    elif len(TEXDATA) == 1:
                        wallEntt.textureComp.color = (200,200,0)
                    else:
                        wallEntt.textureComp.color = BGCOLOR
                    self.entities.append(wallEntt)

                if labyrinth[y][x] == 1:
                    wallEntt = MyEntity(START[0] + x * LINEWIDTH, START[1] + y * LINEWIDTH, 0, LINEWIDTH, LINEWIDTH)
                    self.entities.append(wallEntt)

                if choice >= 95 and labyrinth[y][x] == 0 and self.portalBlue == None:
                    
                    labyrinth[y][x] = "T1" #change value, dont interrupt with coins
                    self.portalBlue = MyEntity(START[0] + x * LINEWIDTH, START[1] + y * LINEWIDTH, 1, LINEWIDTH, LINEWIDTH)
                    self.portalBlue.getTextureComponent().color = (0, 0, 255) #blue
                    self.entities.append(self.portalBlue)

                if choice >= 95 and y > (len(labyrinth) * 0.80) and labyrinth[y][x] == 0 and self.portalOrange == None:

                    labyrinth[y][x] = "T1"
                    self.portalOrange = MyEntity(START[0] + x * LINEWIDTH, START[1] + y * LINEWIDTH, 1, LINEWIDTH, LINEWIDTH)
                    self.portalOrange.getTextureComponent().color = (255, 165, 0) #orange
                    self.entities.append(self.portalOrange)

        #playernum = 0

        #aBot = Agent(START[0] + (1-playernum) * LINEWIDTH + (WIDTH-2) * LINEWIDTH * playernum, START[1] + (1-playernum) * LINEWIDTH + (HEIGHT-2) * LINEWIDTH * playernum, 1, LINEWIDTH, LINEWIDTH, playerNumber=playernum, transport = tpSpots)
        aBot = self.setPlayer(self.gameInfo.playerAlgorithm[0], START, LINEWIDTH, WIDTH, HEIGHT, 0, tpSpots)
        
        #playernumB = 1

        #bBot = AgentEvo(START[0] + (1-playernumB) * LINEWIDTH + (WIDTH-2) * LINEWIDTH * playernumB, START[1] + (1-playernumB) * LINEWIDTH + (HEIGHT-2) * LINEWIDTH * playernumB, 1, LINEWIDTH, LINEWIDTH, playerNumber=playernumB, transport=tpSpots)
        bBot = self.setPlayer(self.gameInfo.playerAlgorithm[1], START, LINEWIDTH, WIDTH, HEIGHT, 1, tpSpots)

        self.coins = []
        #------Testing Tsp Solver
        
        coins = 0
        for y in range(len(labyrinth)):
            for x in range(len(labyrinth[0])):
                if random.randint(0,1000) >= 980 and labyrinth[y][x] == 0 and coins < 10:
                    coins += 1
                    bBot.anchorPoints.append((x,y))
                    aBot.anchorPoints.append((x,y))
                    entt = MyEntity(START[0] + x * LINEWIDTH, START[1] + y * LINEWIDTH, 0, LINEWIDTH, LINEWIDTH)
                    entt.textureComp.setTexture("Source/Game/Files/coin.png")
                    self.entities.append(entt)
                    self.coins.append(entt)
        #-----------------------
                    
        aBot.setup(labyrinth)
        self.entities.append(aBot)
        aBot.getTextureComponent().color = (255,0, 0)
        self.bot.append(aBot)
        self.end.append(aBot.getPosition())
                    
        bBot.setup(labyrinth)
        self.entities.append(bBot)
        bBot.getTextureComponent().color = (255,255, 0)
        self.bot.append(bBot)
        self.end.append(bBot.getPosition())

        playerLeft = MyEntity(50, 560)
        playerLeft.getTextureComponent().setTextureSet(self.setPlayerTexture(self.gameInfo.player[0]), (400,400))
        playerLeft.getTextureComponent().setFrameInterval(0.5)
        self.entities.append(playerLeft)

        playerRight = MyEntity(1470, 560)
        playerRight.getTextureComponent().setTextureSet(self.setPlayerTexture(self.gameInfo.player[1]), (400,400))
        playerRight.getTextureComponent().setFrameInterval(0.5)
        self.entities.append(playerRight)


#------------Setup-------------------------------
    
def customFunc(package : dict, gameInfo):
    
    bot = package["bot"]
    bot.tickMax = (0.000001) * 144 * 0.1
    bBot = package["bot2"]
    bBot.tickMax = (0.000001) * 144 * 0.1
    botPos = package["pos"]
    bBotPos = package["pos2"]

    botPlayScene = package["scene"]

    portalBlue = package["blue"]
    portalOrange = package["orange"]
    
    
    if botPos[0] != bot.getPosition()[0] or botPos[1] != bot.getPosition()[1]:
        elem = MyEntity(botPos.copy()[0], botPos.copy()[1], 0 ,bodyWidth=bot.bodyWidth, bodyHeight=bot.bodyHeight)
        
        elem.getTextureComponent().color = (0,100,255)
        botPlayScene.elements.append(elem)
        botPos = bot.getPosition().copy()
    
    if bBotPos[0] != bBot.getPosition()[0] or bBotPos[1] != bBot.getPosition()[1]:
        elem = MyEntity(bBotPos.copy()[0], bBotPos.copy()[1], 0 ,bodyWidth=bBot.bodyWidth, bodyHeight=bBot.bodyHeight)
        elem.getTextureComponent().color = (0, 255, 0)
        botPlayScene.elements.append(elem)
        bBotPos = bBot.getPosition().copy()


    return [botPos, bBotPos]


#------------------------------------------------

object = Tournament()
gameScene = None
botPackage = {}
background = pygame.image.load("Source/Game/Files/createBackground.png")
controllers = []

def setup(info, screen):

    global gameScene
    global botPackage
    
    object.gameInfo = info
    object.screen = screen
    gameScene = Scene(object.screen, object.entities, [], background)
    

def load():

    global gameScene
    global botPackage
    
    
    object.setupLab()
    bot = object.bot[0]
    bBot = object.bot[1]
    botPos = bot.getPosition().copy()
    bBotPos = bBot.getPosition().copy()
    portalBlue = object.portalBlue
    portalOrange = object.portalOrange
    botPackage = {"bot" : bot, "bot2" : bBot, "pos" : botPos, "pos2" : bBotPos, "scene" : gameScene, "blue" : portalBlue, "orange" : portalOrange}

    gameScene = Scene(object.screen, object.entities, [], background)

    return gameScene