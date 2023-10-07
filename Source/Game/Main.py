import pygame

from Source.Engine.Entity import Entity
from Source.Engine.Scene import Scene
from Source.Engine.Sound import Music
from Source.Engine.Screen import Screen


def main():
    
    pygame.init()

    entts = []

    for i in range(0, 10, 2):
        for j in range(0, 10, 2):
            entt = Entity()
            entt.setBody(50,50)
            entt.setPosition(50 * j, 50 * i, 0)
            entts.append(entt)

    pygame.init()
    screen = Screen.setScreen(500, 500, "Crappy")
    
    running = True
    clock = pygame.time.Clock()

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