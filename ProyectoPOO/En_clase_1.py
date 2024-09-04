import cv2
import numpy as np
import random

class SpaceScene:
    def __init__(self, width=800, height=600, n_stars=50, n_planets=10):
        self.width = width
        self.height = height
        self.n_stars = n_stars
        self.n_planets = n_planets
        self.min_star_size = 5
        self.max_star_size = 15
        self.min_planet_radius = self.min_star_size + 1
        self.max_planet_radius = 60
        self.background_color = (50, 0, 50)  # BGR para morado oscuro
        self.image = np.full((self.height, self.width, 3), self.background_color, dtype=np.uint8)

    def random_yellow(self):
        r = random.randint(150, 255)
        g = random.randint(150, 255)
        b = random.randint(0, 100)
        return (b, g, r)  # BGR

    def random_planet_color(self):
        color_type = random.choice(['purple', 'blue', 'red'])
        if color_type == 'purple':
            return (random.randint(50, 150), random.randint(0, 100), random.randint(100, 200))  # BGR para morado
        elif color_type == 'blue':
            return (random.randint(0, 100), random.randint(0, 100), random.randint(150, 255))  # BGR para azul
        elif color_type == 'red':
            return (random.randint(0, 100), random.randint(0, 50), random.randint(150, 255))  # BGR para rojo

    def draw_star(self, center, size):
        x, y = center
        color = self.random_yellow()
        for i in range(5):
            angle = i * 144  # Ángulo para dibujar las 5 puntas
            end_x = int(x + size * np.cos(np.radians(angle)))
            end_y = int(y - size * np.sin(np.radians(angle)))
            cv2.line(self.image, (x, y), (end_x, end_y), color, 1)

    def draw_planet(self, center, radius):
        color = self.random_planet_color()
        cv2.circle(self.image, center, radius, color, -1)

    def create_scene(self):
        # Dibujar estrellas
        for _ in range(self.n_stars):
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            size = random.randint(self.min_star_size, self.max_star_size)
            self.draw_star((x, y), size)

        # Dibujar planetas
        for _ in range(self.n_planets):
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            radius = random.randint(self.min_planet_radius, self.max_planet_radius)
            self.draw_planet((x, y), radius)

    def show(self):
        cv2.imshow("Space Drawing", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Uso de la clase
scene = SpaceScene(n_stars=50, n_planets=10)
scene.create_scene()
scene.show()
