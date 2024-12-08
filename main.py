import pygame
from sprites import *
import config as c
import sys

main_menu_bg = pygame.image.load('img/main_menu_mel.png')

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((c.DISPLAY_WIDTH, c.DISPLAY_HEIGHT))
        self.screen.fill(c.WHITE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font('dogica.ttf', 32)
        
        self.character_spritesheet = Spritesheet('img/mel_spritesheet.png')
        self.terrain_spritesheet = Spritesheet('img/terrain1.png')

    def createTilemap(self):
        for i, row in enumerate(c.TILEMAP):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "W":
                    Block(self, j, i, 32, 0)
                if column == "E":
                    Block(self, j, i, 64, 0)
                if column == "T":
                    Block(self, j, i, 287, 0)
                if column == "2":
                    Block(self, j, i, 96, 0)
                if column == "1":
                    Block(self, j, i, 128, 0)
                if column == "P":
                    Player(self, j, i)

    def new(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.screen.blit(self.createTilemap(), 120, 120)
        self.playing = True

    def events(self):
        # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        # game loop updates
        self.all_sprites.update()
        
    def draw(self):
        # game loop draw
        self.screen.fill(c.BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(c.FPS)
        pygame.display.update()


    def main(self): # basically all the game happening.
        # game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def game_over(self):
        pass
    def intro_screen(self):
        intro = True

        title = self.font.render('La Llave de Atrás', True, c.BLACK)
        title_rect = title.get_rect(x=10, y=10)

        play_button = Button(c.DISPLAY_WIDTH//2-100, c.DISPLAY_HEIGHT//2, 200, 100, c.WHITE, c.BLACK, 'Jugar', 32)

        while intro:
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False

            self.screen.blit(main_menu_bg, (0,340))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(c.FPS)
            pygame.display.update()

g = Game()
g.intro_screen()
g.new()

while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()