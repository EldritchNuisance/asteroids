import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
    # pygame.draw.circle(surface, color, center, radius, width)
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Add velocity * dt to the position
        self.position += self.velocity * dt