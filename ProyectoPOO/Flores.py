import numpy as np
import random
import cv2 as cv

# Parámetros generales
ancho = 900
alto = 600
n_flores = 50
n_nubes = 10  # Número de nubes
nivel_suelo = alto - 100

# Generación aleatoria de colores para el fondo
color_cielo = (
    random.randint(200, 255),  # Tonos aleatorios para el cielo
    random.randint(180, 223),
    random.randint(0, 80)
)
color_hierba = (
    random.randint(0, 100),  # Tonos aleatorios de verde para la hierba
    random.randint(100, 255),
    random.randint(0, 100)
)

# Imagen (fondo negro)
fondo = np.zeros((alto, ancho, 3), dtype=np.uint8) # cada valor de píxel en la imagen se almacena como un número entero de 8 bits que puede tener un valor entre 0 y 255

# Dibujar el fondo
cv.rectangle(fondo, (ancho, 0), (0, nivel_suelo), color_cielo, -1)  # Cielo
cv.rectangle(fondo, (ancho, nivel_suelo), (0, alto), color_hierba, -1)  # Hierba

# ***********************
class Nube:
    def __init__(self, imagen):
        self.img = imagen
        self.ubicacion_x = int(np.random.choice(range(ancho), 1))  # Posición aleatoria en el eje X
        self.ubicacion_y = int(np.random.choice(range(50, 150), 1))  # Altura aleatoria de la nube
        self.escala = np.random.choice(np.linspace(0.5, 2, num=5), 1)  # Escala aleatoria para variar el tamaño
        self.color_nube = (255, 255, 255)  # Color blanco para la nube

    def dibujar(self):
        radio_grande = int(40 * self.escala)
        radio_pequeno = int(30 * self.escala)

        # Dibujar las partes de la nube con círculos
        cv.circle(self.img, (self.ubicacion_x, self.ubicacion_y), radio_grande, self.color_nube, -1)
        cv.circle(self.img, (self.ubicacion_x + int(40 * self.escala), self.ubicacion_y + int(10 * self.escala)), radio_grande, self.color_nube, -1)
        cv.circle(self.img, (self.ubicacion_x - int(40 * self.escala), self.ubicacion_y + int(10 * self.escala)), radio_grande, self.color_nube, -1)
        cv.circle(self.img, (self.ubicacion_x + int(20 * self.escala), self.ubicacion_y - int(20 * self.escala)), radio_pequeno, self.color_nube, -1)
        cv.circle(self.img, (self.ubicacion_x - int(20 * self.escala), self.ubicacion_y - int(20 * self.escala)), radio_pequeno, self.color_nube, -1)

        return self.img
    
# ***********************

class Flor:
    def __init__(self, imagen): #  inicializa la nube con una ubicación aleatoria, escala y color
        self.img = imagen
        self.ubicacion = int(np.random.choice(range(ancho), 1))  # Posición aleatoria en el ancho de la imagen
        self.altura = int(np.random.choice(range(40, 100), 1))  # Altura aleatoria de la flor
        self.radio = int(np.random.choice(range(10, 17), 1))  # Radio aleatorio de los pétalos
        self.escala = np.random.choice(np.linspace(0.5, 1.5, num=5), 1)  # Escala aleatoria para variar el tamaño

    def generar_colores(self):
        color_petalo = random.choice([
            (153, 50, 204),  # Lila
            (219, 112, 147),  # Rosa pálido
            (255, 20, 147),  # Rosa fuerte
            (255, 105, 180),  # Rosa claro
            (220, 20, 60),  # Rojo carmesí
            (255, 0, 0)  # Rojo
        ])
        
        color_centro = (  # Color aleatorio amarillento para el centro
            random.randint(135, 255),
            random.randint(206, 255),
            random.randint(235, 255)
        )
        color_tallo = (116, 208, 70)  # Color verde para el tallo
        return color_petalo, color_centro, color_tallo

    def dibujar(self):
        radio_pequeno = int(self.radio * self.escala - 2 * self.escala)
        color_petalo, color_centro, color_tallo = self.generar_colores()

        # Dibujar pétalos
        for i in range(5):
            angulo = np.deg2rad(i * 72)  # Calcula la posición de cada pétalo en un círculo
            desplazamiento_x = int(self.radio * self.escala * np.cos(angulo))  # Desplazamiento en el eje X
            desplazamiento_y = int(self.radio * self.escala * np.sin(angulo))  # Desplazamiento en el eje Y
            cv.circle(self.img, (self.ubicacion + desplazamiento_x, nivel_suelo - self.altura + desplazamiento_y), self.radio, color_petalo, -1)
        
        # Dibujar pétalos adicionales más pequeños
        cv.circle(self.img, (self.ubicacion - int(4 * self.escala), nivel_suelo - self.altura + radio_pequeno), radio_pequeno, color_petalo, -1)
        cv.circle(self.img, (self.ubicacion + int(4 * self.escala), nivel_suelo - self.altura + radio_pequeno), radio_pequeno, color_petalo, -1)

        # Dibujar el centro de la flor
        cv.circle(self.img, (self.ubicacion, nivel_suelo - self.altura), int(self.radio * 0.6), color_centro, -1)

        # Dibujar el tallo
        cv.line(self.img, (self.ubicacion, nivel_suelo), (self.ubicacion, nivel_suelo - self.altura + 20), color_tallo, int(3.5 * self.escala))

        return self.img
# ***********************
# Cada objeto de estas clases tiene su propio estado (ubicación, escala, color) y métodos (dibujar) que operan sobre ese estado.


# Mostrar la imagen, se instacían los objetos de las clases Nube y Flor
for i in range(n_nubes):
    img = Nube(fondo).dibujar()

for i in range(n_flores):
    img = Flor(fondo).dibujar()

cv.imshow('campo de flores con nubes', img)

cv.waitKey(0)
cv.destroyAllWindows()
