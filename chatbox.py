import pygame
from sprites import Text

class Pfp(pygame.sprite.Sprite):
    def __init__(self, file, colour):
        super(Pfp, self).__init__()
        self.pfp = pygame.image.load(file).convert_alpha()
        self.pfp.set_colorkey(colour)

    def box(self, text):
        box = pygame.Surface([300,100])
        box.blit(self.pfp, (0,0))
    

    def update(self):
        pass
        