import pygame

from Source.Engine.Screen import Screen
from Source.Engine.UtilFile import File
from Source.Game.Delegate import GameDelegate
from Source.Game.GameInfo import GameInfo
from Source.Game.Levels import Menu
from Source.Game.Levels import Create
from Source.Game.Levels import LabTest
from Source.Game.Levels import Tournament
from Source.Game.Levels import Result

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
    botPackage2 = Tournament.botPackage

    coins = instance.coins

    stateDelegate.setup([Menu.gameScene, Create.gameScene, Result.gameScene, LabTest.gameScene, Tournament.gameScene])

    while stateDelegate.running:
        #print("Info",gameInfo.intMode)
        #print("Delegate",stateDelegate.mode)
        if stateDelegate.play:
            stateDelegate.setMode(gameInfo.intMode)
            if stateDelegate.mode == 1:

                if stateDelegate.game:

                    stateDelegate.setGame(False)
                    stateDelegate.setWin(False)

                    stateDelegate.scenes.pop(4)
                    stateDelegate.scenes.insert(4, Tournament.load())

                    instance = Tournament.object
                    botPackage2 = Tournament.botPackage
                    coins = instance.coins
                    stateDelegate.setScene(4)
                    
                func = Tournament.customFunc(botPackage2, gameInfo)

                botPackage2 = {"bot" : instance.bot[0], "bot2" : instance.bot[1], "pos" : func[0], "pos2" : func[1], "scene" : Tournament.gameScene, "blue" : instance.portalBlue , "orange" : instance.portalOrange }
                    
                if stateDelegate.checkFinish(instance, gameInfo) and not stateDelegate.win:
                    
                    stateDelegate.setWin(True)
                    stateDelegate.setGame(True)
                    print(gameInfo.coins)
                    stateDelegate.checkWin(gameInfo)
                    print(gameInfo.winCount)
                    
                    stateDelegate.reset(screen, instance, Tournament, 4, gameInfo)
                    botPackage2 = Tournament.botPackage
                    
                    if stateDelegate.rounds == stateDelegate.maxRounds:
                        print(stateDelegate.maxRounds)
                        stateDelegate.setTournament(False)
                        stateDelegate.setGame(False)
                        stateDelegate.setPlay(False)
                        stateDelegate.setScene(2)
                        stateDelegate.setFirst(False)
                        gameInfo.winCount = [0, 0, 0]
                        stateDelegate.rounds = 1

                        File.writeContent("./Source/Game/Result/games.txt", gameInfo)
                        
                    else:
                        stateDelegate.setScene(4)
                        botPackage2 = Tournament.botPackage
                        stateDelegate.rounds += 1
                        print(stateDelegate.rounds)
                        
            elif stateDelegate.mode == 0:
                if stateDelegate.game:

                    stateDelegate.setGame(False)
                    stateDelegate.setWin(False)
                    
                    stateDelegate.scenes.pop(3)
                    stateDelegate.scenes.insert(3, LabTest.load())

                    instance = LabTest.object
                    botPackage = LabTest.botPackage
                    coins = instance.coins
                    stateDelegate.setScene(3)

                func = LabTest.customFunc(botPackage, gameInfo)

                botPackage = {"bot" : instance.bot[0], "bot2" : instance.bot[1], "pos" : func[0], "pos2" : func[1], "scene" : LabTest.gameScene, "blue" : instance.portalBlue , "orange" : instance.portalOrange }  

                if stateDelegate.checkFinish(instance, gameInfo) and not stateDelegate.win:
                        
                        stateDelegate.setWin(True)
                        stateDelegate.setPlay(False)
                        stateDelegate.first = False
                        #gameInfo.addWin(instance)
                        Result.showResult(gameInfo)
                        stateDelegate.reset(screen, instance, LabTest, 3, gameInfo)
                        stateDelegate.setScene(2)
   
            #Algorithm Testing
            instance.bot[1].updateGameState(enemyPos = instance.bot[0].positionRelative, enemyPoints = gameInfo.coins[0], thisPoints = gameInfo.coins[1])
            instance.bot[0].updateGameState(enemyPos = instance.bot[1].positionRelative, enemyPoints = gameInfo.coins[1], thisPoints = gameInfo.coins[0])
        
            for coin in coins:
                if coin.checkCollide(instance.bot[0]):
                    #print("Bot 0 collected coin")
                    stateDelegate.selectCoin(coin, coins, instance, gameInfo, 0)
                    
                elif coin.checkCollide(instance.bot[1]):
                    #print("Bot 1 collected coin")
                    stateDelegate.selectCoin(coin, coins, instance, gameInfo, 1)
                    
              
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
