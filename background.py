import pygame
import config as c

class BG(pygame.sprite.Sprite):
    def __init__(self, file, x, y, colour):
        super(BG, self).__init__()
        self.image = pygame.image.load(file).convert()
<<<<<<< HEAD
        self.image = pygame.transform.scale_by(self.image, (self.image.get_width()*0.011, self.image.get_height()*0.011))
=======
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image = pygame.transform.scale_by(self.image, (self.width*0.011, self.height*0.011))
>>>>>>> 9a19b6ee5ecabc4bb45ba2f37ee36b50ab591438
        self.image.set_colorkey(colour)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

    def scale_by(self, mult_x, mult_y):
        self.image = pygame.transform.scale_by(self.image, (self.width*mult_x, self.height*mult_y))

class Asset(pygame.sprite.Sprite):
    def __init__(self, file, x, y):
        super(Asset, self).__init__()
        self.image = pygame.image.load(file).convert_alpha()
        self.image = pygame.transform.scale_by(self.image, (self.image.get_width()*0.08, self.image.get_height()*0.07))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y

    def update(self):
        pass

    def out(self):
        self.rect.x = 800
        self.rect.y = 800

    def get_in(self):
        self.rect.x = self.x
        self.rect.y = self.y

class NPC(pygame.sprite.Sprite):
    def __init__(self, file, x, y):
        super(NPC, self).__init__()

        self.image = pygame.image.load(file).convert()
        self.image = pygame.transform.scale_by(self.image, (self.image.get_width()*0.08, self.image.get_height()*0.06))
        self.image.set_colorkey(c.WHITE)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.x = self.rect.x
        self.rect.y = y
        self.y = self.rect.y

    def update(self):
        pass 

    def out(self):
        self.rect.x = 800
        self.rect.y = 800

    def get_in(self):
        self.rect.x = self.x
        self.rect.y = self.y