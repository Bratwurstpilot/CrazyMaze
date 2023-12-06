import pygame

from Source.Game.Menu import Menu
from Source.Game.Create import Create
from Source.Game.Delegate import GameDelegate
from Source.Engine.Scene import Scene
from Source.Engine.Screen import Screen

pygame.init()

infoObject = pygame.display.Info()
mainBackground = pygame.image.load("Source/Game/Files/MainBackground.png")
createBackground = pygame.image.load("Source/Game/Files/CreateBackground.png")
screen : pygame.display = Screen.setScreen(infoObject.current_w, infoObject.current_h, "")

mainMenu = Menu()
menuScene = Scene(screen, mainMenu.entities, mainMenu.uiEntities, mainBackground)

createGame = Create()
createScene = Scene(screen, createGame.entities, createGame.uiEntities, createBackground)

stateDelegate = GameDelegate(menuScene, True)

mainMenu.startGame.setFunc([stateDelegate.setScene])
mainMenu.startGame.setParam([createScene])

mainMenu.quitGame.setFunc([stateDelegate.setRunning])
mainMenu.quitGame.setParam([False])

createGame.backMenu.setFunc([stateDelegate.setScene])
createGame.backMenu.setParam([menuScene])