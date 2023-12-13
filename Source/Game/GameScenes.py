import pygame

from Source.Game.Menu import Menu
from Source.Game.Create2 import Create
from Source.Game.Delegate import GameDelegate
from Source.Game.GameInstance import Instance
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
gameInstance = Instance()

mainMenu.startGame.setFunc([stateDelegate.setScene])
mainMenu.startGame.setParam([createScene])

mainMenu.quitGame.setFunc([stateDelegate.setRunning])
mainMenu.quitGame.setParam([False])

createGame.backMenu.setFunc([stateDelegate.setScene])
createGame.backMenu.setParam([menuScene])

createGame.switchLeftOne.setFunc([createGame.pOneAlgorithm.setText])
createGame.switchLeftOne.setParam([gameInstance.setPlayerOne(-1)])

createGame.switchRightOne.setFunc([createGame.pOneAlgorithm.setText])
createGame.switchRightOne.setParam([gameInstance.setPlayerOne(1)])
"""
createGame.aStarOne.setFunc([gameInstance.setPlayerOne, createGame.POneAlgorithm.setText])
createGame.aStarOne.setParam(["A Star", "A Star"])

createGame.aStarTwo.setFunc([gameInstance.setPlayerTwo, createGame.PTwoAlgorithm.setText])
createGame.aStarTwo.setParam(["A Star", "A Star"])

createGame.dijkstraOne.setFunc([gameInstance.setPlayerOne, createGame.POneAlgorithm.setText])
createGame.dijkstraOne.setParam(["Djikstra", "Djikstra"])

createGame.dijkstraTwo.setFunc([gameInstance.setPlayerTwo, createGame.PTwoAlgorithm.setText])
createGame.dijkstraTwo.setParam(["Djikstra", "Djikstra"])

"""
