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
    fondo_rect = pygame.transform.scale(fondo_rect, (400, 200))  # Ajustar tamaño del rectángulo
    mel_bg = pygame.transform.scale(mel_bg, (120, 200))          # Ajustar tamaño de Mel

    # Fuentes
    fuente_titulo = pygame.font.Font(None, 48)  # Cambiar por una fuente personalizada si tienes
    titulo_texto = fuente_titulo.render("La Llave de Atrás", True, BLANCO)

    # Posiciones
    fondo_rect_x = (DISPLAY_WIDTH - fondo_rect.get_width()) // 2
    fondo_rect_y = (DISPLAY_HEIGHT - fondo_rect.get_height()) // 2 - 20
    mel_x = fondo_rect_x - mel_bg.get_width() - 10  # Ajustar para separar a "Mel" del rectángulo
    mel_y = fondo_rect_y + (fondo_rect.get_height() - mel_bg.get_height()) // 2
    titulo_x = fondo_rect_x + 20  # Espaciado adicional para centrar el texto dentro del rectángulo
    titulo_y = fondo_rect_y + (fondo_rect.get_height() - titulo_texto.get_height()) // 2

    # Bucle del menú
    ejecutando = True
    while ejecutando:
        DISPLAY.fill(NEGRO)  # Fondo negro
        DISPLAY.blit(fondo_rect, (fondo_rect_x, fondo_rect_y))  # Rectángulo centrado
        DISPLAY.blit(mel_bg, (mel_x, mel_y))  # "Mel" alineada a la izquierda
        DISPLAY.blit(titulo_texto, (titulo_x, titulo_y))  # Título centrado en el rectángulo

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                ejecutando = False

        pygame.display.flip()

    pygame.quit()


    return mostrar_menu ()