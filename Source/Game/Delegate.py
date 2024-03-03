import pygame

from Source.Engine.Scene import Scene


pygame.init()
class GameDelegate:

    def __init__(self, run : bool):

        self.scene : Scene = None
        self.running : bool = run
        self.scenes : list = []
        self.allScenes : list = []
        self.stateGame : bool = True

        self.tournament : bool = False
        self.maxRounds = 0
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
    

    def setTournament(self, state, rounds):

        self.tournament = state
        self.maxRounds = rounds


    def setStateGame(self, state : bool):

        self.stateGame = state

        
    def update(self):

        for entitie in self.scene.elements: 
            entitie.update()
        for entitie in self.scene.uiElements:
            entitie.update() 


    def checkWin(self, instance):

        return (instance.bot[0].getPosition() == instance.end[1]) or (instance.bot[1].getPosition() == instance.end[0])


    def addScene(self, scene):

        self.scenes.append(scene)
    

    def reset(self, delegate, screen, instance, level, index, info):
        
        delegate.setStateGame(True)
        self.scene = self.scenes[0]
        instance.entities.clear()
        
        self.scenes.pop(index)
        