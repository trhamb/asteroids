import pygame
from constants import *

def main():
    # Initialise PyGame Modules
    pygame.init()

    # Set up a display surface (here we pass in width and height from constants.py)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game Loop
    while True:
        # Check if the windows has been closed and kills the process if so
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
    screen.fill((0, 0, 0))
    pygame.display.flip()


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()