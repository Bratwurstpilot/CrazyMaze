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

    POneAlgorithm = Label(1920//4, 300, 0, 1, 1, "Wähle aus", (0, 110, 18), 70)
    POneAlgorithm.setTextRect()
    uiEntities.append(POneAlgorithm)

    PTwoAlgorithm = Label((1920//4)*3, 300, 0, 1, 1, "Wähle aus", (0, 110, 18), 70)
    PTwoAlgorithm.setTextRect()
    uiEntities.append(PTwoAlgorithm)

    startGame = Button(1920//2 - 150, 90, 0, 300, 50, "Spiel starten", (0, 110, 18), 40)
    startGame.setTextRect()
    uiEntities.append(startGame)
    
    backMenu = Button(1920//2 - 150, 160, 0, 300, 50, "Zurück", (0, 110, 18), 40)
    backMenu.setTextRect()
    uiEntities.append(backMenu)

    aStarOne = Button(1920//2 - 150, 210, 0, 150, 50, "A Star", (0, 110, 18), 40)
    aStarOne.setTextRect()
    uiEntities.append(aStarOne)

    dijkstraOne = Button(1920//2 - 150, 260, 0, 150, 50, "Dijkstra", (0, 110, 18), 40)
    dijkstraOne.setTextRect()
    uiEntities.append(dijkstraOne)
    
    aStarTwo = Button(1920//2, 210, 0, 150, 50, "A Star", (0, 110, 18), 40)
    aStarTwo.setTextRect()
    uiEntities.append(aStarTwo)

    dijkstraTwo = Button(1920//2, 260, 0, 150, 50, "Dijkstra", (0, 110, 18), 40)
    dijkstraTwo.setTextRect()
    uiEntities.append(dijkstraTwo)
