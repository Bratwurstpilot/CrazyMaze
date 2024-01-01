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




def main():
        
    pygame.init()

    clock = pygame.time.Clock()
    animations : list = []
    screen : pygame.display = Screen.setScreen(1920, 1080, "")

    #------------Setup-------------------------------

    

    instance = LabTest.LabTest()
    instance.setupLab()

    botPlayScene = Scene(screen, instance.entities, [], None)
    bot = instance.entities[-1]
    botPos = bot.getPosition().copy()

    botPackage = {"bot" : bot, "pos" : botPos, "scene" : botPlayScene}
    

    def customFunc(scene, package : dict, instance, gameInfo):
        
        bot = package["bot"]
        bot.tickMax = (2 - gameInfo.botDifficulty[0] + 1) * 144 * 0.2
        botPos = package["pos"]
        botPlayScene = package["scene"]
            
        if botPos[0] != bot.getPosition()[0] or botPos[1] != bot.getPosition()[1]:
            elem = MyEntity(botPos.copy()[0], botPos.copy()[1], bodyWidth=50, bodyHeight=50)
            elem.getTextureComponent().color = (0,100,255)
            botPlayScene.elements.append(elem)
            botPos = bot.getPosition().copy()

        return botPos
    #------------------------------------------------

    


    stateDelegate = GameDelegate(True)
    gameInfo = GameInfo()
    
    Menu.setup(screen, stateDelegate)
    Create.setup(screen, stateDelegate, gameInfo)

    stateDelegate.setup([Menu.gameScene, Create.gameScene, botPlayScene])
    
    while stateDelegate.running:

        screen.fill((255,255,255))
        

        #Function call + param update || NOT OPTIMAL TODO
        botPackage = {"bot" : bot, "pos" : customFunc(stateDelegate.scene, botPackage, instance, gameInfo), "scene" : botPlayScene}
        #-------------------------------------------------


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        stateDelegate.update()
        stateDelegate.scene.render()
   
        for animation in animations:
            animation.update()
    
               
        #for animation in mainScene.animations: TODO
        #    animation.update()

        clock.tick(144)
    pygame.quit()