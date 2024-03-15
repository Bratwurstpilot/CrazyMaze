import pygame

from Source.Engine.Sound import Music
from Source.Engine.Animation import Animation
from Source.Engine.Label import Label
from Source.Engine.Button import Button
from Source.Engine.Scene import Scene


class Result:
    
    entities : list = []
    animations : list = []
    uiEntities : list = []
    delegate = 0

    resultBackground = pygame.image.load("Source/Game/Files/menuBackground.png")
"""
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
    mainMenu = Music("Source/Game/Files/DriftveilCity.wav", 0.1)
    #mainMenu.play()
"""


#------Setup Part----------

##menuScene = Scene(screen, menu.entities, menu.uiEntities, menu.menuBackground)
object = Result()
gameScene = None
gameDelegate = None
gameInfo = None

def setup(screen, delegate, info):

    global gameDelegate
    global gameScene
    global gameInfo
    
    gameScene = Scene(screen, object.entities, object.uiEntities, object.resultBackground)
    gameDelegate = delegate
    gameInfo = info
    