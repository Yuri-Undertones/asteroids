import pygame
from circleshape import CircleShape
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        surface_size = int(PLAYER_RADIUS * 2 * 1.2)
        self.image = pygame.Surface((surface_size, surface_size), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center = (x, y))
        self.rotation = 0
        self.radius = PLAYER_RADIUS
        self.position = pygame.Vector2(x, y)
        self.circle = CircleShape(x, y, self.radius)
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotation += PLAYER_TURN_SPEED * dt
            self.rotation %= 360
        if keys[pygame.K_d]:
            self.rotation -= PLAYER_TURN_SPEED * dt
            self.rotation %= 360
        if keys[pygame.K_w]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position += forward * PLAYER_SPEED * dt
        if keys[pygame.K_s]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position -= forward * PLAYER_SPEED *dt
            
        self.rect.center = self.position
        self.image.fill((0, 0, 0, 0))
        triangle_vertices = [
            (v.x - self.rect.left, v.y - self.rect.top) for v in self.triangle()
        ]  
        pygame.draw.polygon(self.image, "white", triangle_vertices, 2)
       
    