from abc import ABC, abstractmethod

from Source.Engine.Entity import Entity
import pygame


class EntityController(ABC):

    '''
    An Entity controller can be called in the games lifespan
    and handles all inputs made by the user by default.

    It works with controller ID's = 
    0 -> [WASD]               Controlls
    1 -> [UP RIGHT DOWN LEFT] Controlls
    '''

    def __init__(self, entities : list[Entity] = [], id : int = 0) -> None:

        self.controlledEntities : list[Entity] = entities
        self.keysPressed : list[str] = []
        self.controllerID : int = id
    

    @abstractmethod
    def update(self, key) -> None:

        '''
        update is an abstract method which is given the pressed key
        in form : "UP", "DOWN", "LEFT" or "RIGHT"
        '''
        pass
    

    def update_(self, key, mode : bool) -> None:
        
        '''
        The Controller expects to get the key by the main program
        and does the job to evaluate the pressed key.
        '''
        input = self.processInput(key)
        
        if not mode and input in self.keysPressed:
            self.keysPressed.remove(input)

        elif input not in self.keysPressed:
            self.keysPressed.append(input)

        self.update()
    

    # Set Methods

    
    def setControllerScript(self, script : str) -> None:

        pass


    def setControllerID(self, id : int) -> None:

        self.controllerID = id


    # Get Methods


    def processInput(self, key) -> None:

        if self.controllerID == 0:
            if key == pygame.K_w:
                return "UP"
            elif key == pygame.K_s:
                return "DOWN"
            elif key == pygame.K_a:
                return "LEFT"
            elif key == pygame.K_d:
                return "RIGHT"

        elif self.controllerID == 1:
            if key == pygame.K_UP:
                return "UP"
            elif key == pygame.K_DOWN:
                return "DOWN"
            elif key == pygame.K_LEFT:
                return "LEFT"
            elif key == pygame.K_RIGHT:
                return "RIGHT"