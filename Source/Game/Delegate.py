import pygame

from Source.Engine.Scene import Scene


pygame.init()
class GameDelegate:

    def __init__(self,run : bool):

        self.scene : Scene = None
        self.running : bool = run
        self.scenes : list = []
        self.tournament : bool = False
        

    def setup(self, scenes : list):

        self.scene = scenes[0]
        self.scenes = scenes 


    def setScene(self, index : int) -> None: 
        
        self.scene = self.scenes[index]


    def setRunning(self, run : bool) -> None:

        self.running = run
    

    def update(self,):
        for entitie in self.scene.elements: 
            entitie.update()
        for entitie in self.scene.uiElements:
            entitie.update() 


    def checkWin(self, instance):

        return (instance.bot[0].getPosition() == instance.end[1]) or (instance.bot[1].getPosition() == instance.end[0])
        

