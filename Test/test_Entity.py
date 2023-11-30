import pytest
import pygame
from Source.Game.Util import MyEntity

@pytest.mark.parametrize("x, y, z, width, height",[(10,20,30,40,50),(100,200,300,400,500),(0,0,0,1,1)])
def test_entity(x, y, z, width, height):
    
    entity = MyEntity(x, y, z, width, height)

    entity.setPositionX(x)
    entity.setPositionY(y)
    entity.setPositionZ(z)
    entity.setBody(width, height)

    assert entity.getPositionX() == x
    assert entity.getPositionY() == y
    assert entity.getPositionZ() == z
    assert entity.getBody() == [width, height]

    entity.shiftPosition(x,y,z)
    entity.setBody(2*width,2*height)

    assert entity.getPositionX() == 2*x
    assert entity.getPositionY() == 2*y
    assert entity.getPositionZ() == 2*z
    assert entity.getBody() == [2*width, 2*height]

    assert entity.getCollide([entity, entity, MyEntity(10000,10000,10000,0,0)]) == [entity,entity]

    

