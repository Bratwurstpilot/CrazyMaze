import pygame

from Source.Engine.Scene import Scene


pygame.init()
class GameDelegate:

    def __init__(self,run : bool):

        self.scene : Scene = None
        self.running : bool = run
        self.scenes : list = []
        self.allScenes : list = []

        self.tournament : bool = False
        self.maxRounds = 0
        self.rounds = 1        


    def setup(self, scenes : list):

        self.scene = scenes[0]
        self.scenes = scenes 


    def setScene(self, index : int) -> None: 
        
        self.scene = self.scenes[index]


    def setRunning(self, run : bool) -> None:

        self.running = run
    

    def setTournament(self, state, rounds):

        self.tournament = state
        self.maxRounds = rounds


    def addScene(self, scene): 
    
        self.scenes.append(scene)


    def update(self):

        for entitie in self.scene.elements: 
            entitie.update()
        for entitie in self.scene.uiElements:
            entitie.update() 


    def checkWin(self, instance):

        return (instance.bot[0].getPosition() == instance.end[1]) or (instance.bot[1].getPosition() == instance.end[0])
        
    
    def reset(self, screen, instance, level):
        
        self.scene = self.scenes[0]
        instance.entities.clear()
        instance.setupLab()
        self.scenes.pop(2)
        level.setup(screen)
        self.scenes.insert(2, level.gameScene)