import pygame

from Source.Game.Menu import Menu
from Source.Game.Create import Create
from Source.Engine.Scene import Scene
from Source.Engine.Screen import Screen

pygame.init()
infoObject = pygame.display.Info()
background = pygame.image.load("Source/Game/Files/MainBackground.png")
screen : pygame.display = Screen.setScreen(infoObject.current_w, infoObject.current_h, "")

mainMenu = Menu()
menuScene = Scene(screen, mainMenu.entities, mainMenu.uiEntities, background)

createGame = Create()
createScene = Scene(screen, createGame.entities, createGame.uiEntities, background)