import pytest
import pygame
from Source.Engine.Button import Button

@pytest.mark.parametrize("x, y",[(10,20),(100,200),(0,0)])
def test_button(x,y):

    button = Button(x,y)

    assert button.getText() == ""
    assert button.getRect() == pygame.Rect(100, 100, 100, 100)
    assert button.getBgColor() == (0, 0, 0)

    command ="""
        def f():
            return 10 
        """

    button.setTextSize(30)
    button.setText("TEST")
    button.setBgColor((255, 255, 255))
    button.setCommand(command)
 
    assert button.getPosition() == [x,y]
    assert button.getText() == "TEST"
    assert button.getBgColor() == (255, 255, 255)
    assert button.getCommand() == command,"command not setted"
