import pygame

from Source.Engine.Entity import Entity
from Source.Engine.Scene import Scene
import Source.Engine.Screen as SES


def main():
    
    pygame.init()
    running = True
    clock = pygame.time.Clock()
    screen : pygame.display = SES.setScreen(800,600, "")

    entt = Entity()
    entt.setPosition(250,250,0)
    #entt.setBody()
    entt.getTextureComponent().setTextureSet(["CrazyMaze/Source/Game/Files/KnightSprite1.png", "CrazyMaze/Source/Game/Files/KnightSprite2.png"])
    entt.getTextureComponent().setFrameIntervalCustom([0.5, 0.5, 0.5, 0.5, 0.2, 0.2, 0.2, 0.2, 2])

    scene1 = Scene(screen, [entt])

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        scene1.renderScene()
        entt.update()

        clock.tick(144)

    pygame.quit()
