import pytest
import pygame
from Source.Engine.Physics import PhysicsComponent  
from Source.Game.Util import MyEntity

@pytest.mark.parametrize("momX, momY, x, y",[(10,10,100,100),(0,10,150,150),(10,0,1000,1000),(0,0,500,500)])
def test_phyics(momX, momY,x,y):

    physics_component = PhysicsComponent()

    physics_component.setMomentumX(momX)
    physics_component.setMomentumY(momY)

    assert physics_component.checkCollide(MyEntity(),MyEntity(x,y)) == False
    assert physics_component.getMomentum() == [5.0*momX , 5.0*momY]

    physics_component.resetMomentum()

    assert physics_component.getMomentum() == [0 , 0]