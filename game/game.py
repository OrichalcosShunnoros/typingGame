import pygame
from .settings import *
from .asteroid import Asteroid
from .ship import Ship
import sys

class Game :
    def __init__(self) :
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Asteroid Typing Game')
        self.clock = pygame.time.Clock()
        self.score = 0
        self.word_count = 0
        self.speed = INITIAL_SPEED
        self.level = 1
        self.asteroids = pygame.sprite.Group()
        self.ship = Ship()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.ship)

    def run(self) :
        while True :
            self.hdl_events()
            self.update()
            self.draw()

    def hdl_events(self) :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE] :
            pygame.quit()
            sys.exit()

        if keys[pygame.K_LEFT]  :
            self.ship.move(-5)

        if keys[pygame.K_RIGHT]:
            self.ship.move(5)

        if len(self.asteroids) < ASTEROID_LIMIT :
            asteroid = Asteroid()
            self.asteroids.add(asteroid)
            self.all_sprites.add(asteroid)

    def update(self):
        if self.level == 1 :
            self.speed = 1 
        else:
            self.speed = 5 

        self.asteroids.update(self.speed)

        for asteroid in self.asteroids :
            if asteroid.rect.colliderect(self.ship.rect) :
                typed_word = input(f"Type the word '{asteroid.word}': ")

                if typed_word == asteroid.word :
                    self.score += len(typed_word)
                    self.word_count += 1
                    asteroid.kill()

            if self.word_count >= self.level * SPEED_INCREASE_INTERVAL :
                self.speed += 1
                self.level += 1

    def draw(self) :
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        
        font = pygame.font.Font(None, 36)
        for asteroid in self.asteroids:
            word_surface = font.render(asteroid.word, True, (255, 255, 255))
            self.screen.blit(word_surface, (asteroid.rect.x, asteroid.rect.y))

        score_text = f"Score: {self.score} Words: {self.word_count} Level: {self.level}"
        text_surface = font.render(score_text, True, (255, 255, 255))
        self.screen.blit(text_surface, (10, 10))
        pygame.display.flip()
        self.clock.tick(FPS)
