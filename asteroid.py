import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        line_width = 2
        pygame.draw.circle(screen, "white", self.position, self.radius, line_width)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self, screen):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid_1.velocity = pygame.math.Vector2.rotate(self.velocity, angle) * 1.2
            asteroid_2.velocity = pygame.math.Vector2.rotate(self.velocity, -angle) * 1.2