from __future__ import annotations
import pygame
import random


from Source.Engine.Sound import Music
from Source.Engine.Animation import Animation
from Source.Engine.Label import Label
from Source.Engine.Button import Button
from Source.Game.Util import MyEntity, MyController, MyController2

class Create:
    
    entities : list = []
    animations : list = []
    uiEntities : list = []

    background = pygame.image.load("Source/Game/Files/MainBackground.png")

    gameTitle = Label(1920//2, 440, 0, 1, 1, "Crazy Maze", (0, 110, 18), 70)
    gameTitle.setTextRect()
    uiEntities.append(gameTitle)

    startGame = Button(1920//2 - 150, 490, 0, 300, 50, "Spiel starten", (0, 110, 18), 40)
    startGame.setTextRect()
    
    uiEntities.append(startGame)
    
    #options = Button(1920//2 - 150, 550, 0, 300, 50, "Optionen", (0, 110, 18), 40)
    #options.setTextRect()
    #uiEntities.append(options)
    
    backMenu = Button(1920//2 - 150, 610, 0, 300, 50, "Zurück", (0, 110, 18), 40)
    backMenu.setTextRect()
    uiEntities.append(backMenu)

    #pygame.init()
    #mainMenu = Music("Source/Game/Files/ThemeMainMenu.wav", 0.1)
    #mainMenu.play()