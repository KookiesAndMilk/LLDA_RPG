import pygame
import pygame.surface
import config as c
import math
import random

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert_alpha()
        self.sheet = pygame.transform.scale_by(self.sheet, (self.sheet.get_width()*0.0055, self.sheet.get_height()*0.062))
    
    def get_sprite(self, x, y, width, height, colour):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x,y, width, height))
        sprite.set_colorkey(colour)
        return sprite

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, colour, spritesheet_file):
        super(Player, self).__init__()
        self.width = 38
        self.height = 60
        self.colour = colour
        self.spritesheet = Spritesheet(spritesheet_file)
        self.animation_loop = 0
        self.vel_x = 0
        self.vel_y = 0

        self.image = self.spritesheet.get_sprite(0,0, self.width, self.height, colour)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = c.PLAYER_SPEED
        self.facing = 'down'

        self.down_animations = [
            self.spritesheet.get_sprite(0,0, self.width, self.height, colour),
            self.spritesheet.get_sprite(38,0, self.width, self.height, colour),
            self.spritesheet.get_sprite(76,0, self.width, self.height, colour),
            self.spritesheet.get_sprite(114,0, self.width, self.height, colour)
        ]

        self.up_animations = [
            self.spritesheet.get_sprite(152,0, self.width, self.height, colour),
            self.spritesheet.get_sprite(190,0, self.width, self.height, colour),
            self.spritesheet.get_sprite(228,0, self.width, self.height, colour),
            self.spritesheet.get_sprite(266,0, self.width, self.height, colour)
        ]

        self.right_animations = [
            self.spritesheet.get_sprite(456,0, self.width, self.height, colour),
            self.spritesheet.get_sprite(494,0, self.width, self.height, colour),
            self.spritesheet.get_sprite(532,0, self.width, self.height, colour),
            self.spritesheet.get_sprite(570,0, self.width, self.height, colour)
        ]

        self.left_animations = [
            self.spritesheet.get_sprite(304,0, self.width, self.height, colour),
            self.spritesheet.get_sprite(342,0, self.width, self.height, colour),
            self.spritesheet.get_sprite(380,0, self.width, self.height, colour),
            self.spritesheet.get_sprite(418,0, self.width, self.height, colour)
        ]
    
    def animation(self):
        animations = {
            'down': self.down_animations,
            'up': self.up_animations,
            'left': self.left_animations,
            'right': self.right_animations,
        }

        if self.facing in animations:
            anim = animations[self.facing]
            if (self.vel_y == 0 and self.facing in ['down', 'up']) or (self.vel_x == 0 and self.facing in ['left', 'right']):
                self.image = anim[0]
            else:
                self.image = anim[math.floor(self.animation_loop)]
                self.animation_loop += 0.3
                if self.animation_loop >= len(anim):
                    self.animation_loop = 0

    def limits(self):
                # Limits for Player
        if self.rect.x <= 120:
            self.rect.x = 120
        elif self.rect.x >= 635:
            self.rect.x =635
        
        if self.rect.y <= 175:
            self.rect.y = 175
        elif self.rect.y >= 550:
            self.rect.y = 550

    def update(self):
        self.animation()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y