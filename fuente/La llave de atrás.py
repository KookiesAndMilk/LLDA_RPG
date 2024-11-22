import pygame, sys

pygame.init()

Ancho, Alto = 800, 600
screen = pygame.display.set_mode((Ancho, Alto))
pygame.display.set_caption("La llave de atrás - Menú principal")
clock = pygame.time.Clock()

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
MULTI3 = (118, 87, 118)

# Fuentes
fuente = pygame.font.Font(r'game/fuente/dogica.ttf', 25)
fuente_bold = pygame.font.Font(r'game/fuente/dogicabold.ttf', 25)

# Opciones del menú
opciones = ["Comenzar", "Cargar", "Salir"]
opcion_elegida = 0

def mostrar_cargar(mensaje):
    screen.fill(NEGRO)
    texto = fuente_bold.render(mensaje, True, BLANCO)

def mostrar_menu():
    global opcion_elegida
    corriendo = True

    while corriendo:
        screen.fill(NEGRO)  # Fondo del menú

        # Manejar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    opcion_elegida = (opcion_elegida - 1) % len(opciones)
                elif evento.key == pygame.K_DOWN:
                    opcion_elegida = (opcion_elegida + 1) % len(opciones)
                elif evento.key == pygame.K_RETURN:
                    if opcion_elegida == 0:
                        print("Iniciando juego...")
                        corriendo = False
                    elif opcion_elegida == 1:
                        print("Cargando partida...")
                    elif opcion_elegida == 2:
                        pygame.quit()
                        sys.exit()

        # Dibujar opciones
        for i, opcion in enumerate(opciones):
            if i == opcion_elegida:
                texto = fuente_bold.render(opcion, True, MULTI3)  # Texto resaltado
            else:
                texto = fuente.render(opcion, True, BLANCO)  # Texto normal

            x = Ancho // 2 - texto.get_width() // 2
            y = Alto // 2 - 40 + i * 40
            screen.blit(texto, (x, y))

        pygame.display.flip()
        clock.tick(60)

mostrar_menu()
print("El juego está comenzando...")
