from __future__ import annotations
import pygame
import random


from Source.Engine.Animation import Animation
from Source.Engine.Label import Label
from Source.Engine.Button import Button
from Source.Engine.Scene import Scene
from Source.Engine.Screen import Screen
from Source.Game.GameInstance import Instance
from Source.Game.Main import stateDelegate


class Create:
    
    entities : list = []
    animations : list = []
    uiEntities : list = []
    delegate = 0

    def setup(object, screen : pygame.display, delegate) -> None:
        object.delegate = delegate
        return Scene(screen, object.entities, object.uiEntities, object.menuBackground)

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

infoObject = pygame.display.Info()
screen : pygame.display = Screen.setScreen(infoObject.current_w, infoObject.current_h, "")
create = Create()
createScene = Scene(screen, create.entities, create.uiEntities, create.createBackground)

create.backMenu.setFunc([stateDelegate.setScene])
create.backMenu.setParam([[-1]])

def updateAlgorithm(instance, cgame, state, player) -> None:

    instance.setPlayerAlgorithm(state,player)
    cgame.setText(instance.playerAlgorithm[player])


def updateDiffictuly(instance, cgame, state, player) -> None:

    instance.setBotDifficulty(state,player)
    cgame.setText(instance.difficulty[player])

gameInstance = Instance()

#----------------------------Switch Player One----------------------------
create.switchLOneAlgorithm.setFunc([updateAlgorithm])
create.switchLOneAlgorithm.setParam([[gameInstance, create.pOneAlgorithm, -1, 0]])

create.switchROneAlgorithm.setFunc([updateAlgorithm])
create.switchROneAlgorithm.setParam([[gameInstance, create.pOneAlgorithm, 1, 0]])

create.switchLOneDifficulty.setFunc([updateDiffictuly])
create.switchLOneDifficulty.setParam([[gameInstance, create.pOneDifficulty, -1, 0]])

create.switchROneDifficulty.setFunc([updateDiffictuly])
create.switchROneDifficulty.setParam([[gameInstance, create.pOneDifficulty, 1, 0]])

#----------------------------Switch Player Two----------------------------
create.switchLTwoAlgorithm.setFunc([updateAlgorithm])
create.switchLTwoAlgorithm.setParam([[gameInstance, create.pTwoAlgorithm, -1, 1]])

create.switchRTwoAlgorithm.setFunc([updateAlgorithm])
create.switchRTwoAlgorithm.setParam([[gameInstance, create.pTwoAlgorithm, 1, 1]])

create.switchLTwoDifficulty.setFunc([updateDiffictuly])
create.switchLTwoDifficulty.setParam([[gameInstance, create.pTwoDifficulty, -1, 0]])

create.switchRTwoDifficulty.setFunc([updateDiffictuly])
create.switchRTwoDifficulty.setParam([[gameInstance, create.pTwoDifficulty, 1, 0]])