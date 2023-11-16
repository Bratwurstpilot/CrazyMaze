import pygame

from Source.Engine.Scene import Scene
from Source.Engine.Animation import Animation
from Source.Engine.Screen import Screen
from Source.Engine.Sound import Music
from Source.Game.Menu import Menu
from Source.Game.StressTest import stressTest


class Main:

    def __init__(self, running : bool):
        self.running = running
        self.run()

    def setRunning(self, state : bool):
        self.running = state
        print(state)
        print(self.running)
    

    def run(self):
        
        pygame.init()

        running = True
        clock = pygame.time.Clock()
        infoObject = pygame.display.Info()
        #print(infoObject)
        screen : pygame.display = Screen.setScreen(infoObject.current_w, infoObject.current_h, "")

        mainMenu = Menu([self.setRunning])
        
        background = mainMenu.background
        entities = mainMenu.entities
        #controllers = mainMenu.controllers
        animations = mainMenu.animations
        uiEntities = mainMenu.uiEntities

        scene1 = Scene(screen, entities, uiEntities, background)    

        stateVar = 0

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                #if event.type == pygame.KEYDOWN:
                    #for controller in controllers:
                        #controller.update_(event.key, True)
            # if event.type == pygame.KEYUP:
                    #for controller in controllers:
                        #controller.update_(event.key, False)

                #--------Experimental------------------------
                """if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if stateVar == 0:
                        entities = [otherTest.player]
                        controllers = [otherTest.controller]
                        animations = []
                        scene1 = Scene(screen, entities, uiEntities)    
                        stateVar = 1
                    else:
                        entities = test.entities
                        controllers = test.controllers
                        animations = test.animations
                        scene1 = Scene(screen, entities, uiEntities)  
                        stateVar = 0
                """
                #---------------------------------------------

            scene1.render()
            
            

            for entity in entities:
                entity.update()
            for entity in uiEntities:
                entity.update()             
            for animation in animations:
                animation.update()

            

            clock.tick(144)

        pygame.quit()