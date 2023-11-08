from Source.Engine.Entity import Entity
from Source.Engine.InputController import EntityController


class MyEntity(Entity):

    def __init__(self, positionX : int = 0, positionY : int = 0, positionZ : int = 0, bodyWidth : int = 100, bodyHeight : int = 100):

        super().__init__(positionX, positionY, positionZ, bodyWidth, bodyHeight, physics = True, sound = True, texture = True)


    def update(self) -> None:
        
        self.positionX += self.physicsComp.getMomentum()[0]
        self.positionY += self.physicsComp.getMomentum()[1]

        self.textureComp.update()


class MyController(EntityController):

    def __init__(self, entities : list[Entity] = [], id : int = 0):

        super().__init__(entities, id)

    def update(self) -> None:

        if "LEFT" in self.keysPressed:
            self.controlledEntities[0].shiftPositionX(-200)
        if "RIGHT" in self.keysPressed:
            self.controlledEntities[0].shiftPositionX(200)


class MyController2(EntityController):

    def __init__(self, entities : list[Entity] = [], id : int = 0):

        super().__init__(entities, id)

    def update(self) -> None:

        for entity in self.controlledEntities:
            entity.getPhysicsComponent().resetMomentum()

        if "LEFT" in self.keysPressed:
            for entity in self.controlledEntities:
                entity.getPhysicsComponent().setMomentumX(direction = -1)
        elif "RIGHT" in self.keysPressed:
            for entity in self.controlledEntities:
                entity.getPhysicsComponent().setMomentumX()

        if "UP" in self.keysPressed:
            for entity in self.controlledEntities:
                entity.getPhysicsComponent().setMomentumY(direction = -1)
        elif "DOWN" in self.keysPressed:
            for entity in self.controlledEntities:
                entity.getPhysicsComponent().setMomentumY()