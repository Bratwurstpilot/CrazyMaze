import pygame
import random

from Source.Engine.Entity import Entity
from Source.Engine.Scene import Scene
from Source.Engine.Sound import Music
from Source.Engine.Animation import Animation
from Source.Engine.Screen import Screen
from Source.Engine.InputController import EntityController



def main():
    
    pygame.init()
    running = True
    clock = pygame.time.Clock()
    screen : pygame.display = Screen.setScreen(1920, 1080, "")

    entities : list = []
    animations : list = []

    #---------Simple Animation Example 1 : Flying Block--------------


    entt = Entity(0,0,0)
    entities.append(entt)

    animationEnttDown = Animation([entt], [[1820, 980]])
    animationEnttUp = Animation([entt], [[0,0]])

    animationEnttDown.queue(animationEnttUp)
    animationEnttUp.queue(animationEnttDown)

    animations.append(animationEnttDown)
    animations.append(animationEnttUp)

    animationEnttUp.setActive()

    #-----------------------------------------------

    #---------Simple Animation Example 2 : Rain--------------

    for i in range(300):
        ent = Entity()
        ent.setBody(4, 8)
        x = random.randint(0,1900)
        y = random.randint(0,3000) * -1
        ent.setPosition(x, y)
        entities.append(ent)

        entAnimation = Animation([ent], [[x, 1300]], (i % 10 + 1) * 0.1)
        entAnimation.setExitAction("ent.setPositionY(y)", {"ent" : ent, "y" : y})
        entAnimation.queue(entAnimation)

        animations.append(entAnimation)
        entAnimation.setActive()

    #-----------------------------------------------

    #---------Complex Animation Example : Incoming Logo Box-------------

    # Flow in Effect

    upperRect = Entity(-300, 300, 0, 300, 50)
    centerRect = Entity(-500, 350, 0, 500, 100)
    lowerRect = Entity(-300, 450, 0, 300, 50)

    entities.append(upperRect)
    entities.append(centerRect)
    entities.append(lowerRect)

    animationUpper = Animation([upperRect], [[750, 300]], 0.3)
    animationCenter = Animation([centerRect], [[650, 350]], 0.5)
    animationLower = Animation([lowerRect], [[750, 450]], 0.3)

    animationCenter.queueAsDelay(animationUpper, 0.4)
    animationCenter.queueAsDelay(animationLower, 0.4)

    # Flow out Effect

    animationUpperOut = Animation([upperRect], [[2000, 300]], 0.3)
    animationCenterOut = Animation([centerRect], [[2000, 350]], 0.5)
    animationLowerOut = Animation([lowerRect], [[2000, 450]], 0.3)

    animationCenter.queueAsDelay(animationUpperOut, 2.0)
    animationCenter.queueAsDelay(animationCenterOut, 2.1)
    animationCenter.queueAsDelay(animationLowerOut, 2.0)

    program = "ent1.setPosition(-300, 300, 0) \nent2.setPosition(-500, 350, 0) \nent3.setPosition(-300, 450, 0) \nanim.setActive()"
    animationCenter.setExitAction(program, {"ent1" : upperRect, "ent2" : centerRect, "ent3" : lowerRect, "anim" : animationCenter})
    animationCenter.queueAsDelay(animationCenter, 5.0)

    animations.append(animationUpper)
    animations.append(animationCenter)
    animations.append(animationLower)
    animations.append(animationUpperOut)
    animations.append(animationCenterOut)
    animations.append(animationLowerOut)

    animationCenter.setActive()

    #-------------------------------------------

    scene1 = Scene(screen, entities)

    mainMenu = Music("Source/Game/Files/ThemeMainMenu.wav", 0.1)
    #mainMenu.play()

    player = Entity(200, 700, 0)
    player.getTextureComponent().setTextureSet(["Source/Game/Files/KnightSprite1.png", "Source/Game/Files/KnightSprite2.png"])
    player.getTextureComponent().setFrameInterval(0.5)
    entities.append(player)

    controller = EntityController([player])

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                controller.update(event.key, True)
            if event.type == pygame.KEYUP:
                controller.update(event.key, False)
        scene1.renderScene()

        for entity in entities:
            entity.update()
        for animation in animations:
            animation.update()

        clock.tick(144)

    pygame.quit()