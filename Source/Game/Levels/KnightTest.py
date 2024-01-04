from Source.Game.Util import MyEntity, MyController2
from Source.Engine.Scene import Scene

class KnightTest:

    def __init__(self):

        self.entities : list = []


object = KnightTest()
gameScene = None
controllers = []

def setup(screen):

    global object
    global gameScene
    global controllers

    texPath1 : str = "Source/Game/Files/KnightSprite1.png"
    texPath2 : str = "Source/Game/Files/KnightSprite2.png"

    knight = MyEntity(300, 300)
    knight.textureComp.setTextureSet([texPath1, texPath2])
    knight.textureComp.setFrameInterval(0.5)
    object.entities.append(knight)

    controller = MyController2([knight])
    controllers.append(controller)

    gameScene = Scene(screen, object.entities, [], None)