from __future__ import annotations
import pygame
import random

from Source.Engine.Scene import Scene
from Source.Engine.Sound import Music
from Source.Engine.Animation import Animation
from Source.Engine.Label import Label
from Source.Engine.Button import Button
from Source.Game.Util import MyEntity, MyController, MyController2

class Menu:
    
    entities : list = []
    animations : list = []
    uiEntities : list = []
    delegate = 0
    param = 0

    menuBackground = pygame.image.load("Source/Game/Files/menuBackground.png")

    gameTitle = Label(1920//2, 440, 0, 1, 1, "Crazy Maze", (0, 110, 18), 70)
    gameTitle.setTextRect()
    uiEntities.append(gameTitle)

    startGame = Button(1920//2 - 150, 490, 0, 300, 50, "Spiel erstellen", (0, 110, 18), 40)
    startGame.setTextRect()
    uiEntities.append(startGame)
    
    quitGame = Button(1920//2 - 150, 610, 0, 300, 50, "Beenden", (0, 110, 18), 40)
    quitGame.setTextRect()
    uiEntities.append(quitGame)

    pygame.init()
    mainMenu = Music("Source/Game/Files/ThemeMainMenu.wav", 0.1)
    mainMenu.play()


#------Setup Part----------

object = Menu()
gameScene = None

def setup(screen):
    
    global gameScene
    gameScene = Scene(screen, object.entities, object.uiEntities, object.background)

