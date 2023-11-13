import pygame
import random

from Source.Game.Util import MyEntity, MyController
from Source.Engine.Label import Label


class otherTest:

    player = MyEntity(200, 700, 0)
    player.getTextureComponent().setTextureSet(["Source/Game/Files/KnightSprite1.png", "Source/Game/Files/KnightSprite2.png"])
    player.getTextureComponent().setFrameInterval(0.2)

    controller = MyController([player], 0)