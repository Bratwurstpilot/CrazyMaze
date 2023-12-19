import pygame

from Source.Engine.Animation import Animation
from Source.Engine.Sound import Music
from Source.Engine.Screen import Screen
from Source.Game.Delegate import GameDelegate
from Source.Game.Menu import menu
from Source.Game.Create import create



def main():
        
    pygame.init()

    clock = pygame.time.Clock()
    animations : list = []
    infoObject = pygame.display.Info()
    screen : pygame.display = Screen.setScreen(infoObject.current_w, infoObject.current_h, "")
    stateDelegate = GameDelegate(True)
    test = [menu, create]
    scenes = []
    for i in range(len(test)):
        scenes.append(test[i].setup(test[i], screen, stateDelegate))

    stateDelegate.setup(scenes)

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