import pygame
from sprites import *
from background import *
from arrows import Arrow
from main_menu import mostrar_menu
import config as c
import random

# Pygame Initialization
pygame.font.init()

# Display setup
DISPLAY = pygame.display.set_mode((c.DISPLAY_WIDTH, c.DISPLAY_HEIGHT))
FPS = 60
CLOCK = pygame.time.Clock()
correcto = 0
incorrecto = 0
adivinar = -1
opcion_correcta = random.randrange(0, 3)

#### Object setup ####

# Configuración de pantalla
screen = DISPLAY
pygame.display.set_caption("La llave de atrás")

# Reloj y fuentes
clock = pygame.time.Clock()
fuente = pygame.font.Font("dogica.ttf", 25)
fuente_bold = pygame.font.Font("dogicabold.ttf", 25)

# Carga de imágenes
imagen_fondo = pygame.image.load('img/terrain/main_menu_bg.png').convert_alpha()
imagen_mel = pygame.image.load('img/terrain/main_menu_mel.png').convert_alpha()

# Mostrar el menú
opcion = mostrar_menu(screen, clock, fuente, fuente_bold, imagen_fondo, imagen_mel)

if opcion == 0:
    print("Comenzar juego")
elif opcion == 1:
    print("Cargar partida")
elif opcion == 2:
    pygame.quit()

# Display and Scene Management

SALONIM3 = True
PASILLO = False

# Sprites for Players or NPCs

mel = Player(250, 250, (c.BLACK), 'img/walking_sprites/mel_spritesheet.png')

tah = NPC('img/walking_sprites/tah_single.png', 570, 250)
eb = NPC('img/walking_sprites/eb_single.png', 570, 450)
daniel = NPC('img/walking_sprites/daniel_single.png', 530, 450)

sprite_group = pygame.sprite.Group()
sprite_group.add(mel, tah, daniel, eb)

# Usables

arrow_up = Arrow('img/assets/teleporter_up.png', 230, 200)
arrow_down = Arrow('img/assets/teleporter_down.png', 300, 410)
arrow_left = Arrow('img/assets/teleporter_left.png', 120
                   , 480)
arrow_right = Arrow('img/assets/teleporter_right.png', 340, 370)

sprite_group.add(arrow_up)

# Sprites for Scenes
bg_1 = BG('img/terrain/salon_piso.png', 120, 200, c.WHITE)
bg_2 = BG('img/terrain/salon_pared_im3.png', 120, 64, c.BLUE)

ass_1 = Asset('img/assets/salon_banca1.png', 500, 340)
ass_2 = Asset('img/assets/salon_banca1.png', 500, 400)
ass_3 = Asset('img/assets/salon_bancas.png', 419, 400)
ass_4 = Asset('img/assets/salon_bancas.png', 338, 400)
ass_5 = Asset('img/assets/salon_bancas.png', 257, 400)
ass_6 = Asset('img/assets/salon_banca1.png', 257, 340)

bg_3 = BG('img/terrain/pasillo.png', 197, 20, c.BLACK)
bg_3.scale_by(0.0248, 0.0055)

bg_4 = BG('img/terrain/salon_pared_im5.png', 120, 64, c.BLUE)
ass_7 = Asset('img/assets/salon_banca1.png', 500, 430) # Banca Alberto
ass_8 = Asset('img/assets/salon_banca3.png', 218, 400) # Banca Marco
ass_9 = Asset('img/assets/salon_banca1.png', 218, 230) # Banca Diego
ass_10 = Asset('img/assets/salon_banca1.png', 500, 230) # Banca Dania
ass_11 = Asset('img/assets/salon_bancas.png', 500, 525) # Escritorio

dania = NPC('img/walking_sprites/dania_single.png', 515, 200)
diego = NPC('img/walking_sprites/diego_single.png', 200, 210)
alberto = NPC('img/walking_sprites/alberto_single.png', 470, 400)
mario = NPC('img/walking_sprites/mario_single.png', 400, 505)

mel_talk = NPC('img/mel_01.png', 0, 340)
mario_talk = NPC('img/mario_01.png', 550, 340)

bg_5 = BG('img/terrain/puzzlemania.png', 150, 100, c.BLUE)
hm_01 = BG('img/assets/hm_01.png', 200, 150, c.BLUE)
hm_02 = BG('img/assets/hm_02.png', 200, 150, c.BLUE)
hm_03 = BG('img/assets/hm_03.png', 200, 150, c.BLUE)

