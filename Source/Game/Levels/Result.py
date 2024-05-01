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

    resultBackground = pygame.transform.scale(pygame.image.load("Source/Game/Files/menuBackground.png"), (1920,1080))

    gameResult = Label(1920//2, 665, 0, 1, 1, "Spielergebnis", (255, 255, 255), 50)
    gameResult.setTextRect()
    uiEntities.append(gameResult)
    
    mainMenu = Button(1920//2 - 150, 1010, 0, 300, 50, "Hauptmenü", (255, 255, 255), 40)
    mainMenu.setBgColor((2, 29, 50))
    mainMenu.setTextRect()
    uiEntities.append(mainMenu)

    playerOne = Label(1920//4, 730, 0, 1, 1, "T", (255, 255, 255), 40)
    playerOne.setTextRect()
    uiEntities.append(playerOne)

    playerOCoins = Label(1920//4, 820, 0, 1, 1, "T", (255, 255, 255), 40)
    playerOCoins.setTextRect()
    uiEntities.append(playerOCoins) 

    playerTwo = Label((1920//4) * 3, 730, 0, 1, 1, "T", (255, 255, 255), 40)
    playerTwo.setTextRect()
    uiEntities.append(playerTwo)

    playerTCoins = Label((1920//4) * 3, 820, 0, 1, 1, "T", (255, 255, 255), 40)
    playerTCoins.setTextRect()
    uiEntities.append(playerTCoins)

    winner = Label((1920//2), 800, 0, 1, 1, "T", (255, 255, 255), 40)
    winner.setBgColor((2, 29, 50))
    winner.setTextRect()
    uiEntities.append(winner)
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

    #-------------------------Main Menu-----------------------------------------
    object.mainMenu.setFunc([delegate.reset])
    object.mainMenu.setParam([[info]])
    #---------------------------------------------------------------------------


    
def showResult(gameInfo):
    
    object.playerOne.setText(gameInfo.playerAlgorithm[0])
    object.playerTwo.setText(gameInfo.playerAlgorithm[1])
    object.playerOCoins.setText(gameInfo.coins[0])
    object.playerTCoins.setText(gameInfo.coins[1])
    if gameInfo.coins[0] == gameInfo.coins[1]:
        object.winner.setText("Unentschieden")
    else:
        win = gameInfo.coins.index(max(gameInfo.coins))
        object.winner.setText(str(gameInfo.playerAlgorithm[win]) + " " + str(win + 1) + " hat gewonnen!")