import pygame

class Ship(pygame.sprite.Sprite) :
    def __init__(self) :
        super().__init__()
        self.image = pygame.Surface((60, 30))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)

    def move(self, dx) :
        self.rect.x += dx
        self.rect.x = max(0, min(800 - self.rect.width, self.rect.x))
