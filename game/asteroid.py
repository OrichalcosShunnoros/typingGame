import pygame
import random

class Asteroid(pygame.sprite.Sprite) :
    def __init__(self) :
        super().__init__()
        self.image = pygame.Surface((random.randint(40, 100), random.randint(40, 100)))
        self.image.fill((0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800 - self.rect.width)
        self.rect.y = random.randint(-100, -40)

        self.word = self.gen_word()

    def gen_word(self) :
        length = random.randint(3, 10)
        return ''.join(random.choices('abcdefghijklmnñopqrstuvwxyz', k=length))

    def update(self, speed) :
        self.rect.y += speed

        if self.rect.y > 600 :
            self.kill()
