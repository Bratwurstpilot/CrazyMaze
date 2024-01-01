import pygame


from Source.Engine.Scene import Scene
from Source.Engine.Animation import Animation
from Source.Engine.Sound import Music

from Source.Game.Delegate import GameDelegate
from Source.Game.Util import MyEntity
from Source.Game.Levels.LabTest import LabTest

from Source.Game.Levels import LabTest

from Source.Engine.Screen import Screen
from Source.Game.Delegate import GameDelegate
from Source.Game.Levels import Menu
from Source.Game.Levels import Create




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

    entities = instance.entities

    uiEntities = []

    def customFunc(scene, package : dict, instance):
        
        bot = package["bot"]
        botPos = package["pos"]
        botPlayScene = package["scene"]
            
        if botPos[0] != bot.getPosition()[0] or botPos[1] != bot.getPosition()[1]:
            elem = MyEntity(botPos.copy()[0], botPos.copy()[1], bodyWidth=50, bodyHeight=50)
            elem.getTextureComponent().color = (0,100,255)
            botPlayScene.elements.append(elem)
            botPos = bot.getPosition().copy()

        return botPos
    #------------------------------------------------

    

    while running:

        screen.fill((255,255,255))
        

        #Function call + param update || NOT OPTIMAL TODO
        botPackage = {"bot" : bot, "pos" : customFunc(mainScene, botPackage, instance), "scene" : botPlayScene}
        #-------------------------------------------------


    stateDelegate = GameDelegate(True)
    
    Menu.setup(screen, stateDelegate)
    Create.setup(screen, stateDelegate)

    
    stateDelegate.setup([Menu.gameScene, Create.gameScene])


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        for entity in mainScene.uiElements:
            if entity.update():
                if entity.text == "Beenden":
                    running = False 
                elif entity.text == "Spiel erstellen":
                    mainScene = botPlayScene
                elif entity.text == "Zurück":
                    mainScene = MainMenuStartUp.gameScene
        
        mainScene.render()

        for entity in mainScene.elements:
            entity.update()
        for entity in mainScene.uiElements:
            entity.update()             
        #for animation in mainScene.animations: TODO
        #    animation.update()

        clock.tick(144)
    pygame.quit()