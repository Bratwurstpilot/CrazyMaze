from __future__ import annotations
import pygame
import random


from Source.Engine.Animation import Animation
from Source.Engine.Label import Label
from Source.Engine.Button import Button
from Source.Engine.Scene import Scene

from Source.Game.Util import MyEntity

class Create:
    
    entities : list = []
    animations : list = []
    uiEntities : list = []

    createBackground = pygame.transform.scale(pygame.image.load("Source/Game/Files/SelectionScreen.png"), (1920,1080))

    charSelection = Label(0, 0, 0, 1920, 100, "Spielerauswahl", (255,255,255), 70)
    charSelection.setBgColor((0,0,0))
    charSelection.setTextRect()
    uiEntities.append(charSelection)
    
    """
    algorithmChoice = Label(1920//2, 205, 0, 1, 1, "Algorithmus", (0, 110, 18), 50)
    algorithmChoice.setTextRect()
    uiEntities.append(algorithmChoice)

    difficulty = Label(1920//2, 305, 0, 1, 1, "Schwierigkeitsgrad", (0, 110, 18), 50)
    difficulty.setTextRect()
    uiEntities.append(difficulty)
    """

    startBG = Label(1518, 998, 0, 304, 54, "", (0,204,0), 40)
    startBG.setBgColor((0,204,0))
    startBG.setTextRect()
    uiEntities.append(startBG)

    startGame = Button(1520, 1000, 0, 300, 50, "Start", (0, 204, 0), 40)
    startGame.setBgColor((20,20,20))
    startGame.setTextRect()
    uiEntities.append(startGame)

    backBG = Label(98, 998, 0, 304, 54, "", (204,0,0), 40)
    backBG.setBgColor((204,0,0))
    backBG.setTextRect()
    uiEntities.append(backBG)
    
    backMenu = Button(100, 1000, 0, 300, 50, "Zurück", (204,0,0), 40)
    backMenu.setBgColor((20,20,20))
    backMenu.setTextRect()
    uiEntities.append(backMenu)

    #---------------------------------Mode------------------------------------

    mode = Label(1920//2 - 150, 900, 0, 300, 50, "Einzeln", (0,0,0), 40)
    mode.setBgColor((255,255,255))
    mode.setTextRect()
    uiEntities.append(mode)

    switchLModus = Button((1920//2 - 200), 900, 0, 50, 50, "<", (255,255,255), 40)
    switchLModus.setBgColor((50,50,50))
    switchLModus.setTextRect()
    uiEntities.append(switchLModus)
     
    switchRModus = Button((1920//2 + 150), 900, 0, 50, 50, ">", (255,255,255), 40)
    switchRModus.setBgColor((50,50,50))
    switchRModus.setTextRect()
    uiEntities.append(switchRModus)

    #--------------------------------Round-------------------------------------
    round = Label(1920//2 - 75, 1000, 0, 150, 50, "10", (0,0,0), 40)
    round.setBgColor((255,255,255))
    round.setTextRect()
    uiEntities.append(round)

    switchL10 = Button((1920//2 - 125), 1000, 0, 50, 50, "<", (255,255,255), 30)
    switchL10.setBgColor((50,50,50))
    switchL10.setTextRect()
    uiEntities.append(switchL10)
     
    switchR10 = Button((1920//2 + 75), 1000, 0, 50, 50, ">", (255,255,255), 30)
    switchR10.setBgColor((50,50,50))
    switchR10.setTextRect()
    uiEntities.append(switchR10)
    
    switchL50 = Button((1920//2 - 175), 1000, 0, 50, 50, "<<", (255,255,255), 30)
    switchL50.setBgColor((50,50,50))
    switchL50.setTextRect()
    uiEntities.append(switchL50)
     
    switchR50 = Button((1920//2 + 125), 1000, 0, 50, 50, ">>", (255,255,255), 30)
    switchR50.setBgColor((50,50,50))
    switchR50.setTextRect()
    uiEntities.append(switchR50)

    switchL100 = Button((1920//2 - 265), 1000, 0, 90, 50, "<<<", (255,255,255), 30)
    switchL100.setBgColor((50,50,50))
    switchL100.setTextRect()
    uiEntities.append(switchL100)
     
    switchR100 = Button((1920//2 + 175), 1000, 0, 90, 50, ">>>", (255,255,255), 30)
    switchR100.setBgColor((50,50,50))
    switchR100.setTextRect()
    uiEntities.append(switchR100)
    #---------------------------------Player One------------------------------------
    #playerOne = Label(1920//4, 200, 0, 1, 1, "Spieler 1", (0, 110, 18), 70)
    #playerOne.setTextRect()
    #uiEntities.append(playerOne)

    pOneAlgorithm = Label(1920//4 - 16, 775, 0, 1, 1, "Spieler", (0, 255, 255), 40)
    pOneAlgorithm.setTextRect()
    uiEntities.append(pOneAlgorithm)

    switchLOneAlgorithm = Button((1920//16)*3 - 58, 760, 0, 50, 40, "<", (0,255,255), 40)
    switchLOneAlgorithm.setBgColor((50,50,50))
    switchLOneAlgorithm.setTextRect()
    uiEntities.append(switchLOneAlgorithm)
     
    switchROneAlgorithm = Button((1920//16)*5 - 15, 760, 0, 50, 40, ">", (0,255,255), 40)
    switchROneAlgorithm.setBgColor((50,50,50))
    switchROneAlgorithm.setTextRect()
    uiEntities.append(switchROneAlgorithm)

    pOneDifficulty = Label(1920//4 - 16, 855, 0, 1, 1, "Einfach", (0,255,255), 40)
    pOneDifficulty.setTextRect()
    uiEntities.append(pOneDifficulty)

    switchLOneDifficulty = Button((1920//16)*3 - 58, 840, 0, 50, 40, "<", (0,255,255), 40)
    switchLOneDifficulty.setBgColor((50,50,50))
    switchLOneDifficulty.setTextRect()
    uiEntities.append(switchLOneDifficulty)
    
    switchROneDifficulty = Button((1920//16)*5 - 15, 840, 0, 50, 40, ">", (0,255,255), 40)
    switchROneDifficulty.setBgColor((50,50,50))
    switchROneDifficulty.setTextRect()
    uiEntities.append(switchROneDifficulty)

    #---------------------------------Player Two------------------------------------
    #playerTwo = Label((1920//4)*3, 200, 0, 1, 1, "Spieler 2", (0, 110, 18), 70)
    #playerTwo.setTextRect()
    #uiEntities.append(playerTwo)

    pTwoAlgorithm = Label((1920//4)*3 + 16, 775, 0, 1, 1, "Spieler", (0, 255, 255), 40)
    pTwoAlgorithm.setTextRect()
    uiEntities.append(pTwoAlgorithm)

    switchLTwoAlgorithm = Button((1920//16)*11 - 22, 760, 0, 50, 40, "<", (0, 255, 255), 40)
    switchLTwoAlgorithm.setBgColor((50,50,50))
    switchLTwoAlgorithm.setTextRect()
    uiEntities.append(switchLTwoAlgorithm)
    
    switchRTwoAlgorithm = Button((1920//16)*13 + 15, 760, 0, 50, 40, ">", (0, 255, 255), 40)
    switchRTwoAlgorithm.setBgColor((50,50,50))
    switchRTwoAlgorithm.setTextRect()
    uiEntities.append(switchRTwoAlgorithm)

    pTwoDifficulty = Label((1920//4)*3 + 16, 855, 0, 1, 1, "Einfach", (0, 255, 255), 40)
    pTwoDifficulty.setTextRect()
    uiEntities.append(pTwoDifficulty)

    switchLTwoDifficulty = Button((1920//16)*11 - 22, 840, 0, 50, 40, "<", (0, 255, 255), 40)
    switchLTwoDifficulty.setBgColor((50,50,50))
    switchLTwoDifficulty.setTextRect()
    uiEntities.append(switchLTwoDifficulty)
    
    switchRTwoDifficulty = Button((1920//16)*13 + 15, 840, 0, 50, 40, ">", (0, 255, 255), 40)
    switchRTwoDifficulty.setBgColor((50,50,50))
    switchRTwoDifficulty.setTextRect()
    uiEntities.append(switchRTwoDifficulty)

    playerLeft = MyEntity(230, 260)
    playerLeft.getTextureComponent().setTextureSet(["Source/Game/Files/KnightSprite1.png", "Source/Game/Files/KnightSprite2.png"], (500,500))
    playerLeft.getTextureComponent().setFrameInterval(0.2)
    entities.append(playerLeft)

    playerRight = MyEntity(1190, 260)
    playerRight.getTextureComponent().setTextureSet(["Source/Game/Files/KnightSprite1.png", "Source/Game/Files/KnightSprite2.png"], (500,500), reflectX=True)
    playerRight.getTextureComponent().setFrameInterval(0.2)
    entities.append(playerRight)

object = Create()

gameScene = None
gameDelegate = None


def setup(screen, delegate, info):

    global gameDelegate
    global gameScene
    global gameInfo
    
    gameScene = Scene(screen, object.entities, object.uiEntities, object.createBackground)
    gameDelegate = delegate
    gameInfo = info

    object.backMenu.setFunc([gameDelegate.setScene])
    object.backMenu.setParam([[0]])

    def updateAlgorithm(info, cgame, state, player, object = None) -> None:

        info.setPlayerAlgorithm(state,player)
        cgame.setText(info.playerAlgorithm[player])

        if gameInfo.player[player] == 2:
            object.entities[-(player)].getTextureComponent().setTextureSet(["Source/Game/Files/Echse_1.png", "Source/Game/Files/Echse_2.png"], (450,450), reflectX=bool(player))
            object.entities[-(player)].positionX = 230 * (1-player) + 1240 * player
            object.entities[-(player)].positionY = 260

        elif gameInfo.player[player] == 1:
            object.entities[-(player)].getTextureComponent().setTextureSet(["Source/Game/Files/Robo1.png", "Source/Game/Files/Robo2.png"], (500,500), reflectX=bool(player))
            object.entities[-(player)].positionX = 260 * (1-player) + 1160 * player
            object.entities[-(player)].positionY = 230

        elif gameInfo.player[player] == 0:
            object.entities[-(player)].getTextureComponent().setTextureSet(["Source/Game/Files/KnightSprite1.png", "Source/Game/Files/KnightSprite2.png"], (450,450), reflectX=bool(player))
            object.entities[-(player)].positionX = 230 * (1-player) + 1240 * player
            object.entities[-(player)].positionY = 260


        '''
        Data for Knight:

        playerLeft = MyEntity(230, 260)
        playerLeft.getTextureComponent().setTextureSet(["Source/Game/Files/Robo1.png", "Source/Game/Files/Robo2.png"], (500,500))
        playerLeft.getTextureComponent().setFrameInterval(0.2)
        entities.append(playerLeft)

        playerRight = MyEntity(1190, 260)
        playerRight.getTextureComponent().setTextureSet(["Source/Game/Files/Robo1.png", "Source/Game/Files/Robo2.png"], (500,500), reflectX=True)
        playerRight.getTextureComponent().setFrameInterval(0.2)
        entities.append(playerRight)
        '''

    def updateDiffictuly(instance, cgame, state, player) -> None:

        info.setBotDifficulty(state,player)
        cgame.setText(info.difficulty[player])


    def updateMode(info, cgame, step) -> None:
        
        info.setMode(step)
        cgame.setText(info.mode[0])

    def updateMode(info, cgame, step) -> None:
    
        info.setMode(step)
        cgame.setText(info.mode[0])

    def updateRound(instance, cgame, step):

        instance.swiftRound(step)
        cgame.setText(str(instance.maxRounds))

    #----------------------------Switch Player One----------------------------
    object.switchLOneAlgorithm.setFunc([updateAlgorithm])
    object.switchLOneAlgorithm.setParam([[gameInfo, object.pOneAlgorithm, -1, 0, object]])

    object.switchROneAlgorithm.setFunc([updateAlgorithm])
    object.switchROneAlgorithm.setParam([[gameInfo, object.pOneAlgorithm, 1, 0, object]])

    object.switchLOneDifficulty.setFunc([updateDiffictuly])
    object.switchLOneDifficulty.setParam([[gameInfo, object.pOneDifficulty, -1, 0]])

    object.switchROneDifficulty.setFunc([updateDiffictuly])
    object.switchROneDifficulty.setParam([[gameInfo, object.pOneDifficulty, 1, 0]])

    #----------------------------Switch Player Two----------------------------
    object.switchLTwoAlgorithm.setFunc([updateAlgorithm])
    object.switchLTwoAlgorithm.setParam([[gameInfo, object.pTwoAlgorithm, -1, 1, object]])

    object.switchRTwoAlgorithm.setFunc([updateAlgorithm])
    object.switchRTwoAlgorithm.setParam([[gameInfo, object.pTwoAlgorithm, 1, 1, object]])

    object.switchLTwoDifficulty.setFunc([updateDiffictuly])
    object.switchLTwoDifficulty.setParam([[gameInfo, object.pTwoDifficulty, -1, 1]])

    object.switchRTwoDifficulty.setFunc([updateDiffictuly])
    object.switchRTwoDifficulty.setParam([[gameInfo, object.pTwoDifficulty, 1, 1]])

    #----------------------------Switch Mode-----------------------------------
    object.switchLModus.setFunc([updateMode])
    object.switchLModus.setParam([[gameInfo, object.mode, -1]])

    object.switchRModus.setFunc([updateMode])
    object.switchRModus.setParam([[gameInfo, object.mode, 1]])
    #---------------------------Switch Round-----------------------------------
    object.switchL10.setFunc([updateRound])
    object.switchL10.setParam([[gameDelegate, object.round, -10]])

    object.switchR10.setFunc([updateRound])
    object.switchR10.setParam([[gameDelegate, object.round, 10]])

    object.switchL50.setFunc([updateRound])
    object.switchL50.setParam([[gameDelegate, object.round, -50]])

    object.switchR50.setFunc([updateRound])
    object.switchR50.setParam([[gameDelegate, object.round, 50]])

    object.switchL100.setFunc([updateRound])
    object.switchL100.setParam([[gameDelegate, object.round, -100]])

    object.switchR100.setFunc([updateRound])
    object.switchR100.setParam([[gameDelegate, object.round, 100]])
    #----------------------------------------------------------------------------

    object.startGame.setFunc([gameDelegate.setGame, gameDelegate.setPlay, gameDelegate.setScene])
    object.startGame.setParam([[True], [True], [3]])


    #object.tournament.setFunc([gameDelegate.setGame, gameDelegate.setPlay, gameDelegate.setScene, gameDelegate.setTournament])
    #object.tournament.setParam([[True], [True], [2], [True, 10]])