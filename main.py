# this allows us to use code from the open-source pygame library throughout this file
# 
# 
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    # Set up the game window and clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Initialize sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign sprite groups to class containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Create game objects
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Initialize delta time
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Update the objects    
        updatable.update(dt)
        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game Over!")
                sys.exit()
        # Check for collisions between shots and asteroids
            for shot in shots:
                if shot.collide(asteroid):
                    shot.kill()
                    asteroid.split()

        # Fill the screen with black
        screen.fill("black")

        # Update drawable objects. This is where we draw the player and asteroids. 
        # We can use the sprite groups to update and draw all objects
        for obj in drawable:
            obj.draw(screen)
        
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