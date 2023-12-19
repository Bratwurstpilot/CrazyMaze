import pygame

from Source.Engine.Scene import Scene


pygame.init()
class GameDelegate:

    def __init__(self,run : bool):

        self.scene : Scene = None
        self.running : bool = run
        self.scenes : list = []
        self.setScene(self.scenes[0])

    
    def setup(self, scenes : list):

        self.scene = scenes[0]
        self.scenes = scenes 


    def setScene(self, scene : Scene) -> None: 
        
        self.scene = scene


    def setRunning(self, run : bool) -> None:

        self.running = run
    

    def update(self,):
        for entitie in self.scene.elements: 
            entitie.update()
        for entitie in self.scene.uiElements:
            entitie.update() 
        

