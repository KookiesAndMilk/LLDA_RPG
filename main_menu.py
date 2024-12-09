import pygame
import sys

def mostrar_menu(screen, clock, fuente, fuente_bold, imagen_fondo, imagen_mel):
    NEGRO = (0, 0, 0)
    MULTI3 = (118, 87, 118)
    BLANCO = (255, 255, 255)
    
    opciones = ["Comenzar", "Cargar", "Salir"]
    opcion_elegida = 0
    corriendo = True
    
    fuente_titulo = pygame.font.Font(None, 48)  # Fuente para el título



    while corriendo:
        screen.fill(NEGRO)
        screen.blit(imagen_fondo, (100, 50))  # Posiciona la imagen del fondo
        screen.blit(imagen_mel, (50, 90))    # Posiciona la imagen de Mel
        for i, opcion in enumerate(opciones):
            if i == opcion_elegida:
                texto = fuente_bold.render(opcion, True, MULTI3)
            else:
                texto = fuente.render(opcion, True, BLANCO)
            x = screen.get_width() // 2 - texto.get_width() // 2
            y = 250 + i * 40
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
                    return opcion_elegida

        pygame.display.flip()
        clock.tick(60)
