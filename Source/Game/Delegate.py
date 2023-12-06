import pygame

from Source.Engine.Scene import Scene

pygame.init()
class GameDelegate:

    def __init__(self, scene : Scene, run : bool):
        self.scene : Scene = scene
        self.running : bool = run
    
    def setScene(self, scene : Scene) -> None: 
        
        self.scene = scene

    def setRunning(self, run : bool) -> None:

        self.running = run
    
    def update(self,):
        for entitie in self.scene.elements: 
            entitie.update()
        for entitie in self.scene.uiElements:
            entitie.update() 