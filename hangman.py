import random
import pygame

incorrecto = 0
# Lista de palabras con sus pistas
palabras = [
    ("oveja", "Lana sube, lana baja."),
    ("mecate", "Agua pasa por mi casa, cate de mi corazón."),
    ("cobre", "Oro no es, plata no es.")
]

# Elegir una palabra al azar
indice = random.randrange(0, len(palabras))
palabra, pista = palabras[indice]

print("Adivine la palabra:")
print(pista)

# Entrada del usuario
adivinanza = input().strip().lower()

# Verificar la adivinanza
if adivinanza == palabra:
    print("¡Correcto!")
else:
    print("¡Incorrecto! La palabra era:", palabra)
    incorrecto +=1

if incorrecto >= 3:
    print("MUAJAJA, moriste.")

class Hangman(pygame.sprite.Sprite):
    def __init__(self):
        super(Hangman, self).__init__()
        img_hangman_01 = pygame.image.load('img/assets/hm_01.png')
        img_hangman_02 = pygame.image.load('img/assets/hm_02.png')
        img_hangman_03 = pygame.image.load('img/assets/hm_03.png')
        self.img_hangman = [ img_hangman_01, img_hangman_02, img_hangman_03]
        self.image = pygame.Surface(500, 300)
        self.color = (137, 109, 93)
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.image.fill(self.color)
        self.rect.x += self.vel_x
        self.rect.y +=self.vel_y