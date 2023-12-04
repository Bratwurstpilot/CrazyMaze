import pygame
import random

from Source.Engine.Sound import Music
from Source.Engine.Animation import Animation
from Source.Engine.Label import Label
from Source.Engine.Button import Button
from Source.Game.Util import MyEntity, MyController, MyController2
from Source.Algorithms.Agent import Agent

class stressTest:

    entities : list = []
    animations : list = []
    uiEntities : list = []
    
    #---------Test Labels--------------------------------------------
    
    testLabel = Label(100, 200, 1, 100, 100)
    testLabel.setText("Crazy Maze")
    testLabel.setBgColor((0, 0, 0))
    testLabel.setTextFont()
    testLabel.setRect()
    uiEntities.append(testLabel)

    def testFunc(x):
        x.shiftPositionX(200)
        x.setTextFont()
        x.setRect()

    testButton = Button(100, 300, 1, 200, 100, buttonFunction = testFunc, param = testLabel)
    testButton.setText("Button")
    testButton.setBgColor((0, 0, 0))
    testButton.setTextFont()
    testButton.setTextRect()
    uiEntities.append(testButton)

    #---------Simple Animation Example 1 : Flying Block--------------

    entt = MyEntity(0,0,0)
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
        ent = MyEntity()
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

    upperRect = MyEntity(-300, 300, 0, 300, 50)
    centerRect = MyEntity(-500, 350, 0, 500, 100)
    lowerRect = MyEntity(-300, 450, 0, 300, 50)

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

    player1 = MyEntity(200, 700, 0)
    player1.getTextureComponent().setTextureSet(["Source/Game/Files/KnightSprite1.png", "Source/Game/Files/KnightSprite2.png"])
    player1.getTextureComponent().setFrameInterval(0.5)
    entities.append(player1)

    controller1 = MyController([player1], 0)

    player2 = MyEntity(200, 700, 0)
    player2.getTextureComponent().setTextureSet(["Source/Game/Files/KnightSprite1.png", "Source/Game/Files/KnightSprite2.png"])
    player2.getTextureComponent().setFrameInterval(0.5)
    entities.append(player2)

    controller2 = MyController2([player2], 1)
    
    agent = Agent()
    entities.append(agent)

    controllers = [controller1, controller2]
    
    pygame.init()
    mainMenu = Music("Source/Game/Files/ThemeMainMenu.wav", 0.1)
    #mainMenu.play()