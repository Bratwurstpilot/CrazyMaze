import pygame

from Source.Game.Menu import menu
from Source.Game.Create import create
from Source.Game.Delegate import GameDelegate
from Source.Game.GameInstance import Instance
import Source.Game.UtilFunction as UtilFunction

from Source.Engine.Scene import Scene
from Source.Engine.Screen import Screen

pygame.init()

infoObject = pygame.display.Info()
screen : pygame.display = Screen.setScreen(infoObject.current_w, infoObject.current_h, "")

def updateAlgorithm(instance, cgame, state, player) -> None:

    instance.setPlayerAlgorithm(state,player)
    cgame.setText(instance.playerAlgorithm[player])


def updateDiffictuly(instance, cgame, state, player) -> None:

    instance.setBotDifficulty(state,player)
    cgame.setText(instance.difficulty[player])

#----------------------------Create Scenes----------------------------
menuScene = Scene(screen, menu.entities, menu.uiEntities, menu.menuBackground)

createScene = Scene(screen, create.entities, create.uiEntities, create.createBackground)

stateDelegate = GameDelegate(menuScene, True)
gameInstance = Instance()

#----------------------------Set Functions and Params-------------------
menu.startGame.setFunc([stateDelegate.setScene])
menu.startGame.setParam([[createScene]])

menu.quitGame.setFunc([stateDelegate.setRunning])
menu.quitGame.setParam([[False]])

create.backMenu.setFunc([stateDelegate.setScene])
create.backMenu.setParam([[menuScene]])

#----------------------------Switch Player One----------------------------
create.switchLOneAlgorithm.setFunc([updateAlgorithm])
create.switchLOneAlgorithm.setParam([[gameInstance, create.pOneAlgorithm, -1, 0]])

create.switchROneAlgorithm.setFunc([updateAlgorithm])
create.switchROneAlgorithm.setParam([[gameInstance, create.pOneAlgorithm, 1, 0]])

create.switchLOneDifficulty.setFunc([updateDiffictuly])
create.switchLOneDifficulty.setParam([[gameInstance, create.pOneDifficulty, -1, 0]])

create.switchROneDifficulty.setFunc([updateDiffictuly])
create.switchROneDifficulty.setParam([[gameInstance, create.pOneDifficulty, 1, 0]])

#----------------------------Switch Player Two----------------------------
create.switchLTwoAlgorithm.setFunc([updateAlgorithm])
create.switchLTwoAlgorithm.setParam([[gameInstance, create.pTwoAlgorithm, -1, 1]])

create.switchRTwoAlgorithm.setFunc([updateAlgorithm])
create.switchRTwoAlgorithm.setParam([[gameInstance, create.pTwoAlgorithm, 1, 1]])

create.switchLTwoDifficulty.setFunc([updateDiffictuly])
create.switchLTwoDifficulty.setParam([[gameInstance, create.pTwoDifficulty, -1, 0]])

create.switchRTwoDifficulty.setFunc([updateDiffictuly])
create.switchRTwoDifficulty.setParam([[gameInstance, create.pTwoDifficulty, 1, 0]])