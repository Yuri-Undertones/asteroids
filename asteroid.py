import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (self.radius, self.radius), self.radius, 2)
        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))
        self.position = pygame.Vector2(x, y)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
        self.rect.center = self.position
          