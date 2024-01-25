from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty

from Source.Engine.Physics import PhysicsComponent
from Source.Engine.Sound import SoundComponent
from Source.Engine.Texture import TextureComponent


class Entity(ABC):

    '''
    Entity is a base class which can be inherited from to get the
    minimal setup to render an element on the screen.
    
    One needs to define an update method, which is an abstract method.

    An Entity can have one or no of the following predefined components:

    - PhysicsComponent
    - SoundComponent
    - TextureComponent
    '''

    def __init__(self, positionX : int = 0, positionY : int = 0, positionZ : int = 0, bodyWidth : int = 100, bodyHeight : int = 100,
                 physics = False, sound = False, texture = False):

        self.physicsComp = PhysicsComponent(self)
        self.soundComp = SoundComponent()
        self.textureComp = TextureComponent()

        self.positionX : int = positionX
        self.positionY : int = positionY
        self.positionZ : int = positionZ
        
        self.bodyWidth : int = bodyWidth
        self.bodyHeight : int = bodyHeight

        self.configSave : None = None


    # Update Process

    @abstractmethod
    def update(self) -> None:
        
        '''
        self.physicsComp.update()
        
        self.positionX += self.physicsComp.getMomentum()[0]
        self.positionY += self.physicsComp.getMomentum()[1]

        self.textureComp.update()

        The update method is called once per game cycle and may be defined
        by an inhereting class
        '''
        pass


    # Set Methods


    def setPositionX(self, xPosition : int) -> None:

        self.positionX = xPosition
    

    def setPositionY(self, yPosition : int) -> None:

        self.positionY = yPosition
    

    def setPositionZ(self, zPosition : int) -> None:

        self.positionZ = zPosition


    def setPosition(self, positionX : int = 0, positionY : int = 0, positionZ : int = 0) -> None:

        self.positionX = positionX
        self.positionY = positionY
        self.positionZ = positionZ

    
    def shiftPositionX(self, shift : int) -> None:

        self.positionX += shift

    
    def shiftPositionY(self, shift : int) -> None:

        self.positionY += shift

    
    def shiftPositionZ(self, shift : int) -> None:

        self.positionY += shift

    
    def shiftPosition(self, positionX : int = 0, positionY : int = 0, positionZ : int = 0) -> None:

        self.positionX += positionX
        self.positionY += positionY
        self.positionZ += positionZ
    

    def setBody(self, width : int = 100, height : int = 100) -> None:

        self.bodyWidth = width
        self.bodyHeight = height 

    
    def setBodyWidth(self, width : int) -> None:

        self.bodyWidth = width


    def setBodyHeight(self, height : int) -> None:

        self.bodyHeight = height


    # Get Methods
    

    def getPhysicsComponent(self) -> PhysicsComponent:

        return self.physicsComp


    def getTextureComponent(self) -> TextureComponent:

        return self.textureComp
    

    def getSoundComponent(self) -> SoundComponent:

        return self.soundComp
    

    def getPosition(self) -> list:

        return [self.positionX, self.positionY]
    

    def getPositionX(self) -> int:

        return self.positionX
    

    def getPositionY(self) -> int:

        return self.positionY
    

    def getPositionZ(self) -> int:

        return self.positionZ
    

    def getBody(self) -> list:

        return [self.bodyWidth, self.bodyHeight]
    

    def getBodyWidth(self) -> int:

        return self.bodyWidth
    
    
    def getBodyHeight(self) -> int:

        return self.bodyHeight
    
    
    def getCollide(self, entities : list[Entity]) -> list:

        return [entity for entity in entities if self.checkCollide(entity) == True]


    def checkCollide(self, entity : Entity) -> list:

        return self.physicsComp.checkCollide(self, entity)