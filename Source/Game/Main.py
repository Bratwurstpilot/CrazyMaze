import pygame
import random

from Source.Engine.Entity import Entity
from Source.Engine.Scene import Scene
from Source.Engine.Sound import Music

from Source.Engine.Animation import Animation


from Source.Engine.Screen import Screen



def main():
    
    pygame.init()
    running = True
    clock = pygame.time.Clock()
    screen : pygame.display = Screen.setScreen(1920, 1080, "")

    entities : list = []
    animations : list = []

    #---------Simple Animation Example 1 : Flying Block--------------


    entt = Entity()
    entt.setPosition(0,0,0)
    entt.setBody()

    entities.append(entt)

    animationEnttDown = Animation()
    animationEnttDown.setComponents([entt])
    animationEnttDown.setTargetPositions([[1820, 980]])

    animationEnttUp = Animation()
    animationEnttUp.setComponents([entt])
    animationEnttUp.setTargetPositions([[0, 0]])

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

        entAnimation = Animation()
        entAnimation.setComponents([ent])
        entAnimation.setTargetPositions([[x,1300]])
        entAnimation.setExitAction("ent.setPositionY(y)", {"ent" : ent, "y" : y})
        entAnimation.setTime((i % 10 + 1) * 0.1)
        entAnimation.queue(entAnimation)

        animations.append(entAnimation)
        entAnimation.setActive()

    #-----------------------------------------------

    #---------Complex Animation Example : Incoming Logo Box-------------

    # Flow in Effect

    upperRect = Entity()
    upperRect.setPosition(-300, 300, 0)
    upperRect.setBody(300, 50)

    centerRect = Entity()
    centerRect.setPosition(-500, 350, 0)
    centerRect.setBody(500, 100)

    lowerRect = Entity()
    lowerRect.setPosition(-300, 450, 0)
    lowerRect.setBody(300, 50)

    entities.append(upperRect)
    entities.append(centerRect)
    entities.append(lowerRect)

    animationUpper = Animation()
    animationUpper.setComponents([upperRect])
    animationUpper.setTargetPositions([[750,300]])
    animationUpper.setTime(0.3)

    animationCenter = Animation()
    animationCenter.setComponents([centerRect])
    animationCenter.setTargetPositions([[650,350]])
    animationCenter.setTime(0.5)

    animationLower = Animation()
    animationLower.setComponents([lowerRect])
    animationLower.setTargetPositions([[750,450]])
    animationLower.setTime(0.3)

    animationCenter.queueAsDelay(animationUpper, 0.4)
    animationCenter.queueAsDelay(animationLower, 0.4)

    # Flow out Effect

    animationUpperOut = Animation()
    animationUpperOut.setComponents([upperRect])
    animationUpperOut.setTargetPositions([[2000,300]])
    animationUpperOut.setTime(0.3)

    animationCenterOut = Animation()
    animationCenterOut.setComponents([centerRect])
    animationCenterOut.setTargetPositions([[2000,350]])
    animationCenterOut.setTime(0.5)

    animationLowerOut = Animation()
    animationLowerOut.setComponents([lowerRect])
    animationLowerOut.setTargetPositions([[2000,450]])
    animationLowerOut.setTime(0.3)

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

    mainMenu = Music()
    mainMenu.setMusic("Source/Game/Files/ThemeMainMenu.wav")
    mainMenu.setVolume(0.1)
    mainMenu.play()

    player = Entity()
    player.setPosition(200, 700, 0)
    player.getTextureComponent().setTextureSet(["Source/Game/Files/KnightSprite1.png", "Source/Game/Files/KnightSprite2.png"])
    player.getTextureComponent().setFrameInterval(0.5)
    
    entities.append(player)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        scene1.renderScene()

        for entity in entities:
            entity.update()
        for animation in animations:
            animation.update()

        clock.tick(144)

    pygame.quit()