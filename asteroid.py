import pygame
import circleshape
import random
from   constants import *


class Asteroid(circleshape.CircleShape):

    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        color_white = pygame.Color(255, 255, 255)
        pygame.draw.circle(screen, color_white, self.position, self.radius, 2)
    

    def move(self, dt):
        self.position += self.velocity * dt

    
    def update(self, dt):
        self.move(dt)


    def split(self):

        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        random_angle_one = self.velocity.rotate(random_angle)
        random_angle_two = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_one.velocity = random_angle_one * 1.5
        asteroid_two.velocity = random_angle_two * 1.5
