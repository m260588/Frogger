#moving logs

import pygame
import random

MIN_SPEED = .5
MAX_SPEED = 3

class Log(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        #self.reglog
        #self.longlog
        self.image = pygame.image.load("../Final/sprites/reglog.png").convert()
        # change image later on
        self.reglog = pygame.image.load("../Final/sprites/reglog.png").convert()
        self.reglog.set_colorkey((0,0,0))
        self.rect_reglog = self.reglog.get_rect()
        self.speed_reglog = random.uniform(MIN_SPEED, MAX_SPEED)

        self.x = x
        self.y = y
        #self.rect.center (x,y)

        self.longlog = pygame.image.load("../Final/sprites/longlog.png").convert()
        self.longlog.set_colorkey((0, 0, 0))
        self.rect_longlog = self.longlog.get_rect()
        self.speed_longlog = random.uniform(MIN_SPEED, MAX_SPEED)

        self.shortlog = pygame.image.load("../Final/sprites/shortlog.png").convert()
        self.shortlog.set_colorkey((0, 0, 0))
        self.rect_shortlog = self.shortlog.get_rect()
        self.speed_shortlog = random.uniform(MIN_SPEED, MAX_SPEED)

    def update(self):
        self.x += self.speed_shortlog
        self.x += self.speed_reglog
        self.x += self.speed_longlog
        self.rect_longlog.x = self.x
        self.rect_shortlog = self.x
        self.rect_reglog = self.x

    def draw(self, surf):
        surf.blit(self.longlog, self.rect_longlog)
        surf.blit(self.reglog, self.rect_reglog)
        surf.blit(self.shortlog, self.rect_shortlog)

logs = pygame.sprite.Group()