import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        
        random_angle = random.uniform(20, 50)
        
        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius / 2)
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius / 2)
        
        asteroid1.velocity = self.velocity.rotate(random_angle)
        asteroid2.velocity = self.velocity.rotate(-random_angle)

        return [asteroid1, asteroid2]