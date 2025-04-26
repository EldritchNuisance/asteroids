import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):

    
    def __init__(self, x, y):
        # Call the parent class (CircleShape) constructor
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        
    #     # Initialize player-specific attributes
    #     self.color = (0, 255, 0)  # Green color for the player
    #     self.score = 0

    def draw(self, screen):
        # Draw the player as a circle
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        # Rotate the player based on the turn speed and time delta
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # Rotate left
            self.rotate(dt)
            
        if keys[pygame.K_d]:
            # Rotate right
            self.rotate(-dt)

        if keys[pygame.K_w]:
            # Move forward
            self.move(dt)
            
        if keys[pygame.K_s]:
            # Move backward
            self.move(-dt)
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt