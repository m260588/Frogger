import pygame
import random

MIN_SPEED = .5
MAX_SPEED = 3

class TruckFlip(pygame.sprite.Sprite):
    def __init__(self, x, y, idx):
        super().__init__()
        self.image = pygame.image.load("../Final/sprites/truck1.png").convert()

        self.truck1 = pygame.image.load("../Final/sprites/truck1.png").convert()
        self.truck1 = pygame.transform.scale(self.truck1, (90, 50))
        self.truck1.set_colorkey((0, 0, 0))

        self.truck2 = pygame.image.load("../Final/sprites/truck2.png").convert()
        self.truck2 = pygame.transform.scale(self.truck2, (100, 50))
        self.truck2.set_colorkey((0, 0, 0))

        self.car1 = pygame.image.load("../Final/sprites/car1.png").convert()
        self.car1 = pygame.transform.scale(self.car1, (75, 50))
        self.car1.set_colorkey((0, 0, 0))

        self.car2 = pygame.image.load("../Final/sprites/car2.png").convert()
        self.car2 = pygame.transform.scale(self.car2, (75, 50))
        self.car2.set_colorkey((0, 0, 0))

        self.car3 = pygame.image.load("../Final/sprites/car3.png").convert()
        self.car3 = pygame.transform.scale(self.car3, (75, 50))
        self.car3.set_colorkey((0, 0, 0))

        if idx == 1:
            self.image = pygame.transform.flip(self.truck1, True, False)

        elif idx == 2:
            self.image = pygame.transform.flip(self.truck2, True, False)

        elif idx == 3:
            self.image = pygame.transform.flip(self.car1, True, False)

        elif idx == 4:
            self.image = pygame.transform.flip(self.car2, True, False)

        else:
            self.image = pygame.transform.flip(self.car3, True, False)

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = -random.uniform(MIN_SPEED, MAX_SPEED)


    def update(self):
        self.x += self.speed
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, surf):
        surf.blit(self.image, self.rect)


cars1 = pygame.sprite.Group()