import pygame
import random
from   constants     import *
from   player        import *
from   asteroid      import *
from   asteroidfield import *


def main():

    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen         = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player         = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    updatable.add(player)
    drawable.add(player)

    Asteroid.containers = (updatable, drawable, asteroids)

    updatable.add(asteroid_field)
    
    color_black = pygame.Color(0, 0, 0)

    clock = pygame.time.Clock()
    dt    = 0
    sixty_fps = 60

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color_black)

        for update in updatable:
            update.update(dt)

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()

        dt = clock.tick(sixty_fps) / 1000




if __name__ == "__main__":
    main()