pista_o = BG('img/assets/oveja_p.png', 150, 150, c.WHITE)
pista_m = BG('img/assets/mecate_p.png', 150, 150, c.WHITE)
pista_c = BG('img/assets/cobre_p.png', 150, 150, c.WHITE)
respuesta = BG('img/assets/respuestas.png', 150, 80, c.WHITE)

pistas = [pista_o, pista_m, pista_c]

hangman = [hm_01, hm_02, hm_03]

bg_group = pygame.sprite.Group()
bg_group.add(bg_1, bg_2)

sprite_group.add(ass_1, ass_2, ass_3, ass_4, ass_5, ass_6)

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
    if pygame.sprite.collide_rect(mel, arrow_up):
        ass_1.out(), ass_2.out(), ass_3.out(), ass_4.out(), ass_5.out(), ass_6.out()

        tah.out(), eb.out(), daniel.out()

        bg_group.add(bg_3)
        bg_group.remove(bg_1, bg_2)
        sprite_group.empty()
        sprite_group.add(mel,arrow_right, arrow_down)
        mel.door(250, 360)

    if pygame.sprite.collide_rect(mel, arrow_right):
        bg_group.remove(bg_3)
        sprite_group.remove(arrow_right, arrow_down)
        bg_group.add(bg_1, bg_4)
        arrow_right.out(), arrow_down.out()
        sprite_group.add(ass_7, ass_8, ass_9, ass_10, ass_11, dania, diego, alberto, mario, arrow_left)
        mel.door(160, 480)

    if pygame.sprite.collide_rect(mel, mario):
        bg_group.empty()
        sprite_group.empty()
        ass_7.out(), ass_8.out(), ass_9.out(), ass_10.out(), ass_11.out(), dania.out(), diego.out(), alberto.out(), mario.out(), arrow_left.out()
        sprite_group.add(mel_talk, mario_talk, hangman)
        random = random.randrange(0,3)
        adivinar = int()
        correcto = 0
        incorrecto = 0
        sprite_group.add(pistas[random], respuesta)
        bg_group.add(bg_5)
        if keys[pygame.K_1]:
            adivinar = 0
        elif keys[pygame.K_2]:
            adivinar = 1
        elif keys[pygame.K_3]:
            adivinar = 2

        # Evaluar la respuesta solo si el jugador presiona una tecla válida
        if adivinar != -1:
            if adivinar == opcion_correcta:
                correcto += 1
                print("¡Correcto!")
                # Reiniciar el estado o actualizar la pantalla de éxito
                bg_group.empty()
                sprite_group.empty()
                bg_group.add(bg_1, bg_4)  # Ajusta bg_1 y bg_4 a tus recursos
                sprite_group.add(ass_7, ass_8, ass_9, ass_10, ass_11, dania, diego, alberto, mario, arrow_left, mel)
                mel.door(160, 480)
                break  # Salir del ciclo principal si es correcto
            else:
                incorrecto += 1
                print(f"¡Incorrecto! Intentos fallidos: {incorrecto}")
                if incorrecto > 2:
                    # Mostrar "Game Over"
                    print("¡Game Over!")
                    bg_group.empty()
                    sprite_group.empty()
                    game_over = BG('img/terrain/game_over.png', 120, 200, c.WHITE)
                    bg_group.add(game_over)
                    running = False

            # Reiniciar la variable `adivinar` para evitar reevaluaciones
            adivinar = -1

    if pygame.sprite.collide_rect(mel, arrow_down):
        bg_group.add(bg_1, bg_2)
        bg_group.remove(bg_3)
        sprite_group.add(ass_1, ass_2, ass_3, ass_4, ass_5, ass_6, tah, eb, daniel)
        sprite_group.remove(arrow_down,arrow_right)
        ass_1.get_in(), ass_2.get_in(), ass_3.get_in(), ass_4.get_in(), ass_5.get_in(), ass_6.get_in(), eb.get_in(), tah.get_in(), daniel.get_in()
        mel.door(250, 280)
        
    # Check for Game Over

    # Render the Display
        SALONIM3=True
        DISPLAY.fill(c.BLACK)
    if SALONIM3:
        bg_group.draw(DISPLAY)
        sprite_group.draw(DISPLAY)
    pygame.display.update()