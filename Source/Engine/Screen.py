import pygame



def setScreen(width : int, height : int, title : str) -> pygame.display:

    screen : pygame.display = pygame.display.set_mode([width, height])
    screen : pygame.display = pygame.display.set_caption(title)

    return screen