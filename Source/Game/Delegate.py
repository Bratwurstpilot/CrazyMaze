import pygame

from Source.Engine.Scene import Scene


pygame.init()
class GameDelegate:

    def __init__(self, run : bool):

        self.scene : Scene = None
        self.running : bool = run
        self.scenes : list = []
        self.allScenes : list = []
        self.mode : int = -1

        self.stateGame : bool = True
        self.game : bool = False
        self.play : bool = False
        self.first : bool = False
        self.win : bool = False
        self.tournament : bool = False
        self.maxRounds = 10
        self.rounds = 1        


    def setup(self, scenes : list):

        self.scene = scenes[0]
        self.scenes = scenes 


    def setScene(self, index : int) -> None: 

        try: 
            self.scenes[index].setup()
            self.scene = self.scenes[index]
        except:
            self.scene = self.scenes[index]


    def setRunning(self, run : bool) -> None:

        self.running = run
    

    def setTournament(self, state, rounds = 10):

        self.tournament = state
        self.maxRounds = rounds


    def setGame(self, state : bool):

        self.game = state

    
    def setPlay(self, state : bool):
        
        self.play = state

    
    def setWin(self, state : bool): 
        
        self.win = state

    
    def setFirst(self, state : bool):

        self.first = state


    def setMode(self, mode : int):

        self.mode = mode
        
    
    def swiftRound(self, step : int):

        self.maxRounds += step
        
        if self.maxRounds < 0:
            self.maxRounds = 0


    def update(self):

        for entitie in self.scene.elements: 
            entitie.update()
        for entitie in self.scene.uiElements:
            entitie.update() 


    def checkFinish(self, instance, gameInfo):

        if not self.first:
            
            if instance.bot[0].getPosition() == instance.end[1]:
                self.first = True
                gameInfo.coins[0] += 2
            
            elif instance.bot[1].getPosition() == instance.end[0]:
                self.first = True
                gameInfo.coins[1] += 2
            
        return (instance.bot[0].getPosition() == instance.end[1]) and (instance.bot[1].getPosition() == instance.end[0])


    def checkWin(self, gameInfo):

        if gameInfo.coins[0] > gameInfo.coins[1]:
            gameInfo.winCount[0] += 1

        elif gameInfo.coins[1] > gameInfo.coins[0]:
            gameInfo.winCount[1] += 1

        elif gameInfo.coins[0] == gameInfo.coins[1]:
            gameInfo.winCount[2] += 1

        gameInfo.coins = [0, 0]
        
    
    def selectCoin(self, coin, coins, instance, info, botNumber):

        info.coins[botNumber] += 1
     
        for bot in instance.bot:
            try:
                bot.signal("Coin", [coin.positionX, coin.positionY], labCoords = instance.START, labLineWidth = instance.LINEWIDTH)
            except AttributeError:
                bot.signal("Coin", [coin.positionX, coin.positionY])
        coins.remove(coin)
        instance.entities.remove(coin)
    
    
    def reset(self, screen, instance, level, index, info):
        
        self.scene = self.scenes[0]
        instance.entities.clear()
        self.scenes.pop(index)
        self.scenes.insert(index, level.gameScene)
