import pygame
import random

from Source.Engine.Entity import Entity
from Source.Engine.Scene import Scene
import Source.Engine.Screen as SES


def main():
    
    entt = Entity()
    entt.setBodyWidth(50)
    entt.setBodyHeight(50)
    entt.setPositionZ(2)

    entt2 = Entity()
    entt2.setBody(50,50)
    entt2.setPosition(100,100, 0)
    entt2.setPositionZ(1)

    entt3 = Entity()
    entt3.setBody(50,50)
    entt3.setPosition(150,150, 0)
    entt3.setPositionZ(0)


    pygame.init()
    screen = SES.setScreen(500, 500, "Crappy")

    rend = Scene(screen, [entt, entt2, entt3])
    

    running = True
    clock = pygame.time.Clock()

    timer = 0
    limit = 144
    sound = pygame.mixer.Sound("Dependencies/Sounds/test.wav") # Selbst erstellter Sound, kein Copyright

    # crappy pygame test

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        rend.renderScene()
        
        timer += 1
        #if timer >= limit:
        #    entt.getSoundComponent().play(sound)
        #    timer = 0

        clock.tick(144)

    pygame.quit()