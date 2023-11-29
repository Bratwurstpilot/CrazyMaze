import random

from Source.Engine.Entity import Entity


class Agent(Entity):

    def __init__(self):
        
        super().__init__(500, 500, 1, 50, 50, True, True, True)
        self.tick = 0
        self.tickMax = 144 * 0.5

        self.currentChoice = 0


    def update(self) -> None:

        if self.currentChoice == 0 and self.positionX < 1920 - 100:
            self.shiftPositionX(5)
        if self.currentChoice == 1 and self.positionX > 100:
            self.shiftPositionX(-5)
        if self.currentChoice == 2 and self.positionY < 1080 - 100:
            self.shiftPositionY(5)
        if self.currentChoice == 3 and self.positionY > 100:
            self.shiftPositionY(-5)

        self.tick += 1
        if self.tick < self.tickMax : return

        self.tick = 0
        self.currentChoice = random.randint(0,3)