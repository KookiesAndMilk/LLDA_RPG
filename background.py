import pygame
import config as c

class BG(pygame.sprite.Sprite):
    def __init__(self, file, x, y, colour):
        super(BG, self).__init__()
        self.image = pygame.image.load(file).convert()
        self.image = pygame.transform.scale_by(self.image, (self.image.get_width()*0.011, self.image.get_height()*0.011))
        self.image.set_colorkey(colour)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

class Asset(pygame.sprite.Sprite):
    def __init__(self, file, x, y):
        super(Asset, self).__init__()
        self.image = pygame.image.load(file).convert_alpha()
        self.image = pygame.transform.scale_by(self.image, (self.image.get_width()*0.08, self.image.get_height()*0.07))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

class NPC(pygame.sprite.Sprite):
    def __init__(self, file, x, y):
        super(NPC, self).__init__()

        self.image = pygame.image.load(file).convert()
        self.image = pygame.transform.scale_by(self.image, (self.image.get_width()*0.08, self.image.get_height()*0.06))
        self.image.set_colorkey(c.WHITE)
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def update(self):
        pass 