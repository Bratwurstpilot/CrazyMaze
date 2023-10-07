import pygame

from Source.Engine.Entity import Entity
from Source.Engine.Scene import Scene
from Source.Engine.Sound import Music

import Source.Engine.Screen as SES


def main():
    
    pygame.init()
    running = True
    clock = pygame.time.Clock()
    screen : pygame.display = SES.setScreen(800,600, "")

    entt = Entity()
    entt.setPosition(250,250,0)
    entt.getTextureComponent().setTextureSet(["Source/Game/Files/KnightSprite1.png", "Source/Game/Files/KnightSprite2.png"])
    entt.getTextureComponent().setFrameInterval(0.5)

    themeMain = Music()
    themeMain.setMusic("Source/Game/Files/ThemeMainMenu.wav")
    themeMain.setVolume(0.1)
    themeMain.play()
    
    scene1 = Scene(screen, [entt])

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        scene1.renderScene()
        entt.update()


        clock.tick(144)

    pygame.quit()
