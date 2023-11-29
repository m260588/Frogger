#moving logs

import pygame
import random

MIN_SPEED = .5
MAX_SPEED = 3

class Log(pygame.sprite.Sprite):
    def __init__(self, x, y, idx):
        super().__init__()
        self.image = pygame.image.load("../Final/sprites/reglog.png").convert()

        # reg log
        self.reglog = pygame.image.load("../Final/sprites/reglog.png").convert()
        self.reglog = pygame.transform.scale(self.reglog, (90,50))
        self.reglog.set_colorkey((0, 0, 0))


        # #long log
        self.longlog = pygame.image.load("../Final/sprites/longlog.png").convert()
        self.longlog = pygame.transform.scale(self.longlog, (100,50))
        self.longlog.set_colorkey((0, 0, 0))


        #short log
        self.shortlog = pygame.image.load("../Final/sprites/shortlog.png").convert()
        self.shortlog = pygame.transform.scale(self.shortlog, (75,50))
        self.shortlog.set_colorkey((0, 0, 0))


        if idx == 1:
            self.image = self.reglog
        elif idx == 2:
            self.image = self.shortlog
        else:
            self.image = self.longlog
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)



    def update(self):
        self.x += self.speed
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, surf):
        surf.blit(self.image, self.rect)


logs = pygame.sprite.Group()