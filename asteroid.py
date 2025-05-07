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

    def split(self):
        self.kill()
        # Split the asteroid into smaller ones
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        import random
        angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(angle)
        velocity2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2 * 1.2