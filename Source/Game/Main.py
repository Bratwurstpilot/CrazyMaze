import pygame

from Source.Engine.Scene import Scene
from Source.Engine.Animation import Animation
from Source.Engine.Sound import Music
from Source.Engine.Screen import Screen
from Source.Engine.Label import Label
from Source.Game.Delegate import GameDelegate
from Source.Game.GameInfo import GameInfo
from Source.Game.Levels import Menu
from Source.Game.Levels import Create
from Source.Game.Levels import LabTest
from Source.Game.Levels import KnightTest
from Source.Game.Levels import Tournament
from Source.Game.Levels import Result
from Source.Game.Util import MyEntity

def main():

    pygame.init()

    clock = pygame.time.Clock()
    animations : list = []
    screen : pygame.display = Screen.setScreen(1920, 1080, "")

    stateDelegate = GameDelegate(True)
    gameInfo = GameInfo()

    Menu.setup(screen, stateDelegate)
    Create.setup(screen, stateDelegate, gameInfo)
    Result.setup(screen, stateDelegate, gameInfo)

    LabTest.setup(gameInfo, screen)
    Tournament.setup(gameInfo, screen)

    instance = LabTest.object
    botPackage = LabTest.botPackage
    coins = instance.coins

    stateDelegate.setup([Menu.gameScene, Create.gameScene, Result.gameScene, LabTest.gameScene, Tournament.gameScene])

    while stateDelegate.running:
        
        if stateDelegate.play:
            
            if stateDelegate.game:

                stateDelegate.setGame(False)
                stateDelegate.setWin(False)
                
                stateDelegate.scenes.pop(3)
                stateDelegate.scenes.insert(3, LabTest.load())
                botPackage = LabTest.botPackage
                coins = instance.coins
                stateDelegate.setScene(3)

            func = LabTest.customFunc(botPackage, gameInfo)
                
            #Function call + param update || NOT OPTIMAL TODO
            botPackage = {"bot" : instance.bot[0], "bot2" : instance.bot[1], "pos" : func[0], "pos2" : func[1], "scene" : LabTest.gameScene, "blue" : instance.portalBlue , "orange" : instance.portalOrange }  
            
            if stateDelegate.checkWin(instance) and not stateDelegate.win:
                    
                    stateDelegate.setWin(True)
                    stateDelegate.setPlay(False)

                    gameInfo.addWin(instance)
                    Result.showResult()
                    stateDelegate.reset(screen, instance, LabTest, 3, gameInfo)
                    stateDelegate.setScene(2)

            #Algorithm Testing
            instance.bot[1].updateGameState(enemyPos = instance.bot[0].positionRelative, enemyPoints = gameInfo.coins[0], thisPoints = gameInfo.coins[1])
            instance.bot[0].updateGameState(enemyPos = instance.bot[1].positionRelative, enemyPoints = gameInfo.coins[1], thisPoints = gameInfo.coins[0])
        
            print(instance.bot[0].getPosition())
            #print(instance.bot[1].getPosition())
            for coin in coins:
                if coin.checkCollide(instance.bot[0]):
                    print("Bot 0 collected coin")
                    gameInfo.coins[0] += 1
                    instance.bot[1].signal("Coin", [coin.positionX, coin.positionY])
                    coins.remove(coin)
                    instance.entities.remove(coin)

                elif coin.checkCollide(instance.bot[1]):
                    print("Bot 1 collected coin")
                    gameInfo.coins[1] += 1
                    instance.bot[0].signal("Coin", [coin.positionX, coin.positionY])
                    coins.remove(coin)
                    instance.entities.remove(coin)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stateDelegate.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if not stateDelegate.tournament:
                        stateDelegate.reset(screen, instance, LabTest, 3, gameInfo)
                        botPackage = LabTest.botPackage
                        coins = instance.coins
                        gameInfo.coins = [0, 0]


        stateDelegate.update()
        stateDelegate.scene.render()
   
        for animation in animations:
            animation.update()

        clock.tick(144)

    pygame.quit()
