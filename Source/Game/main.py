from Source.Engine.Entity import Entity
import pygame

def main():
    
    entt = Entity()

    pygame.init()
    screen = pygame.display.set_mode([500, 500])
    running = True
    clock = pygame.time.Clock()

    timer = 0
    limit = 144
    sound = pygame.mixer.Sound("CrazyMaze/Dependencies/Sounds/test.wav") # Selbst erstellter Sound, kein Copyright

    from Source.Engine.UtilFile import File
    print(File.getContentSplit("CrazyMaze/Dependencies/Files/TestFile.txt", ";"))
    print(File.getContentRaw("CrazyMaze/Dependencies/Files/TestFile.txt"))
    

    # crappy pygame test

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
        pygame.display.flip()

        timer += 1
        if timer >= limit:
            entt.getSoundComponent().play(sound)
            timer = 0

        clock.tick(144)

    pygame.quit()