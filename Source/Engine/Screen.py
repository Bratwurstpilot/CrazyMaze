import pygame

class Screen:

    def setScreen(width : int = 500, height : int = 500, title : str = "", img : pygame.image = pygame.image.load("Dependencies/Files/icon.png")) -> pygame.display:

        screen : pygame.display = pygame.display.set_icon(img)
        screen : pygame.display = pygame.display.set_caption(title)
        screen : pygame.display = pygame.display.set_mode([width, height])
        
        return screen