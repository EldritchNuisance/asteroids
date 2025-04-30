import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)

    def draw(self, screen):
        pygame.draw.cirle(screen, "white", self.circle(), 2)

    def update(self, dt):
        