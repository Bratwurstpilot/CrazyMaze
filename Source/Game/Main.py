import pygame

from Source.Engine.Animation import Animation
from Source.Engine.Sound import Music
from Source.Engine.Screen import Screen
from Source.Game.Delegate import GameDelegate
from Source.Game.Levels import Menu
from Source.Game.Levels import Create



def main():
        
    pygame.init()

    clock = pygame.time.Clock()
    animations : list = []
    screen : pygame.display = Screen.setScreen(1920, 1080, "")

    stateDelegate = GameDelegate(True)
    
    Menu.setup(screen, stateDelegate)
    Create.setup(screen, stateDelegate)

    
    stateDelegate.setup([Menu.gameScene, Create.gameScene])

    while stateDelegate.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pass
        
        
        stateDelegate.update()
        stateDelegate.scene.render()
   
        for animation in animations:
            animation.update()

        

        clock.tick(144)
    pygame.quit()