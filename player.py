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