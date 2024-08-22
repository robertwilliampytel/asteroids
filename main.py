import pygame
from   constants import *
from   player    import *


def main():

    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
    color_black = pygame.Color(0, 0, 0)

    clock = pygame.time.Clock()
    dt    = 0
    sixty_fps = 60

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color_black)

        player.draw(screen)
        player.update(dt)

        pygame.display.flip()

        dt = clock.tick(sixty_fps) / 1000




if __name__ == "__main__":
    main()
