import pygame
import random
from   constants     import *
from   player        import *
from   asteroid      import *
from   asteroidfield import *
from   shot          import *


def main():

    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen         = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player         = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    updatables = pygame.sprite.Group()
    drawables  = pygame.sprite.Group()
    asteroids  = pygame.sprite.Group()
    shots      = pygame.sprite.Group()

    updatables.add(player)
    drawables.add(player)

    Asteroid.containers = (updatables, drawables, asteroids)

    updatables.add(asteroid_field)

    Shot.containers = (updatables, drawables, shots)
    
    color_black = pygame.Color(0, 0, 0)

    clock = pygame.time.Clock()
    dt    = 0
    sixty_fps = 60

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color_black)

        for updateable in updatables:
            updateable.update(dt)

        for asteroid in asteroids:
            if asteroid.has_collided_with(player):
                print("Game over!")
                return

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        dt = clock.tick(sixty_fps) / 1000




if __name__ == "__main__":
    main()
