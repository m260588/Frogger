import pygame
import random

MIN_SPEED = .5
MAX_SPEED = 3

class Truck(pygame.sprite.Sprite):
    def __init__(self, x, y, idx):
        super().__init__()
        self.image = pygame.image.load("../Final/sprites/truck1.png").convert()

        # reg log
        self.truck1 = pygame.image.load("../Final/sprites/truck1.png").convert()
        self.truck1 = pygame.transform.scale(self.truck1, (90,50))
        self.truck1.set_colorkey((0, 0, 0))
        #self.rect_reglog = self.reglog.get_rect()
        #self.speed_reglog = random.uniform(MIN_SPEED, MAX_SPEED)

        # #long log
        self.truck2 = pygame.image.load("../Final/sprites/truck2.png").convert()
        self.truck2 = pygame.transform.scale(self.truck2, (100,50))
        self.truck2.set_colorkey((0, 0, 0))
        # self.longlog.get_rect()

        #short log
        self.car1 = pygame.image.load("../Final/sprites/car1.png").convert()
        self.car1 = pygame.transform.scale(self.car1, (75,50))
        self.car1.set_colorkey((0, 0, 0))
        #self.rect_shortlog = self.shortlog.get_rect()

        self.car2 = pygame.image.load("../Final/sprites/car2.png").convert()
        self.car2 = pygame.transform.scale(self.car2, (75, 50))
        self.car2.set_colorkey((0, 0, 0))

        self.car3 = pygame.image.load("../Final/sprites/car3.png").convert()
        self.car3 = pygame.transform.scale(self.car3, (75, 50))
        self.car3.set_colorkey((0, 0, 0))

        if idx == 1:
            self.image = self.truck1
        elif idx == 2:
            self.image = self.truck2
        elif idx == 3:
            self.image = self.car1
        elif idx == 4:
            self.image = self.car2
        else:
            self.image = self.car3
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


cars = pygame.sprite.Group()