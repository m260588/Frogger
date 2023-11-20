import pygame
from game_parameters import *


frog_frames = [pygame.image.load("../Final/sprites/frogjump1.png"),pygame.image.load("../Final/sprites/frogjump2.png"),pygame.image.load("../Final/sprites/frogjump3.png"),pygame.image.load("../Final/sprites/frogjump4.png")]

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        #TODO turn fish in opposite direction
        self.image = pygame.image.load("../Final/sprites/frogjump1.png").convert()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.image_flip = pygame.transform.flip(self.image, False, True)
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0

    def move_up(self):
        self.y_speed = -PLAYER_SPEED
    def move_down(self):
        self.y_speed = PLAYER_SPEED
    def move_right(self):
        self.x_speed = PLAYER_SPEED
        self.image = pygame.image.load("../Final/sprites/frogjump1.png").convert()
        self.image.set_colorkey((0, 0, 0))
    def move_left(self):
        self.x_speed = -PLAYER_SPEED
        self.image = self.image_flip

    def stop(self):
        self.x_speed = 0
        self.y_speed = 0
    def update(self):
        #TODO need to check if player fish goes off the screen (stop it from going off)
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > screen_width-tile_size:
            self.rect.x = screen_width-tile_size
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > screen_height-tile_size:
            self.rect.y = screen_height-tile_size

    def draw(self, surf):
        surf.blit(self.image, self.rect)

# RGB = (10,150,150)
# color =(247,247,247)
#
#
# class Player(pygame.sprite,Sprite):
#
#     def __init__(self, x, y):
#         self.image = pygame.image.load("../assests/sprites/orange_fish.png").convert()
#         self.image.set_colorkey((0, 0, 0))
#         self.rect = self.image.get_rect()
#         self.image_flip = pygame.transform.flip(self.image, False, True)
#         self.x = x
#         self.y = y
#         self.rect.center = (x, y)
#         self.x_speed = 0
#         self.y_speed = 0
#
#     screen.fill(RGB)
#
#     for x in range(len(frog_frames)):
#         screen.fill(RGB)
#         screen.blit(frog_frames[x], (75, 0))
#         pygame.display.flip()
#         clock.tick(10)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#
#     pygame.display.flip()
# pygame.quit()
