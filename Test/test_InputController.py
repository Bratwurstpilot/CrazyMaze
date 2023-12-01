import pytest
import pygame
from Source.Game.Util import MyEntity,MyController2

@pytest.mark.parametrize("key",[(pygame.K_UP),(pygame.K_DOWN),(pygame.K_RIGHT),(pygame.K_LEFT)])
def test_entity_controller(key):

    player1 = MyEntity(200, 700, 0)
    player1.getTextureComponent().setTextureSet(["Source/Game/Files/KnightSprite1.png", "Source/Game/Files/KnightSprite2.png"])
    player1.getTextureComponent().setFrameInterval(0.5)
    
    controller = MyController2([player1])
    controller.setControllerID(1)

    initial_keys = controller.keysPressed.copy()
    controller.update_(pygame.K_UP, True)
    updated_keys = controller.keysPressed

    assert initial_keys != updated_keys

    controller.setControllerID(0)

    initial_keys = controller.keysPressed.copy()
    controller.update_(key, True)
    updated_keys = controller.keysPressed
    initial_keys.append(None)
    
    assert controller.controllerID == 0
    assert initial_keys == updated_keys

  