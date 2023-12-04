import pytest
import pygame
from Source.Engine.Label import Label

def test_label():
    label = Label()

    assert label.getText() == "Crazy Maze"
    assert label.getBgColor() == (0, 0, 0)

    label.setTextSize(25)
    label.setText("TEST")
    label.setBgColor((255, 255, 255))

    assert label.getText() == "TEST"
    assert label.getBgColor() == (255, 255, 255)
    assert isinstance(label.getTextFont(), pygame.Surface)
    assert isinstance(label.getRect(), pygame.Rect)
