import pygame
import random

from Source.Engine.Sound import Music
from Source.Engine.Animation import Animation
from Source.Engine.Label import Label
from Source.Engine.Button import Button
from Source.Game.Util import MyEntity, MyController, MyController2

class Menu:

    entities : list = []
    animations : list = []
    uiEntities : list = []

    background = pygame.image.load("Source/Game/Files/MainBackground.png")

    gameTitle = Label(1920//2, 440, 0, 1, 1, "Crazy Maze", (0, 110, 18), 70)
    gameTitle.setRect()
    uiEntities.append(gameTitle)


    startGame = Button(1920//2, 540, 0, 1, 1, "Spiel erstellen", (0, 110, 18), 40)
    startGame.setRect()
    uiEntities.append(startGame)
    
    options = Button(1920//2, 640, 0, 1, 1, "Optionen", (0, 110, 18), 40)
    options.setRect()
    uiEntities.append(options)
    
    quitGame = Button(1920//2, 740, 0, 1, 1, "Beenden", (0, 110, 18), 40)
    quitGame.setRect()
    uiEntities.append(quitGame)
    pygame.init()
    mainMenu = Music("Source/Game/Files/ThemeMainMenu.wav", 0.1)
    mainMenu.play()
