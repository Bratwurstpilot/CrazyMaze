import pygame

import Source.Game.GameScenes as GameScene
from Source.Engine.Scene import Scene
from Source.Engine.Animation import Animation
from Source.Engine.Sound import Music
from Source.Game.Delegate import GameDelegate


def main():
        
    pygame.init()

    running = True
    clock = pygame.time.Clock()
    animations : list = []

    stateDelegate = GameScene.stateDelegate

    while stateDelegate.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        
        stateDelegate.update()
        stateDelegate.scene.render()
        
        

                    
        for animation in animations:
            animation.update()

        

        clock.tick(144)

    pygame.quit()