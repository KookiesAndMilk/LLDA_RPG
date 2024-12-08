import pygame
import pygame.surface
import config as c
import math
import random

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(c.BLACK)
        return sprite

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = c.PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * c.TILESIZE
        self.y = y * c.TILESIZE
        self.width = c.PLAYER_WIDTH
        self.height = c.PLAYER_HEIGHT

        self.facing = 'down'
        self.animation_loop = 0

        self.x_change = 0
        self.y_change = 0

        self.image = self.game.character_spritesheet.get_sprite(0, 0, c.PLAYER_WIDTH, c.PLAYER_HEIGHT)

        self.rect = self.image.get_rect()
        self.rect.x = self.x 
        self.rect.y = self.y
        
        self.down_animations = [
            self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
            self.game.character_spritesheet.get_sprite(21, 0, self.width, self.height),
            self.game.character_spritesheet.get_sprite(21, 0, self.width, self.height),
            self.game.character_spritesheet.get_sprite(42, 0, self.width, self.height),
            self.game.character_spritesheet.get_sprite(42, 0, self.width, self.height)
        ]

        self.up_animations = [
            self.game.character_spritesheet.get_sprite(0, 30, self.width, self.height),
            self.game.character_spritesheet.get_sprite(21, 30, self.width, self.height),
            self.game.character_spritesheet.get_sprite(21, 30, self.width, self.height),
            self.game.character_spritesheet.get_sprite(42, 30, self.width, self.height),
            self.game.character_spritesheet.get_sprite(42, 30, self.width, self.height)

        ]

        self.left_animations = [
            self.game.character_spritesheet.get_sprite(0, 60, self.width, self.height),
            self.game.character_spritesheet.get_sprite(21, 60, self.width, self.height),
            self.game.character_spritesheet.get_sprite(21, 60, self.width, self.height),
            self.game.character_spritesheet.get_sprite(42, 60, self.width, self.height),
            self.game.character_spritesheet.get_sprite(42, 60, self.width, self.height)

        ]

        self.right_animations = [
            self.game.character_spritesheet.get_sprite(0, 90, self.width, self.height),
            self.game.character_spritesheet.get_sprite(21, 90, self.width, self.height),
            self.game.character_spritesheet.get_sprite(21, 90, self.width, self.height),
            self.game.character_spritesheet.get_sprite(42, 90, self.width, self.height),
            self.game.character_spritesheet.get_sprite(42, 90, self.width, self.height)
        ]

    def update(self):
        self.movement()
        self.animation()

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += c.PLAYER_SPEED / 2
            self.x_change -= c.PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_d]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= c.PLAYER_SPEED / 2
            self.x_change += c.PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_w]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += c.PLAYER_SPEED / 2
            self.y_change -= c.PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_s]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= c.PLAYER_SPEED / 2
            self.y_change += c.PLAYER_SPEED
            self.facing = 'down'

    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                   self.rect.x = hits[0].rect.left - self.rect.width
                   for sprite in self.game.all_sprites:
                       sprite.rect.x += c.PLAYER_SPEED / 2
                if self.x_change < 0:
                   self.rect.x = hits[0].rect.right
                   for sprite in self.game.all_sprites:
                       sprite.rect.x -= c.PLAYER_SPEED / 2

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.game.all_sprites:
                       sprite.rect.y += c.PLAYER_SPEED / 2
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.game.all_sprites:
                       sprite.rect.y -= c.PLAYER_SPEED / 2

    def animation(self):

        if self.facing == 'down':
            if self.y_change == 0:
                self.image = self.down_animations[0]
            else:
                self.image = self.down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= len(self.down_animations):
                    self.animation_loop = 1

        elif self.facing == 'up':
            if self.y_change == 0:
                self.image = self.up_animations[0]
            else:
                self.image = self.up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= len(self.up_animations):
                    self.animation_loop = 1

        elif self.facing == 'left':
            if self.x_change == 0:
                self.image = self.left_animations[0]
            else:
                self.image = self.left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= len(self.left_animations):
                    self.animation_loop = 1

        elif self.facing == 'right':
            if self.x_change == 0:
                self.image = self.right_animations[0]
            else:
                self.image = self.right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= len(self.right_animations):
                    self.animation_loop = 1


class Block(pygame.sprite.Sprite):
    def  __init__(self, game, x, y, xx, yy):

        self.game = game
        self._layer = c.BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * c.TILESIZE
        self.y = y * c.TILESIZE
        self.width = c.TILESIZE
        self.height = c.TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(xx, yy, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = c.GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * c.TILESIZE
        self.y = y * c.TILESIZE
        self.width = c.TILESIZE
        self.height = c.TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Button:
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font('dogica.ttf', fontsize)
        self.content = content
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if pos[0] in range (self.rect.left, self.rect.right) and pos[1] in range (self.rect.top, self.rect.bottom) and pressed[0]:
            return True
        return False
