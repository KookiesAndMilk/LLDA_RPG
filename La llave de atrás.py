import pygame, sys

pygame.init()

Ancho, Alto = 320, 240
screen = pygame.display.set_mode((Ancho, Alto))
pygame.display.set_caption("La llave de atrás - Menú principal")

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (50, 50, 50)
MULTI3 = (118, 87, 118)

fuente = pygame.font.Font('fuente/dogica.ttf', 50)
fuente_bold = pygame.font.Font('fuente/dogicabold.ttf', 25)

opciones = ["Comenzar", "Cargar", "Salir"]
opcion_elegida = 0

def mostrar_menu():
    global opcion_elegida
    corriendo = True
    while corriendo:
        pantalla.fill(NEGRO)
        for i, opcion in enumerate(opciones):
            if i == opcion_elegida:
                texto = fuente.render(opcion, True, MULTI3)
            else:
                texto = fuente.render(opcion, True, BLANCO)

                x =  Ancho // 2 - texto.get_width() // 2
                y = Alto // 2 - 100 + i * 60 
                screen.blit(texto, (x, y))

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
                                print("Inciando juego...")
                                corriendo = False
                            elif opcion_elegida == 1:
                                print("Cargando partida...")
                            elif opcion_elegida == 2:
                                pygame.quit()
                                sys.exit()
        
                pygame.display.flip()
    mostrar_menu ()
    print ("El juego está comenzando...")

