import pygame
import circleshape
from   constants import *


class Shot(circleshape.CircleShape):


    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.rotation = rotation 


    def draw(self, screen):
        color_white = pygame.Color(255, 255, 255)
        pygame.draw.circle(screen, color_white, self.position, self.radius)


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SHOOT_SPEED * dt


    def update(self, dt):
        self.move(dt)
