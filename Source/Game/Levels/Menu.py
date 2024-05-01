import pygame

from Source.Engine.Sound import Music
from Source.Engine.Animation import Animation
from Source.Engine.Label import Label
from Source.Engine.Button import Button
from Source.Engine.Scene import Scene


class Menu:
    
    entities : list = []
    animations : list = []
    uiEntities : list = []
    delegate = 0

    #menuBackground = pygame.image.load("Source/Game/Files/menuBackground.png")
    menuBackground = pygame.transform.scale(pygame.image.load("Source/Game/Files/menuBackground.png"), (1920,1320))
  
    startGame = Button(1920//2 - 150, 870, 0, 300, 50, "Spiel erstellen", (235, 196,0), 30)
    startGame.setBgColor((20,20,20))
    startGame.setTextRect()
    uiEntities.append(startGame)
    
    quitGame = Button(1920//2 - 150, 950, 0, 300, 50, "Beenden", (235,196,0), 30)
    quitGame.setBgColor((20,20,20))
    quitGame.setTextRect()
    uiEntities.append(quitGame)

    pygame.init()
    mainMenu = Music("Source/Game/Files/DriftveilCity.wav", 0.1)
    #mainMenu.play()

#------Setup Part----------
 
object = Menu()
gameScene = None
gameDelegate = None

def setup(screen, delegate):

    global gameDelegate
    global gameScene
    
    gameScene = Scene(screen, object.entities, object.uiEntities, object.menuBackground)
    gameDelegate = delegate

    object.startGame.setFunc([gameDelegate.setScene])
    object.startGame.setParam([[1]])

    object.quitGame.setFunc([gameDelegate.setRunning])
    object.quitGame.setParam([[False]])