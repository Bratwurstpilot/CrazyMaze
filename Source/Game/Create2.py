from __future__ import annotations
import pygame
import random


from Source.Engine.Sound import Music
from Source.Engine.Animation import Animation
from Source.Engine.Label import Label
from Source.Engine.Button import Button
from Source.Game.Util import MyEntity, MyController, MyController2
from Source.Game.GameInstance import Instance

class Create:
    
    entities : list = []
    animations : list = []
    uiEntities : list = []

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
    
