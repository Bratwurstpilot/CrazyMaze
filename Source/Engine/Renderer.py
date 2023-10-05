import pygame

class Renderer():

    def __init__(self, newScreen : pygame.display, newElements : list) -> None :

        self.__screen : pygame.display = newScreen
        self.__elements : list = newElements

    def renderScene(self) -> None :
        
        pass