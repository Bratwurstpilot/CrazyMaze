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
    delegate = 0

    createBackground = pygame.image.load("Source/Game/Files/createBackground.png")

    gameTitle = Label(1920//2, 40, 0, 1, 1, "Crazy Maze", (0, 110, 18), 70)
    gameTitle.setTextRect()
    uiEntities.append(gameTitle)

    algorithmChoice = Label(1920//2, 205, 0, 1, 1, "Algorithmus", (0, 110, 18), 50)
    algorithmChoice.setTextRect()
    uiEntities.append(algorithmChoice)

    difficulty = Label(1920//2, 305, 0, 1, 1, "Schwierigkeitsgrad", (0, 110, 18), 50)
    difficulty.setTextRect()
    uiEntities.append(difficulty)

    startGame = Button(1920//2 - 150, 740, 0, 300, 50, "Spiel starten", (0, 110, 18), 40)
    startGame.setTextRect()
    uiEntities.append(startGame)
    
    backMenu = Button(1920//2 - 150, 800, 0, 300, 50, "Zurück", (0, 110, 18), 40)
    backMenu.setTextRect()
    uiEntities.append(backMenu)

    tournament = Button(1920//2 - 250, 500, 0, 500, 50, "Tournament (10 Runden)", (0, 110, 18), 40)
    tournament.setTextRect()
    uiEntities.append(tournament)

    #---------------------------------Player One------------------------------------
    playerOne = Label(1920//4, 100, 0, 1, 1, "Spieler 1", (0, 110, 18), 70)
    playerOne.setTextRect()
    uiEntities.append(playerOne)

    pOneAlgorithm = Label(1920//4, 205, 0, 1, 1, "Manuell", (0, 110, 18), 40)
    pOneAlgorithm.setTextRect()
    uiEntities.append(pOneAlgorithm)

    switchLOneAlgorithm = Button((1920//16)*3 - 40, 190, 0, 50, 40, "<<", (0,110,18), 40)
    switchLOneAlgorithm.setBgColor((67 ,181 ,207))
    switchLOneAlgorithm.setTextRect()
    uiEntities.append(switchLOneAlgorithm)
     
    switchROneAlgorithm = Button((1920//16)*5, 190, 0, 50, 40, ">>", (0,110,18), 40)
    switchROneAlgorithm.setBgColor((67 ,181 ,207))
    switchROneAlgorithm.setTextRect()
    uiEntities.append(switchROneAlgorithm)

    pOneDifficulty = Label(1920//4, 305, 0, 1, 1, "Einfach", (0, 110, 18), 40)
    pOneDifficulty.setTextRect()
    uiEntities.append(pOneDifficulty)

    switchLOneDifficulty = Button((1920//16)*3 - 40, 290, 0, 50, 40, "<<", (0,110,18), 40)
    switchLOneDifficulty.setBgColor((114 ,194 ,203))
    switchLOneDifficulty.setTextRect()
    uiEntities.append(switchLOneDifficulty)
    
    switchROneDifficulty = Button((1920//16)*5, 290, 0, 50, 40, ">>", (0,110,18), 40)
    switchROneDifficulty.setBgColor((114 ,194 ,203))
    switchROneDifficulty.setTextRect()
    uiEntities.append(switchROneDifficulty)

    #---------------------------------Player Two------------------------------------
    playerTwo = Label((1920//4)*3, 100, 0, 1, 1, "Spieler 2", (0, 110, 18), 70)
    playerTwo.setTextRect()
    uiEntities.append(playerTwo)

    pTwoAlgorithm = Label((1920//4)*3, 205, 0, 1, 1, "Manuell", (0, 110, 18), 40)
    pTwoAlgorithm.setTextRect()
    uiEntities.append(pTwoAlgorithm)

    switchLTwoAlgorithm = Button((1920//16)*11 - 40, 190, 0, 50, 40, "<<", (0,110,18), 40)
    switchLTwoAlgorithm.setTextRect()
    uiEntities.append(switchLTwoAlgorithm)
    
    switchRTwoAlgorithm = Button((1920//16)*13, 190, 0, 50, 40, ">>", (0,110,18), 40)
    switchRTwoAlgorithm.setTextRect()
    uiEntities.append(switchRTwoAlgorithm)

    pTwoDifficulty = Label((1920//4)*3, 305, 0, 1, 1, "Einfach", (0, 110, 18), 40)
    pTwoDifficulty.setTextRect()
    uiEntities.append(pTwoDifficulty)

    switchLTwoDifficulty = Button((1920//16)*11 - 40, 290, 0, 50, 40, "<<", (0,110,18), 40)
    switchLTwoDifficulty.setTextRect()
    uiEntities.append(switchLTwoDifficulty)
    
    switchRTwoDifficulty = Button((1920//16)*13, 290, 0, 50, 40, ">>", (0,110,18), 40)
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

    def updateAlgorithm(instance, cgame, state, player) -> None:

        instance.setPlayerAlgorithm(state,player)
        cgame.setText(instance.playerAlgorithm[player])


    def updateDiffictuly(instance, cgame, state, player) -> None:

        instance.setBotDifficulty(state,player)
        cgame.setText(instance.difficulty[player])

    

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

    #---------------------------------------------------------------------------
    object.startGame.setFunc([gameDelegate.setScene])
    object.startGame.setParam([[2]])