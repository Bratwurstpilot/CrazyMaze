from Source.Engine.Entity import Entity
from Source.Engine.Scene import Scene

import Source.Engine.Screen as SES
import pygame

def main():
    
    entt = Entity()
    entt.setBodyWidth(50)
    entt.setBodyHeight(50)
    

    pygame.init()
    screen = SES.setScreen(500, 500, "Crappy")

    rend = Scene(screen, [entt])

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

        rend.screen.fill((255, 255, 255))
        rend.renderScene()
        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
        pygame.display.flip()

        timer += 1
        #if timer >= limit:
        #    entt.getSoundComponent().play(sound)
        #    timer = 0

        clock.tick(144)

    pygame.quit()
