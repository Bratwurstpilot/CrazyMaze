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

def updateAlgorithm(instance, cgame, state, player) -> None:

    instance.setPlayerAlgorithm(state,player)
    cgame.setText(instance.playerAlgorithm[player])


def updateDiffictuly(instance, cgame, state, player) -> None:

    instance.setBotDifficulty(state,player)
    cgame.setText(instance.difficulty[player])

#----------------------------Switch Player One----------------------------
createGame.switchLOneAlgorithm.setFunc([updateAlgorithm])
createGame.switchLOneAlgorithm.setParam([[gameInstance, createGame.pOneAlgorithm, -1, 0]])

createGame.switchROneAlgorithm.setFunc([updateAlgorithm])
createGame.switchROneAlgorithm.setParam([[gameInstance, createGame.pOneAlgorithm, 1, 0]])

createGame.switchLOneDifficulty.setFunc([updateDiffictuly])
createGame.switchLOneDifficulty.setParam([[gameInstance, createGame.pOneDifficulty, -1, 0]])

createGame.switchROneDifficulty.setFunc([updateDiffictuly])
createGame.switchROneDifficulty.setParam([[gameInstance, createGame.pOneDifficulty, 1, 0]])

#----------------------------Switch Player Two----------------------------
createGame.switchLTwoAlgorithm.setFunc([updateAlgorithm])
createGame.switchLTwoAlgorithm.setParam([[gameInstance, createGame.pTwoAlgorithm, -1, 1]])

createGame.switchRTwoAlgorithm.setFunc([updateAlgorithm])
createGame.switchRTwoAlgorithm.setParam([[gameInstance, createGame.pTwoAlgorithm, 1, 1]])

createGame.switchLTwoDifficulty.setFunc([updateDiffictuly])
createGame.switchLTwoDifficulty.setParam([[gameInstance, createGame.pTwoDifficulty, -1, 0]])

createGame.switchRTwoDifficulty.setFunc([updateDiffictuly])
createGame.switchRTwoDifficulty.setParam([[gameInstance, createGame.pTwoDifficulty, 1, 0]])