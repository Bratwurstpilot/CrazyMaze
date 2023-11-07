import pygame

from Source.Engine.Scene import Scene
from Source.Engine.Screen import Screen
from Source.Engine.Sound import Music
from Source.Game.StressTest import stressTest
from Source.Game.OtherTest import otherTest


def main():
    
    pygame.init()

    running = True
    clock = pygame.time.Clock()
    screen : pygame.display = Screen.setScreen(1920, 1080, "")

    test = stressTest
    test2 = otherTest

    entities = test.entities
    controllers = test.controllers
    animations = test.animations

    scene1 = Scene(screen, entities)    

    stateVar = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                for controller in controllers:
                    controller.update_(event.key, True)
            if event.type == pygame.KEYUP:
                for controller in controllers:
                    controller.update_(event.key, False)

            #--------Experimental------------------------
            if event.type == pygame.MOUSEBUTTONDOWN:
                if stateVar == 0:
                    entities = [otherTest.player]
                    controllers = [otherTest.controller]
                    animations = []
                    scene1 = Scene(screen, entities)    
                    stateVar = 1
                else:
                    entities = test.entities
                    controllers = test.controllers
                    animations = test.animations
                    scene1 = Scene(screen, entities)  
                    stateVar = 0
            #---------------------------------------------

        scene1.renderScene()

        for entity in entities:
            entity.update()
        for animation in animations:
            animation.update()

        clock.tick(144)

    pygame.quit()