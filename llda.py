import pygame
from sprites import *
from background import *
from arrows import Arrow
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
PASILLO = False

# Main Menu Setup

main_menu_mel = pygame.image.load('img/terrain/main_menu_mel.png').convert_alpha()
main_menu_bg = pygame.image.load('img/terrain/main_menu_bg.png').convert()
title = Text("La Llave de Atrás",'dogicabold.ttf', c.WHITE, 32, 50, 30)
button = Text("Pulse 'ESPACIO' para comenzar", 'dogica.ttf', c.BLACK, 16, 200, 440)
text_group = pygame.sprite.Group()
text_group.add(button)
text_group.add(title)

# Sprites for Players or NPCs

mel = Player(400, 250, (c.BLACK), 'img/walking_sprites/mel_spritesheet.png')

tah = NPC('img/walking_sprites/tah_single.png', 570, 250)
eb = NPC('img/walking_sprites/eb_single.png', 570, 450)
daniel = NPC('img/walking_sprites/daniel_single.png', 530, 450)

sprite_group_1 = pygame.sprite.Group()
sprite_group_1.add(mel)
sprite_group_1.add(tah)
sprite_group_1.add(eb)
sprite_group_1.add(daniel)

# Usables

arrow_up = Arrow('img/assets/teleporter_up.png', 230, 200)
arrow_down = Arrow('img/assets/teleporter_down.png', 800, 800)
arrow_left = Arrow('img/assets/teleporter_left.png', 800, 800)
arrow_right = Arrow('img/assets/teleporter_right.png', 800, 800)

sprite_group_1.add(arrow_up)

# Sprites for Scenes
bg_1 = BG('img/terrain/salon_piso.png', 120, 200, c.WHITE)
bg_2 = BG('img/terrain/salon_pared_im3.png', 120, 64, c.BLUE)
ass_1 = Asset('img/assets/salon_banca1.png', 500, 340)
ass_2 = Asset('img/assets/salon_banca1.png', 500, 400)
ass_3 = Asset('img/assets/salon_bancas.png', 419, 400)
ass_4 = Asset('img/assets/salon_bancas.png', 338, 400)
ass_5 = Asset('img/assets/salon_bancas.png', 257, 400)
ass_6 = Asset('img/assets/salon_banca1.png', 257, 340)

bg_3 = BG('img/terrain/pasillo.png', 120, 64, c.BLACK)

bg_group_1 = pygame.sprite.Group()
bg_group_1.add(bg_1, bg_2)

bg_group_2 = pygame.sprite.Group()

sprite_group_1.add(ass_1, ass_2, ass_3, ass_4, ass_5, ass_6)

################## THE GAME ##################

running = True
while running:

    # Tick Clock
    
    CLOCK.tick(FPS)
    
    # Handle Events
    
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            quit()
        if event.type == pygame.key:
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                running = False
                quit()

        # Player movement
        if SALONIM3:
            mel.limits(120, 630, 180, 550)

        if not keys:
            mel.vel_x = 0
            mel.vel_y = 0
        
        # Go from Main Menu
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

    sprite_group_1.update()
    bg_group_1.update()
    bg_group_2.update()

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
    if pygame.sprite.collide_rect(mel, arrow_up):
        bg_group_1.add(bg_3)
        bg_group_1.remove(bg_1, bg_2)
        sprite_group_1.remove(ass_1, ass_2, ass_3, ass_4, ass_5, ass_6)
        sprite_group_1.remove(arrow_up)
        
    # Check for Game Over

    # Render the Display
    if INTRO:
        SALONIM3 = False
        DISPLAY.blit(main_menu_bg, (0,0))
        DISPLAY.blit(main_menu_mel, (0, 340))
        text_group.draw(DISPLAY)
    elif not INTRO:
        SALONIM3=True
        DISPLAY.fill(c.BLACK)
    if SALONIM3:
        bg_group_1.draw(DISPLAY)
        sprite_group_1.draw(DISPLAY)
    pygame.display.update()