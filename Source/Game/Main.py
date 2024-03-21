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
    
    LabTest.setup(gameInfo, screen)
    Tournament.setup(gameInfo, screen)
    Menu.setup(screen, stateDelegate)
    Create.setup(screen, stateDelegate, gameInfo)
    Result.setup(screen, stateDelegate, gameInfo)
    
    instance = LabTest.object
    botPackage = LabTest.botPackage

    tournament = Tournament.object
    botPackage2 = Tournament.botPackage

    stateDelegate.setup([Menu.gameScene, Create.gameScene, Result.gameScene, LabTest.gameScene, Tournament.gameScene])
    
    coins = instance.coins
    

    while stateDelegate.running:

        if stateDelegate.tournament:
            

            if stateDelegate.game:
                Tournament.setup(gameInfo, screen)
                stateDelegate.scenes.insert(4,Tournament.load())
                stateDelegate.setScene(4)
                stateDelegate.setGame(False)
                stateDelegate.win = False
                coins = instance.coins
            
            
            if botPackage2:
                
                func = Tournament.customFunc(botPackage2, gameInfo)
                #Function call + param update || NOT OPTIMAL TODO
                botPackage2 = {"bot" : tournament.bot[0], "bot2" : tournament.bot[1], "pos" : func[0], "pos2" : func[1], "scene" : Tournament.gameScene, "blue" : tournament.portalBlue , "orange" : tournament.portalOrange }
                
            if stateDelegate.checkWin(tournament) and not stateDelegate.win:
                
                stateDelegate.win = True
                stateDelegate.setGame(True)
                gameInfo.addWin(tournament)
                stateDelegate.reset(screen, tournament, Tournament, 4, gameInfo)
                botPackage2 = Tournament.botPackage
                
                if stateDelegate.rounds == stateDelegate.maxRounds:
                    stateDelegate.tournament = False
                    stateDelegate.setGame(False)
                    stateDelegate.setScene(2)
                    stateDelegate.rounds = 1

                else:
                    stateDelegate.setScene(4)
                    botPackage2 = Tournament.botPackage
                    stateDelegate.rounds += 1

        #-------------------------------------------------

        else:
            if stateDelegate.game:
                LabTest.setup(gameInfo, screen)
                stateDelegate.scenes.insert(3,LabTest.load())
                stateDelegate.setScene(3)
                stateDelegate.setGame(False)
                stateDelegate.win = False
                coins = instance.coins
                
                
            if botPackage:
                func = LabTest.customFunc(botPackage, gameInfo)
            
                #Function call + param update || NOT OPTIMAL TODO
                botPackage = {"bot" : instance.bot[0], "bot2" : instance.bot[1], "pos" : func[0], "pos2" : func[1], "scene" : LabTest.gameScene, "blue" : instance.portalBlue , "orange" : instance.portalOrange }    
            
            if stateDelegate.checkWin(instance) and not stateDelegate.win:
                
                stateDelegate.win = True
                gameInfo.addWin(instance)
                Result.showResult()
                stateDelegate.reset(screen, instance, LabTest, 3, gameInfo)
                stateDelegate.setScene(2)

       
        #Algorithm Testing
        instance.bot[1].updateGameState(enemyPos = instance.bot[0].positionRelative, enemyPoints = gameInfo.coins[0], thisPoints = gameInfo.coins[1])
        instance.bot[0].updateGameState(enemyPos = instance.bot[1].positionRelative, enemyPoints = gameInfo.coins[1], thisPoints = gameInfo.coins[0])
        
        #print(instance.bot)
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

        print(gameInfo.coins)

                    
            #------------------
                
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