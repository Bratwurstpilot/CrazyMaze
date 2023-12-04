import pygame

import Source.Game.GameScenes as GameScene
from Source.Engine.Scene import Scene
from Source.Engine.Animation import Animation
from Source.Engine.Screen import Screen
from Source.Engine.Sound import Music
from Source.Game.StressTest import stressTest
from Source.Game.OtherTest import otherTest

def main():
        
    pygame.init()

    running = True
    clock = pygame.time.Clock()
    animations : list = []
    
    mainScene = GameScene.menuScene
    entities = GameScene.mainMenu.entities
    uiEntities = GameScene.mainMenu.uiEntities

    while running:
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