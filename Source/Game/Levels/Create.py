from __future__ import annotations
import pygame
import random


from Source.Engine.Animation import Animation
from Source.Engine.Label import Label
from Source.Engine.Button import Button
from Source.Engine.Scene import Scene


class Create:
    
    entities : list = []
    animations : list = []
    uiEntities : list = []

    createBackground = pygame.image.load("Source/Game/Files/createBackground.png")

    charSelection = Label(1920//2, 40, 0, 1, 1, "Spielerauswahl", (0, 110, 18), 70)
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

    startGame = Button(1520, 1000, 0, 300, 50, "Start", (0, 110, 18), 60)
    startGame.setTextRect()
    uiEntities.append(startGame)
    
    backMenu = Button(100, 1000, 0, 300, 50, "Zurück", (0, 110, 18), 60)
    backMenu.setTextRect()
    uiEntities.append(backMenu)

    #---------------------------------Mode------------------------------------

    mode = Button(1920//2 - 150, 900, 0, 300, 50, "Einzeln", (0, 110, 18), 40)
    mode.setTextRect()
    uiEntities.append(mode)

    switchLModus = Button((1920//2 - 250), 900, 0, 50, 50, "<<", (0,110,18), 40)
    switchLModus.setBgColor((67 ,181 ,207))
    switchLModus.setTextRect()
    uiEntities.append(switchLModus)
     
    switchRModus = Button((1920//2 + 200), 900, 0, 50, 50, ">>", (0,110,18), 40)
    switchRModus.setBgColor((67 ,181 ,207))
    switchRModus.setTextRect()
    uiEntities.append(switchRModus)

    #--------------------------------Round-------------------------------------
    round = Button(1920//2 - 150, 1000, 0, 300, 50, "10", (0, 110, 18), 40)
    round.setTextRect()
    uiEntities.append(round)

    switchL10 = Button((1920//2 - 250), 1000, 0, 50, 50, "<<", (0,110,18), 40)
    switchL10.setBgColor((67 ,181 ,207))
    switchL10.setTextRect()
    uiEntities.append(switchL10)
     
    switchR10 = Button((1920//2 + 200), 1000, 0, 50, 50, ">>", (0,110,18), 40)
    switchR10.setBgColor((67 ,181 ,207))
    switchR10.setTextRect()
    uiEntities.append(switchR10)
    
    switchL50 = Button((1920//2 - 310), 1000, 0, 50, 50, "<<", (0,110,18), 40)
    switchL50.setBgColor((67 ,181 ,207))
    switchL50.setTextRect()
    uiEntities.append(switchL50)
     
    switchR50 = Button((1920//2 + 260), 1000, 0, 50, 50, ">>", (0,110,18), 40)
    switchR50.setBgColor((67 ,181 ,207))
    switchR50.setTextRect()
    uiEntities.append(switchR50)

    switchL100 = Button((1920//2 - 370), 1000, 0, 50, 50, "<<", (0,110,18), 40)
    switchL100.setBgColor((67 ,181 ,207))
    switchL100.setTextRect()
    uiEntities.append(switchL100)
     
    switchR100 = Button((1920//2 + 320), 1000, 0, 50, 50, ">>", (0,110,18), 40)
    switchR100.setBgColor((67 ,181 ,207))
    switchR100.setTextRect()
    uiEntities.append(switchR100)
    #---------------------------------Player One------------------------------------
    playerOne = Label(1920//4, 200, 0, 1, 1, "Spieler 1", (0, 110, 18), 70)
    playerOne.setTextRect()
    uiEntities.append(playerOne)

    pOneAlgorithm = Label(1920//4, 755, 0, 1, 1, "A Star", (0, 110, 18), 40)
    pOneAlgorithm.setTextRect()
    uiEntities.append(pOneAlgorithm)

    switchLOneAlgorithm = Button((1920//16)*3 - 40, 740, 0, 50, 40, "<<", (0,110,18), 40)
    switchLOneAlgorithm.setBgColor((67 ,181 ,207))
    switchLOneAlgorithm.setTextRect()
    uiEntities.append(switchLOneAlgorithm)
     
    switchROneAlgorithm = Button((1920//16)*5, 740, 0, 50, 40, ">>", (0,110,18), 40)
    switchROneAlgorithm.setBgColor((67 ,181 ,207))
    switchROneAlgorithm.setTextRect()
    uiEntities.append(switchROneAlgorithm)

    pOneDifficulty = Label(1920//4, 855, 0, 1, 1, "Einfach", (0, 110, 18), 40)
    pOneDifficulty.setTextRect()
    uiEntities.append(pOneDifficulty)

    switchLOneDifficulty = Button((1920//16)*3 - 40, 840, 0, 50, 40, "<<", (0,110,18), 40)
    switchLOneDifficulty.setBgColor((114 ,194 ,203))
    switchLOneDifficulty.setTextRect()
    uiEntities.append(switchLOneDifficulty)
    
    switchROneDifficulty = Button((1920//16)*5, 840, 0, 50, 40, ">>", (0,110,18), 40)
    switchROneDifficulty.setBgColor((114 ,194 ,203))
    switchROneDifficulty.setTextRect()
    uiEntities.append(switchROneDifficulty)

    #---------------------------------Player Two------------------------------------
    playerTwo = Label((1920//4)*3, 200, 0, 1, 1, "Spieler 2", (0, 110, 18), 70)
    playerTwo.setTextRect()
    uiEntities.append(playerTwo)

    pTwoAlgorithm = Label((1920//4)*3, 755, 0, 1, 1, "A Star", (0, 110, 18), 40)
    pTwoAlgorithm.setTextRect()
    uiEntities.append(pTwoAlgorithm)

    switchLTwoAlgorithm = Button((1920//16)*11 - 40, 740, 0, 50, 40, "<<", (0,110,18), 40)
    switchLTwoAlgorithm.setTextRect()
    uiEntities.append(switchLTwoAlgorithm)
    
    switchRTwoAlgorithm = Button((1920//16)*13, 740, 0, 50, 40, ">>", (0,110,18), 40)
    switchRTwoAlgorithm.setTextRect()
    uiEntities.append(switchRTwoAlgorithm)

    pTwoDifficulty = Label((1920//4)*3, 855, 0, 1, 1, "Einfach", (0, 110, 18), 40)
    pTwoDifficulty.setTextRect()
    uiEntities.append(pTwoDifficulty)

    switchLTwoDifficulty = Button((1920//16)*11 - 40, 840, 0, 50, 40, "<<", (0,110,18), 40)
    switchLTwoDifficulty.setTextRect()
    uiEntities.append(switchLTwoDifficulty)
    
    switchRTwoDifficulty = Button((1920//16)*13, 840, 0, 50, 40, ">>", (0,110,18), 40)
    switchRTwoDifficulty.setTextRect()
    uiEntities.append(switchRTwoDifficulty)

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

    def updateAlgorithm(info, cgame, state, player) -> None:

        info.setPlayerAlgorithm(state,player)
        cgame.setText(info.playerAlgorithm[player])


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
    object.switchLOneAlgorithm.setParam([[gameInfo, object.pOneAlgorithm, -1, 0]])

    object.switchROneAlgorithm.setFunc([updateAlgorithm])
    object.switchROneAlgorithm.setParam([[gameInfo, object.pOneAlgorithm, 1, 0]])

    object.switchLOneDifficulty.setFunc([updateDiffictuly])
    object.switchLOneDifficulty.setParam([[gameInfo, object.pOneDifficulty, -1, 0]])

    object.switchROneDifficulty.setFunc([updateDiffictuly])
    object.switchROneDifficulty.setParam([[gameInfo, object.pOneDifficulty, 1, 0]])

    #----------------------------Switch Player Two----------------------------
    object.switchLTwoAlgorithm.setFunc([updateAlgorithm])
    object.switchLTwoAlgorithm.setParam([[gameInfo, object.pTwoAlgorithm, -1, 1]])

    object.switchRTwoAlgorithm.setFunc([updateAlgorithm])
    object.switchRTwoAlgorithm.setParam([[gameInfo, object.pTwoAlgorithm, 1, 1]])

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