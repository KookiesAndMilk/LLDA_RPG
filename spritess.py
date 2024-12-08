import pygame
import pygame.surface
import config as c
import math
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, file, x, y):
        super(Player, self).__init__()
        self.image = pygame.image.load(file).convert()
        self.image = pygame.transform.scale_by(self.image, (self.image.get_width()*0.15, self.image.get_height()*0.1))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = c.PLAYER_SPEED
        self.vel_x = 0
        self.vel_y = 0
        self.image.set_colorkey(c.WHITE)
        self.facing = 'down'

    def movement(self):
        keys = pygame.key.get_pressed()
        if not keys:
            self.vel_x = 0
            self.vel_y = 0
        if keys[pygame.K_a]:
            self.vel_x = - self.speed
            self.facing = 'left'
        elif keys[pygame.K_d]:
            self.vel_x = + self.speed
            self.facing = 'right'
        elif keys[pygame.K_w]:
            self.vel_y = - self.speed
            self.facing = 'up'
        elif keys[pygame.K_s]:
            self.vel_y = + self.speed
            self.facing = 'down'
        else:
            self.vel_x = 0
            self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y