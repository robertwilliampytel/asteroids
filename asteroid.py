import pygame
import circleshape
import random
from   constants import *


class Asteroid(circleshape.CircleShape):

    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = random.randrange(ROTATION_MIN, ROTATION_MAX + 1, 1)


    def draw(self, screen):
        color_white = pygame.Color(255, 255, 255)
        pygame.draw.circle(screen, color_white, self.position, self.radius)
    

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        speed_multiplier = pygame.Vector2(ASTEROID_SPEED_MULTIPLIER * dt,
                                          ASTEROID_SPEED_MULTIPLIER * dt)
        self.position += forward * self.velocity * speed_multiplier

    
    def update(self, dt):
        self.move(dt)
