from __future__ import annotations

from Source.Engine.Animation import AnimationComponent
from Source.Engine.Physics import PhysicsComponent
from Source.Engine.Sound import SoundComponent
from Source.Engine.Texture import TextureComponent


class Entity:

    def __init__(self):

        self.__animationComp = AnimationComponent()
        self.__physicsComp = PhysicsComponent()
        self.__soundComp = SoundComponent()
        self.__textureComp = TextureComponent()
        #self.__controllComp = Controller(id : int = 0)

        self.__playable : bool = False

        self.__positionX : int = 0
        self.__positionY : int = 0
        self.__positionZ : int = 0
        
        self.__bodyWidth : int = 0
        self.__bodyHeight : int = 0

        self.__configSave : None = None


    # Update Process


    def update(self) -> None:
        
        self.__physicsComp.update()
        self.__animationComp.update(self.__textureComp)


    # Set Methods


    def setPlayable(self) -> None:

        self.__playable = True


    def setPositionX(self, xPosition : int) -> int:

        self.__positionX = xPosition
    

    def setPositionY(self, yPosition : int) -> int:

        self.__positionY = yPosition
    

    def setPositionZ(self, zPosition : int) -> int:

        self.__positionZ = zPosition


    def setPosition(self, positionX : int = 0, positionY : int = 0, positionZ : int = 0) -> int:

        self.__positionX = positionX
        self.__positionY = positionY
        self.__positionZ = positionZ

    
    def shiftPositonX(self, shift : int) -> int:

        self.__positionX += shift

    
    def shiftPositonY(self, shift : int) -> int:

        self.__positionY += shift

    
    def shiftPositonZ(self, shift : int) -> int:

        self.__positionY += shift

    
    def shiftPosition(self, positionX : int = 0, positionY : int = 0, positionZ : int = 0) -> int:

        self.__positionX += positionX
        self.__positionY += positionY
        self.__positionZ += positionZ
    

    def setBody(self, width : int = 100, height : int = 100) -> None:

        self.__bodyWidth = width
        self.__bodyHeight = height 

    
    def setBodyWidth(self, width : int) -> None:

        self.__bodyWidth = width


    def setBodyHeight(self, height : int) -> None:

        self.__bodyHeight = height

    
    def disablePlayable(self) -> None:

        self.__playable = False


    def setConfig(self, file : None) -> None:
        
        if self.__configSave != None : print("Overwriting Config on Entity " + self)
        self.__configSave = file
        #TODO Parse File Content 


    # Get Methods


    def getAnimationComponent(self) -> AnimationComponent:

        return self.__animationComp
    

    def getPhysicsComponent(self) -> PhysicsComponent:

        return self.__physicsComp


    def getTextureComponent(self) -> TextureComponent:

        return self.__textureComp
    

    def getSoundComponent(self) -> SoundComponent:

        return self.__soundComp
    

    def getPosition(self) -> list:

        return [self.__positionX, self.__positionY]
    

    def getPositionX(self) -> int:

        return self.__positionX
    

    def getPositionY(self) -> int:

        return self.__positionY
    

    def getPositionZ(self) -> int:

        return self.__positionZ
    

    def getBody(self) -> list:

        return [self.__bodyWidth, self.__bodyHeight]
    

    def getBodyWidth(self) -> int:

        return self.__bodyWidth
    
    
    def getBodyHeight(self) -> int:

        return self.__bodyHeight
    
    
    def getCollide(self, entities : list[Entity]) -> list:

        return [entity for entity in entities if self.checkCollide(entity) == True]


    def checkCollide(self, entity : Entity) -> list:

        return self.__physicsComp.checkCollide(self, entity)