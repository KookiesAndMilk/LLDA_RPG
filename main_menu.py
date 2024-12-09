import pygame

def mostrar_menu():
    pygame.init()

    # Configuración de la pantalla
    DISPLAY_WIDTH, DISPLAY_HEIGHT = 640, 480
    DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("La Llave de Atrás")

    # Colores
    NEGRO = (0, 0, 0)
    BLANCO = (255, 255, 255)

     # Cargar imágenes
    fondo_rect = pygame.image.load('LLDA_RPG-main/img/main_menu_bg.png')  # Reemplaza con la imagen del rectángulo
    mel_bg = pygame.image.load('LLDA_RPG-main/img/main_menu_mel.png')    # Imagen de Mel

    # Escalar imágenes si es necesario
    fondo_rect = pygame.transform.scale(fondo_rect, (400, 200))  # Tamaño del rectángulo
    mel_bg = pygame.transform.scale(mel_bg, (120, 200))          # Tamaño de Mel

    # Fuentes
    fuente_titulo = pygame.font.Font(None, 48)  # Fuente para el título
    fuente_opciones = pygame.font.Font(None, 36)  # Fuente para las opciones del menú

    titulo_texto = fuente_titulo.render("La Llave de Atrás", True, BLANCO)

    # Opciones del menú
    opciones = ["Comenzar", "Cargar", "Salir"]
    opciones_render = [fuente_opciones.render(opcion, True, BLANCO) for opcion in opciones]

    # Posiciones de las imágenes
    fondo_rect_x = (DISPLAY_WIDTH - fondo_rect.get_width()) // 2
    fondo_rect_y = 80  # Más cerca del borde superior
    mel_x = fondo_rect_x - mel_bg.get_width() - 10
    mel_y = fondo_rect_y + (fondo_rect.get_height() - mel_bg.get_height()) // 2
    titulo_x = fondo_rect_x + 20
    titulo_y = fondo_rect_y + (fondo_rect.get_height() - titulo_texto.get_height()) // 2

    # Posiciones de las opciones
    opciones_x = DISPLAY_WIDTH // 2
    opciones_y = fondo_rect_y + fondo_rect.get_height() + 40  # Espaciadas debajo del rectángulo
    espacio_entre_opciones = 50

    seleccion_actual = 0

    # Bucle del menú
    ejecutando = True
    while ejecutando:
        DISPLAY.fill(NEGRO)  # Fondo negro
        DISPLAY.blit(fondo_rect, (fondo_rect_x, fondo_rect_y))  # Rectángulo centrado
        DISPLAY.blit(mel_bg, (mel_x, mel_y))  # "Mel" alineada a la izquierda
        DISPLAY.blit(titulo_texto, (titulo_x, titulo_y))  # Título centrado en el rectángulo

        # Renderizar opciones del menú
        for i, opcion_render in enumerate(opciones_render):
            color = BLANCO if i == seleccion_actual else (150, 150, 150)  # Resalta la opción seleccionada
            opcion_texto = fuente_opciones.render(opciones[i], True, color)
            opcion_x = opciones_x - opcion_texto.get_width() // 2
            opcion_y = opciones_y + i * espacio_entre_opciones
            DISPLAY.blit(opcion_texto, (opcion_x, opcion_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    seleccion_actual = (seleccion_actual - 1) % len(opciones)
                elif event.key == pygame.K_DOWN:
                    seleccion_actual = (seleccion_actual + 1) % len(opciones)
                elif event.key == pygame.K_RETURN:
                    if seleccion_actual == 0:  # Comenzar
                        ejecutando = False
                    elif seleccion_actual == 1:  # Cargar
                        print("Opción Cargar seleccionada")
                    elif seleccion_actual == 2:  # Salir
                        pygame.quit()
                        exit()

        pygame.display.flip()

    pygame.quit()

    return mostrar_menu ()