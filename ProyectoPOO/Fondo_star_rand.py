import cv2
import numpy as np
import random

# Crear una imagen con fondo morado oscuro
height, width = 600, 800
background_color = (50, 0, 50)  # BGR para morado oscuro
image = np.full((height, width, 3), background_color, dtype=np.uint8)

# Número de estrellas y rango de tamaño
n_stars = 50  # Puedes ajustar este número
min_size, max_size = 5, 15  # Tamaño de estrella entre 5 y 15

# Función para generar un color amarillo aleatorio
def random_yellow():
    r = random.randint(150, 255)
    g = random.randint(150, 255)
    b = random.randint(0, 100)
    return (b, g, r)  # BGR

# Función para dibujar una estrella
def draw_star(image, center, size):
    x, y = center
    color = random_yellow()
    for i in range(5):
        angle = i * 144  # Ángulo para dibujar las 5 puntas
        end_x = int(x + size * np.cos(np.radians(angle)))
        end_y = int(y - size * np.sin(np.radians(angle)))
        cv2.line(image, (x, y), (end_x, end_y), color, 1)

# Dibujar estrellas en posiciones aleatorias
for _ in range(n_stars):
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)
    size = random.randint(min_size, max_size)
    draw_star(image, (x, y), size)

# Dibujar un planeta
planet_center = (width // 2, height // 2 + 100)
planet_radius = 50
planet_color = (255, 0, 0)  # BGR para azul
cv2.circle(image, planet_center, planet_radius, planet_color, -1)

# Mostrar la imagen
cv2.imshow("Space Drawing", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
