from Source.Game.Util import MyEntity, MyController2
from Source.Engine.Scene import Scene

import pygame

class KnightTest:

    def __init__(self):

        self.entities : list = []


object = KnightTest()
gameScene = None
controllers = []
createBackground = pygame.image.load("Source/Game/Files/createBackground.png")

def setup(screen):

    global object
    global gameScene
    global controllers

    texPath1 : str = "Source/Game/Files/Echse_1.png"
    texPath2 : str = "Source/Game/Files/Echse_2.png"

    knight = MyEntity(300, 300, 1)
    knight.textureComp.setTextureSet([texPath1, texPath2])
    knight.textureComp.setFrameInterval(0.5)
    object.entities.append(knight)

    rectangle = MyEntity(300,300,0,128,128)
    rectangle.getTextureComponent().color = (0, 0, 0)
    object.entities.append(rectangle)

    controller = MyController2([knight, rectangle])
    controllers.append(controller)

    gameScene = Scene(screen, object.entities, [], createBackground)