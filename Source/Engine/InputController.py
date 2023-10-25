from Source.Engine.Entity import Entity
import pygame


class EntityController():

    def __init__(self, entities : list[Entity] = []) -> None:

        self.__aiControlled : bool = False
        self.__controlledEntities : list[Entity] = entities
        self.__keysPressed : list[str] = []

        self.__controllerID : int = 0 # ID 0 => WASD, ID 1 => ULDR
    

    def update(self, key, mode : bool) -> None:
        
        input = self.__processInput(key)

        for entity in self.__controlledEntities:
            entity.getPhysicsComponent().resetMomentum()

        if not mode:
            self.__keysPressed.remove(input)
        else:
            if input not in self.__keysPressed:
                self.__keysPressed.append(input)
                print(self.__keysPressed)

        if "LEFT" in self.__keysPressed:
            for entity in self.__controlledEntities:
                entity.getPhysicsComponent().setMomentumX(direction = -1)
        elif "RIGHT" in self.__keysPressed:
            for entity in self.__controlledEntities:
                entity.getPhysicsComponent().setMomentumX()

        if "UP" in self.__keysPressed:
            for entity in self.__controlledEntities:
                entity.getPhysicsComponent().setMomentumY(direction = -1)
        elif "DOWN" in self.__keysPressed:
            for entity in self.__controlledEntities:
                entity.getPhysicsComponent().setMomentumY()


    # Set Methods

    
    def setControllScript(self, script : str) -> None:

        pass


    # Get Methods


    def getKeys(self) -> None:

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.KEYDOWN:
                return self.__processInput()


    def __processInput(self, key) -> None:

        if self.__controllerID == 0:
            if key == pygame.K_w:
                return "UP"
            elif key == pygame.K_s:
                return "DOWN"
            elif key == pygame.K_a:
                return "LEFT"
            elif key == pygame.K_d:
                return "RIGHT"

        elif self.__controllerID == 1:
            if key == pygame.K_UP:
                return "UP"
            elif key == pygame.K_DOWN:
                return "DOWN"
            elif key == pygame.K_LEFT:
                return "LEFT"
            elif key == pygame.K_RIGHT:
                return "RIGHT"