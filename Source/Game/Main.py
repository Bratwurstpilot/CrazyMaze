import pygame
import random

from Source.Engine.Entity import Entity
from Source.Engine.Scene import Scene
import Source.Engine.Screen as SES


def main():
    
    entts = []

    for i in range(0, 10, 2):
        for j in range(0, 10, 2):
            entt = Entity()
            entt.setBody(50,50)
            entt.setPosition(50 * j, 50 * i, 0)
            entts.append(entt)

    pygame.init()
    screen = SES.setScreen(500, 500, "Crappy")

    rend = Scene(screen, entts)
    

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