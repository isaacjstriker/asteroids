# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import everything from constants.py
from constants import *

#initialize pygame
def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:  # Infinite loop
        for event in pygame.event.get(): # listening for events
            if event.type == pygame.QUIT: # if close window button is clicked
                return # closes pygame window
        pygame.Surface.fill(screen, (0, 0, 0))
        pygame.display.flip()
                


if __name__ == "__main__":
    main()