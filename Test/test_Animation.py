import pytest
from Source.Engine.Animation import Animation
from Source.Game.Util import MyEntity

@pytest.mark.parametrize("x, y",[(10,20),(100,200),(0,0)])
def test_animation(x, y):
    animation = Animation()

    animation.setComponents([MyEntity(x, y), MyEntity(x+10, y+10)])
    animation.setTargetPositions([[x + 10, y + 20], [x + 30, y + 40]])

    
    initial_positions = [component.getPosition() for component in animation.getComponents()]
    animation.setActive()
    animation.update()
    updated_positions = [component.getPosition() for component in animation.getComponents()]

    assert initial_positions != updated_positions