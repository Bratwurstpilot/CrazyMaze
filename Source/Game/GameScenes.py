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
mainMenu.startGame.setParam([[createScene]])

mainMenu.quitGame.setFunc([stateDelegate.setRunning])
mainMenu.quitGame.setParam([[False]])

createGame.backMenu.setFunc([stateDelegate.setScene])
createGame.backMenu.setParam([[menuScene]])

def update(instance, cgame, state, player) -> None:

    instance.setPlayerOne(state,player)
    cgame.setText(instance.playerAlgorithm[player])

#----------------------------Switch Algorithm Player One----------------------------
createGame.switchLeftOne.setFunc([update])
createGame.switchLeftOne.setParam([[gameInstance, createGame.pOneAlgorithm, -1, 0]])

createGame.switchRightOne.setFunc([update])
createGame.switchRightOne.setParam([[gameInstance, createGame.pOneAlgorithm, 1, 0]])

#----------------------------Switch Algorithm Player Two----------------------------
createGame.switchLeftTwo.setFunc([update])
createGame.switchLeftTwo.setParam([[gameInstance, createGame.pTwoAlgorithm, -1, 1]])

createGame.switchRightTwo.setFunc([update])
createGame.switchRightTwo.setParam([[gameInstance, createGame.pTwoAlgorithm, 1, 1]])



