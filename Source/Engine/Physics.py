import pygame


class PhysicsComponent:

    '''
    The PhysicsComponent class can be used to derive
    some basic physical properties and behaviour.
    '''
    
    def __init__(self):

        self.__inPhysics : bool = False
        self.__velocityX : float = 5.0
        self.__velocityY : float = 5.0
        self.__momentum : list[float, float] = [0.0, 0.0]


    # Physics Model Functions


    def checkCollide(self, entity1, entity2) -> bool:

        entity1Position = entity1.getPosition()
        entity1Body = entity1.getBody()
        ENTITY1RECT = pygame.rect(entity1Position[0], entity1Position[1], entity1Body[0], entity1Body[1])

        entity2Position = entity2.getPosition()
        entity2Body = entity2.getBody()
        ENTITY2RECT = pygame.rect(entity2Position[0], entity2Position[1], entity2Body[0], entity2Body[1])


    # Set Methods 


    def setMomentumX(self, direction : int = 1) -> None:

        self.__momentum[0] = self.__velocityX * direction

    
    def setMomentumY(self, direction : int = 1) -> None:

        self.__momentum[1] = self.__velocityY * direction


    def setMomentum(self, directionX : int = 1, directionY : int = 1) -> None:

        self.__momentum[0] = self.__velocityX * directionX
        self.__momentum[1] = self.__velocityY * directionY


    def resetMomentum(self) -> None:

        self.__momentum = [0.0, 0.0]


    def resetMomentumX(self) -> None:


        self.__momentum[0] = 0.0

    def resetMomentumY(self) -> None:

        self.__momentum[1] = 0.0


    # Get Methods


    def getPhysicState(self) -> bool:

        return self.getPhysicState
    

    def getVelocityX(self) -> float:

        return self.__velocityX
    

    def getVelocityY(self) -> float:

        return self.__velocityY
    

    def getVelocity(self) -> float:

        return [self.__velocityX, self.__velocityY]
    

    def getMomentum(self) -> list[float, float]:

        #TODO Calculate Collisions and block momentum
        return self.__momentum