import pygame


from Source.Engine.Scene import Scene
from Source.Engine.Animation import Animation
from Source.Engine.Sound import Music
from Source.Engine.Screen import Screen

from Source.Game.Util import MyEntity
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
    entitiyControllers = KnightTest.controllers

    #-------------------------------------

    stateDelegate = GameDelegate(True)
    gameInfo = GameInfo()
    
    Menu.setup(screen, stateDelegate)
    Create.setup(screen, stateDelegate, gameInfo)
    LabTest.setup(screen)

    instance = LabTest.object

    bot = instance.bot[0]
    bBot = instance.bot[1]
    botPos = bot.getPosition().copy()
    bBotPos = bBot.getPosition().copy()
    botPackage = {"bot" : bot, "bot2" : bBot, "pos" : botPos, "pos2" : bBotPos, "scene" : LabTest.gameScene}
    
    LabTest.setup(screen, LabTest.customFunc, [LabTest.botPackage, gameInfo])
    stateDelegate.setup([Menu.gameScene, Create.gameScene, LabTest.gameScene])
    
    while stateDelegate.running:

        func = LabTest.gameScene.execFunc()
        #Function call + param update || NOT OPTIMAL TODO
        botPackage = {"bot" : bot, "bot2" : bBot, "pos" : func[0], "pos2" : func[1], "scene" : LabTest.gameScene}
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
                    botPackage = LabTest.botPackage
                    LabTest.setup(screen, LabTest.customFunc, [botPackage, gameInfo])
                    stateDelegate.scenes.append(LabTest.gameScene)
                    
                for controller in entitiyControllers:
                    controller.update(event.key, True)

            if event.type == pygame.KEYUP:
                for controller in entitiyControllers:
                    controller.update(event.key, False)

        stateDelegate.update()
        stateDelegate.scene.render()
   
        for animation in animations:
            animation.update()

        clock.tick(144)

    pygame.quit()