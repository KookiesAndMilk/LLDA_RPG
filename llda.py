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

#### Object setup ####

# Display and Scene Management
INTRO = True
SALONIM3 = True

# Illustrations

main_menu_mel = pygame.image.load('img/main_menu_mel.png').convert_alpha()
main_menu_bg = pygame.image.load('img/main_menu_bg.png').convert()
title = Text("La Llave de Atrás",'dogicabold.ttf', c.WHITE, 32, 50, 30)
button = Text("Pulse 'ESPACIO' para comenzar", 'dogica.ttf', c.BLACK, 16, 200, 440)
text_group = pygame.sprite.Group()
text_group.add(button)
text_group.add(title)



# Sprites for Players or NPCs
mel = Player(200, 200, (c.BLACK), 'img/mel_spritesheet.png')

tah = NPC('img/tah_single.png', 570, 250)
eb = NPC('img/eb_single.png', 570, 450)
daniel = NPC('img/daniel_single.png', 530, 450)

sprite_group = pygame.sprite.Group()
sprite_group.add(mel)
sprite_group.add(tah)
sprite_group.add(eb)
sprite_group.add(daniel)

# Sprites for Scenes
bg_1 = BG('img/salon_piso.png', 120, 200, c.WHITE)
bg_2 = BG('img/salon_pared_im3.png', 120, 64, c.BLUE)
ass_1 = Asset('img/salon_banca1.png', 500, 340)
ass_2 = Asset('img/salon_banca1.png', 500, 400)
ass_3 = Asset('img/salon_bancas.png', 419, 400)
ass_4 = Asset('img/salon_bancas.png', 338, 400)
ass_5 = Asset('img/salon_bancas.png', 257, 400)
ass_6 = Asset('img/salon_banca1.png', 257, 340)

bg_group = pygame.sprite.Group()
bg_group.add(bg_2)
bg_group.add(bg_1)

sprite_group.add(ass_1)
sprite_group.add(ass_2)
sprite_group.add(ass_3)
sprite_group.add(ass_4)
sprite_group.add(ass_5)
sprite_group.add(ass_6)

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
        mel.limits()

        keys = pygame.key.get_pressed()
        if not keys:
            mel.vel_x = 0
            mel.vel_y = 0

        if keys[pygame.K_SPACE]:
            INTRO=False
            
        if keys[pygame.K_a]:
            mel.vel_x = - mel.speed
            mel.facing = 'left'
        elif keys[pygame.K_d]:
            mel.vel_x = + mel.speed
            mel.facing = 'right'
        elif keys[pygame.K_w]:
            mel.vel_y = - mel.speed
            mel.facing = 'up'
        elif keys[pygame.K_s]:
            mel.vel_y = + mel.speed
            mel.facing = 'down'
        else:
            mel.vel_x = 0
            mel.vel_y = 0

    # Update all the objects
    sprite_group.update()
    bg_group.update()

    # Check collissions
    if pygame.sprite.collide_rect(mel, tah):
        mel.vel_x = 0
        mel.vel_y = 0
    if pygame.sprite.collide_rect(mel, eb):
        mel.vel_x = 0
        mel.vel_y = 0
    if pygame.sprite.collide_rect(mel, daniel):
        mel.vel_x = 0
        mel.vel_y = 0
    if pygame.sprite.collide_rect(mel, ass_1):
        mel.vel_x = 0
        mel.vel_y = 0
    if pygame.sprite.collide_rect(mel, ass_2):
        mel.vel_x = 0
        mel.vel_y = 0
    if pygame.sprite.collide_rect(mel, ass_3):
        mel.vel_x = 0
        mel.vel_y = 0
    if pygame.sprite.collide_rect(mel, ass_4):
        mel.vel_x = 0
        mel.vel_y = 0
    if pygame.sprite.collide_rect(mel, ass_5):
        mel.vel_x = 0
        mel.vel_y = 0   
    
    # Check for Game Over

    # Render the Display
    if INTRO:
        DISPLAY.blit(main_menu_bg, (0,0))
        DISPLAY.blit(main_menu_mel, (0, 340))
        text_group.draw(DISPLAY)
    elif not INTRO:
        DISPLAY.fill(c.BLACK)
        bg_group.draw(DISPLAY)
        sprite_group.draw(DISPLAY)
    pygame.display.update()