# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    # Set up the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate to 60 FPS
        # and calculate the time since the last frame
        # This is useful for controlling the speed of the game
        # and for smooth animations
        # dt is the time since the last frame in seconds
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()