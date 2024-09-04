import cv2
import numpy as np
import random

# Crear una imagen con fondo morado oscuro
height, width = 600, 800
background_color = (50, 0, 50)  # BGR para morado oscuro
image = np.full((height, width, 3), background_color, dtype=np.uint8)

# Número de estrellas y rango de tamaño
n_stars = 50  # Puedes ajustar este número
min_star_size, max_star_size = 5, 15  # Tamaño de estrella entre 5 y 15

# Número de planetas y rango de tamaño
n_planets = 10  # Puedes ajustar este número
min_planet_radius, max_planet_radius = min_star_size + 1, 60  # Radio de planeta

# Función para generar un color amarillo aleatorio
def random_yellow():
    r = random.randint(150, 255)
    g = random.randint(150, 255)
    b = random.randint(0, 100)
    return (b, g, r)  # BGR

# Función para generar un color para los planetas
def random_planet_color():
    color_type = random.choice(['purple', 'blue', 'red'])
    if color_type == 'purple':
        return (random.randint(50, 150), random.randint(0, 100), random.randint(100, 200))  # BGR para morado
    elif color_type == 'blue':
        return (random.randint(0, 100), random.randint(0, 100), random.randint(150, 255))  # BGR para azul
    elif color_type == 'red':
        return (random.randint(0, 100), random.randint(0, 50), random.randint(150, 255))  # BGR para rojo

# Función para dibujar una estrella
def draw_star(image, center, size):
    x, y = center
    color = random_yellow()
    for i in range(5):
        angle = i * 144  # Ángulo para dibujar las 5 puntas
        end_x = int(x + size * np.cos(np.radians(angle)))
        end_y = int(y - size * np.sin(np.radians(angle)))
        cv2.line(image, (x, y), (end_x, end_y), color, 1)

# Función para dibujar un planeta
def draw_planet(image, center, radius):
    color = random_planet_color()
    cv2.circle(image, center, radius, color, -1)

# Dibujar estrellas en posiciones aleatorias
for _ in range(n_stars):
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)
    size = random.randint(min_star_size, max_star_size)
    draw_star(image, (x, y), size)

# Dibujar planetas en posiciones aleatorias
for _ in range(n_planets):
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)
    radius = random.randint(min_planet_radius, max_planet_radius)
    draw_planet(image, (x, y), radius)

# Mostrar la imagen
cv2.imshow("Space Drawing", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
