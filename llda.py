import pygame
from sprites import *
from background import *
import config as c

# Pygame Initialization
pygame.font.init()

# Display setup
DISPLAY = pygame.display.set_mode((c.DISPLAY_WIDTH, c.DISPLAY_HEIGHT))
FPS = 60
CLOCK = pygame.time.Clock()

# Object setup
# Sprites for Players or NPCs
sprite_group = pygame.sprite.Group()
mel = Player('img/mel_spritesheet.png', 200, 200)
tah = Player('img/tah_single.png', 160, 100)
eb = Player('img/eb_single.png', 220, 100)
daniel = Player('img/daniel_single.png', 280, 100)
sprite_group.add(mel)
sprite_group.add(tah)
sprite_group.add(eb)
sprite_group.add(daniel)

# Sprites for Scenes
bg_1 = BG('img/salon_piso.png', 120, 200)
bg_2 = BG('img/salon_pared.png', 120, 64)
ass_2 = Asset('img/salon_assets1.png', 120, 64)
bg_group = pygame.sprite.Group()
bg_group.add(bg_1)
bg_group.add(bg_2)
ass_group = pygame.sprite.Group()
ass_group.add(ass_2)

# The Game

running = True
while running:
    # Tick Clock
    CLOCK.tick(FPS)
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            quit()
        mel.movement()
        if mel.movement() == 'down':
            print('down')
        if mel.movement() == 'up':
            print('up')
        if mel.movement() == 'left':
            print('left')
        if mel.movement() == 'right':
            print('right')

    # Update all the objects
    sprite_group.update()
    bg_group.update()

    # Check collission

    # Check for Game Over

    # Render the Display
    DISPLAY.fill(c.BLACK)
    bg_group.draw(DISPLAY)
    ass_group.draw(DISPLAY) 
    sprite_group.draw(DISPLAY)
    pygame.display.update()