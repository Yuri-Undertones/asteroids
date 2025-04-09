import pygame
from constants import *
from circleshape import *
from player import *

def main():
    pygame.init()
    running = True
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player.update(dt)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
    


if __name__ == "__main__":
    main()