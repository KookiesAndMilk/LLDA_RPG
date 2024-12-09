import pygame

class Arrow(pygame.sprite.Sprite):
    def __init__(self, file, x, y):
        super(Arrow, self).__init__()
        self.image = pygame.image.load(file).convert_alpha()
        self.image = pygame.transform.scale_by(self.image, (self.image.get_width()*0.03, self.image.get_height()*0.03))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

    def out(self):
        self.rect.x = 800
        self.rect.y = 800

    def get_in(self):
        self.rect.x = self.x
        self.rect.y = self.y