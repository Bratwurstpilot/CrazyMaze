import pygame

from Source.Engine.Screen import Screen
from Source.Game.Delegate import GameDelegate
from Source.Game.GameInfo import GameInfo
from Source.Game.Levels import Menu
from Source.Game.Levels import Create
from Source.Game.Levels import LabTest
from Source.Game.Levels import KnightTest



def main():
        
    pygame.init()

    clock = pygame.time.Clock()
    animations : list = []
    screen : pygame.display = Screen.setScreen(1920, 1080, "")

    #----------Knight Testing-------------

    KnightTest.setup(screen)
    knightScene = KnightTest.gameScene
    #entitiyControllers = KnightTest.controllers

    #-------------------------------------

    stateDelegate = GameDelegate(True)
    gameInfo = GameInfo()
    
    Menu.setup(screen, stateDelegate)
    Create.setup(screen, stateDelegate, gameInfo)
    LabTest.setup(screen)
    entitiyControllers = LabTest.controllers
    teleport = True

    instance = LabTest.object
    print(instance.bot)
    botPackage = LabTest.botPackage
    
    stateDelegate.setup([Menu.gameScene, Create.gameScene, LabTest.gameScene])
    
    while stateDelegate.running:

        func = LabTest.customFunc(botPackage, gameInfo)
        
        #Function call + param update || NOT OPTIMAL TODO
        botPackage = {"bot" : instance.bot[0], "bot2" : instance.bot[1], "pos" : func[0], "pos2" : func[1], "scene" : LabTest.gameScene, "blue" : instance.portalBlue , "orange" : instance.portalOrange }
        #-------------------------------------------------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stateDelegate.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:

                    stateDelegate.scene = stateDelegate.scenes[0]
                    instance.entities.clear()
                    instance.setupLab()
                    stateDelegate.scenes.remove(LabTest.gameScene)
                    LabTest.setup(screen)
                    botPackage = LabTest.botPackage
                    stateDelegate.scenes.append(LabTest.gameScene)
                    
                for controller in entitiyControllers:
                    controller.update(event.key, True)

            if event.type == pygame.KEYUP:
                for controller in entitiyControllers:
                    controller.update(event.key, False)
            
            

        if teleport:
            
            if instance.portalBlue.getPhysicsComponent().checkCollide(instance.bot[2]):
                instance.bot[2].setPositionX(instance.portalOrange.getPosition()[0])
                instance.bot[2].setPositionY(instance.portalOrange.getPosition()[1])
                teleport = False

            elif instance.portalOrange.getPhysicsComponent().checkCollide(instance.bot[2]):
                instance.bot[2].setPositionX(instance.portalBlue.getPosition()[0])
                instance.bot[2].setPositionY(instance.portalBlue.getPosition()[1])
                teleport = False
        
        elif not teleport:

            if not instance.portalBlue.getPhysicsComponent().checkCollide(instance.bot[2]) and not instance.portalOrange.getPhysicsComponent().checkCollide(instance.bot[2]):
                teleport = True

        stateDelegate.update()
        stateDelegate.scene.render()
   
        for animation in animations:
            animation.update()

        clock.tick(144)

    pygame.quit()