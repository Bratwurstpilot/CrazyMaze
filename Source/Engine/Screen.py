import pygame

def setScreen(width : int, height : int, title : str) -> pygame.display:

   
    screen : pygame.display = pygame.display.set_mode([width, height])
    

    return screen