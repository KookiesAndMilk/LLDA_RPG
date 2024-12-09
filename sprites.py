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
        self.height = 59
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

    def limits(self, xa, xb, ya, yb):
        # Limits for Player
        if self.rect.x <= xa:
            self.rect.x = xa
        elif self.rect.x >= xb:
            self.rect.x =xb
        
        if self.rect.y <= ya:
            self.rect.y = ya
        elif self.rect.y >= yb:
            self.rect.y = yb

    def update(self):
        self.animation()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def door(self, x, y):
        self.rect.x = x
        self.rect.y = y

class Text(pygame.sprite.Sprite):
    def __init__(self, content, font, fg, fs, x, y):
        super(Text, self).__init__()
        self.content = content
        self.color = fg
        self.font_size = fs
        self.font = font
        self.font = pygame.font.Font(self.font, self.font_size)
        
        self.x_pad = 20
        self.y_pad = 13

        self.image = self.font.render(content, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    
    def update(self):
        pass

    def is_pressed(self, pos, pressed):
        if pos[0] in range (self.rect.left, self.rect.right) and pos [1] in range(self.rect.top, self.rect.bottom):
            if pressed[0]:
                return True
        return False