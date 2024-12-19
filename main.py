# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from circleshape import *

#initialize pygame
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = clock.tick(60) / 1000
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # dividing game objects into two groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    updatable.add(player)
    drawable.add(player)

    while True:  # Infinite loop
        pygame.Surface.fill(screen, (0, 0, 0))

        #iterate over updatable and drawable objects within the game loop
        for player in updatable:
            player.update(dt)
        for player in drawable:
            player.draw(screen)

        clock.tick(60)
        pygame.display.flip()
        for event in pygame.event.get(): # listening for events
            if event.type == pygame.QUIT: # if close window button is clicked
                return # closes pygame window
                


if __name__ == "__main__":
    main()