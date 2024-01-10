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

    #------------Setup-------------------------------

    instance = LabTest.LabTest()
    instance.setupLab()
    

    botPlayScene = Scene(screen, instance.entities, [], None)
    bot = instance.bot[0]
    bBot = instance.bot[1]
    botPos = bot.getPosition().copy()
    bBotPos = bBot.getPosition().copy()

    botPackage = {"bot" : bot, "bot2" : bBot, "pos" : botPos, "pos2" : bBotPos, "scene" : botPlayScene}
    
    def customFunc(scene, package : dict, instance, gameInfo):
        
        bot = package["bot"]
        bot.tickMax = (2 - gameInfo.botDifficulty[0] + 1) * 144 * 0.1
        bBot = package["bot2"]
        bBot.tickMax = (2 - gameInfo.botDifficulty[1] + 1) * 144 * 0.1
        botPos = package["pos"]
        bBotPos = package["pos2"]
        botPlayScene = package["scene"]
            
        if botPos[0] != bot.getPosition()[0] or botPos[1] != bot.getPosition()[1]:
            elem = MyEntity(botPos.copy()[0], botPos.copy()[1], -1 ,bodyWidth=bot.bodyWidth, bodyHeight=bot.bodyHeight)
            elem.getTextureComponent().color = (0,100,255)
            botPlayScene.elements.append(elem)
            botPos = bot.getPosition().copy()
        
        if bBotPos[0] != bBot.getPosition()[0] or bBotPos[1] != bBot.getPosition()[1]:
            elem = MyEntity(bBotPos.copy()[0], bBotPos.copy()[1], -1 ,bodyWidth=bBot.bodyWidth, bodyHeight=bBot.bodyHeight)
            elem.getTextureComponent().color = (0, 255, 0)
            botPlayScene.elements.append(elem)
            bBotPos = bBot.getPosition().copy()

        return [botPos, bBotPos]
    
    #------------------------------------------------

    #----------Knight Testing-------------

    KnightTest.setup(screen)
    knightScene = KnightTest.gameScene
    entitiyControllers = KnightTest.controllers

    #-------------------------------------

    stateDelegate = GameDelegate(True)
    gameInfo = GameInfo()
    
    Menu.setup(screen, stateDelegate)
    Create.setup(screen, stateDelegate, gameInfo)

    stateDelegate.setup([Menu.gameScene, Create.gameScene, botPlayScene])
    
    while stateDelegate.running:

        screen.fill((255,255,255))
        func = customFunc(stateDelegate.scene, botPackage, instance, gameInfo)
        #Function call + param update || NOT OPTIMAL TODO
        botPackage = {"bot" : bot, "bot2" : bBot, "pos" : func[0], "pos2" : func[1], "scene" : botPlayScene}
        #-------------------------------------------------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:

                    stateDelegate.scene = stateDelegate.scenes[0]
                    instance.entities.clear()
                    instance.setupLab()
                    stateDelegate.scenes.remove(botPlayScene)
                    bot = instance.bot[0]
                    bBot = instance.bot[1]
                    botPos = bot.getPosition().copy()
                    bBotPos = bBot.getPosition().copy()
                    botPlayScene = Scene(screen, instance.entities, [], None)
                    stateDelegate.scenes.append(botPlayScene)
                    botPackage = {"bot" : bot, "bot2" : bBot, "pos" : botPos, "pos2" : bBotPos, "scene" : botPlayScene}

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