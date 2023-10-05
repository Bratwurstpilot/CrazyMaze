import pygame


class PhysicsComponent:
    
    def __init__(self):

        self.__inPhysics : bool = False
        self.__velocityX : float = 0.0
        self.__velocityY : float = 0.0


    # Physics Model Functions


    def checkCollide(self, entity1, entity2) -> bool:

        entity1Position = entity1.getPosition()
        entity1Body = entity1.getBody()
        ENTITY1RECT = pygame.rect(entity1Position[0], entity1Position[1], entity1Body[0], entity1Body[1])

        entity2Position = entity2.getPosition()
        entity2Body = entity2.getBody()
        ENTITY2RECT = pygame.rect(entity2Position[0], entity2Position[1], entity2Body[0], entity2Body[1])


    def update(self, postion : list[int]) :

        return [postion[0] + self.__velocityX, postion[1] + self.__velocityY]


    # Get Methods


    def getPhysicState(self) -> bool:

        return self.getPhysicState