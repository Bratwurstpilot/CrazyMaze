from __future__ import annotations
import pygame

from Source.Engine.Label import Label
from Source.Engine.Button import Button

class Menu:
    
    entities : list = []
    animations : list = []
    uiEntities : list = []

    background = pygame.image.load("Source/Game/Files/MainBackground.png")

    gameTitle = Label(1920//2, 440, 0, 1, 1, "Crazy Maze", (0, 110, 18), 70)
    gameTitle.setTextRect()
    uiEntities.append(gameTitle)

    volume = Button(1920//2 - 150, 490, 0, 300, 50, "Spiel erstellen", (0, 110, 18), 40)
    volume.setTextRect()
    uiEntities.append(volume)
    
    menu = Button(1920//2 - 150, 550, 0, 300, 50, "Optionen", (0, 110, 18), 40)
    menu.setTextRect()
    uiEntities.append(menu)
    
