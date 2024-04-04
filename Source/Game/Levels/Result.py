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
    gameInfo = None

    resultBackground = pygame.image.load("Source/Game/Files/menuBackground.png")

    gameResult = Label(1920//2, 440, 0, 1, 1, "Spielergebnis", (0, 110, 18), 70)
    gameResult.setTextRect()
    uiEntities.append(gameResult)
    
    mainMenu = Button(1920//2 - 150, 610, 0, 300, 50, "Hauptmenü", (0, 110, 18), 40)
    mainMenu.setTextRect()
    uiEntities.append(mainMenu)

    playerOne = Label(1920//4, 490, 0, 1, 1, "T", (0, 110, 18), 70)
    playerOne.setTextRect()
    uiEntities.append(playerOne)

    playerOCoins = Label(1920//4, 580, 0, 1, 1, "T", (0, 110, 18), 70)
    playerOCoins.setTextRect()
    uiEntities.append(playerOCoins) 

    playerTwo = Label((1920//4) * 3, 490, 0, 1, 1, "T", (0, 110, 18), 70)
    playerTwo.setTextRect()
    uiEntities.append(playerTwo)

    playerTCoins = Label((1920//4) * 3, 580, 0, 1, 1, "T", (0, 110, 18), 70)
    playerTCoins.setTextRect()
    uiEntities.append(playerTCoins) 

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
    object.gameInfo = info

    

def showResult(gameInfo):
    print(gameInfo)
    object.playerOne.setText(gameInfo.playerAlgorithm[0])
    object.playerTwo.setText(gameInfo.playerAlgorithm[1])
    object.playerOCoins.setText(gameInfo.points[0])
    object.playerTCoins.setText(gameInfo.points[1])