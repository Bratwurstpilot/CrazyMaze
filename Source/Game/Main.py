import pygame

import Source.Game.GameScenes as GameScene
from Source.Engine.Scene import Scene
from Source.Engine.Animation import Animation
from Source.Engine.Screen import Screen
from Source.Engine.Sound import Music
from Source.Game.StressTest import stressTest
from Source.Game.OtherTest import otherTest
from Source.Game.Util import MyEntity

from Source.Game.LabTest import LabTest

def main():
        
    pygame.init()

    running = True
    clock = pygame.time.Clock()
    animations : list = []
    
    #mainScene = GameScene.menuScene
    #entities = GameScene.mainMenu.entities
    #uiEntities = GameScene.mainMenu.uiEntities

    instance = LabTest()
    instance.setupLab()
    bot = instance.entities[0]
    botPos = bot.getPosition().copy()

    screen : pygame.display = Screen.setScreen(1920, 1080, "")
    scene = Scene(screen, instance.entities, [], None)

    entities = instance.entities
    uiEntities = []

    mainScene = scene

    while running:

        screen.fill((255,255,255))

        if botPos[0] != bot.getPosition()[0] or botPos[1] != bot.getPosition()[1]:
            
            elem = MyEntity(botPos.copy()[0], botPos.copy()[1], bodyWidth=50, bodyHeight=50)
            elem.getTextureComponent().color = (0,100,255)
            scene.elements.append(elem)
            botPos = bot.getPosition().copy()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        for entity in uiEntities:
            if entity.update():
                if entity.text == "Beenden":
                    running = False 
                elif entity.text == "Spiel erstellen":
                    entities = GameScene.createGame.entities
                    uiEntities = GameScene.createGame.uiEntities
                    mainScene = GameScene.createScene
                elif entity.text == "Zurück":
                    entities = GameScene.mainMenu.entities
                    uiEntities = GameScene.mainMenu.uiEntities
                    mainScene = GameScene.menuScene
        
        mainScene.render()

        for entity in entities:
            entity.update()
        for entity in uiEntities:
            entity.update()             
        for animation in animations:
            animation.update()

        

        clock.tick(144)

    pygame.quit()