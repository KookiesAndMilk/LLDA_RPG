import pygame
import config as c

class BG(pygame.sprite.Sprite):
    def __init__(self, file, x, y):
        super(BG, self).__init__()
        self.image = pygame.image.load(file).convert()
        self.image = pygame.transform.scale_by(self.image, (self.image.get_width()*0.011, self.image.get_height()*0.011))
        self.image.set_colorkey(c.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

class Asset(pygame.sprite.Sprite):
    def __init__(self, file, x, y):
        super(Asset, self).__init__()
        self.image = pygame.image.load(file).convert()
        self.image = pygame.transform.scale_by(self.image, (self.image.get_width()*0.011, self.image.get_height()*0.022))
        self.image.set_colorkey(c.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass