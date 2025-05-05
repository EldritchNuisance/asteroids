import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):

    
    def __init__(self, x, y):
        # Call the parent class (CircleShape) constructor
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        
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
        # Get the current state of all keyboard keys
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # Rotate left (counter-clockwise)
            self.rotate(-dt)
            
        if keys[pygame.K_d]:
            # Rotate right (clockwise)
            self.rotate(dt)

        if keys[pygame.K_w]:
            # Move forward in the direction the player is facing
            self.move(dt)
            
        if keys[pygame.K_s]:
            # Move backward (opposite to the direction the player is facing)
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            # Attempt to shoot a projectile
            self.shoot()

        if self.timer > 0:
            # Decrease the shooting cooldown timer
            self.timer -= dt

    def shoot(self):
        if self.timer <= 0:  # Only shoot if cooldown is complete
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
                # create bullet code
            self.timer = PLAYER_SHOOT_COOLDOWN  # Reset timer after shooting
            return True  # or whatever you return when a shot is fired
        return False  # or whatever you return when a shot can't be fired        
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

