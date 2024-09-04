import cv2
import numpy as np
import random

class SpaceScene:
    def __init__(self, width=800, height=600, n_stars=50, n_planets=10, ring_probability=0.33, half_ring_probability=0.33):
        self.width = width
        self.height = height
        self.n_stars = n_stars
        self.n_planets = n_planets
        self.min_star_size = 5
        self.max_star_size = 15
        self.min_planet_radius = self.min_star_size + 1
        self.max_planet_radius = 60
        self.ring_probability = ring_probability
        self.half_ring_probability = half_ring_probability
        self.background_color = (50, 0, 50)  # BGR para morado oscuro
        self.image = np.full((self.height, self.width, 3), self.background_color, dtype=np.uint8)

    def random_yellow(self): # Amarillos para estrellas
        r = random.randint(150, 255)
        g = random.randint(150, 255)
        b = random.randint(0, 100)
        return (b, g, r)  

    def random_planet_color(self): # Distintos tonos planetas
        color_type = random.choice(['purple', 'blue', 'red'])
        if color_type == 'purple':
            return (random.randint(50, 150), random.randint(0, 100), random.randint(100, 200))  
        elif color_type == 'blue':
            return (random.randint(0, 100), random.randint(0, 100), random.randint(150, 255))  
        elif color_type == 'red':
            return (random.randint(0, 100), random.randint(0, 50), random.randint(150, 255))  

    def lighten_color(self, color, amount=50):
        b, g, r = color
        b = min(b + amount, 255)
        g = min(g + amount, 255)
        r = min(r + amount, 255)
        return (b, g, r)

    def darken_color(self, color, amount=100):
        b, g, r = color
        b = max(b - amount, 0)
        g = max(g - amount, 0)
        r = max(r - amount, 0)
        return (b, g, r)

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
        # Dibuja el planeta
        cv2.circle(self.image, center, radius, color, -1)
        
        # Calcula la posición y color de la sombra
        shadow_radius = radius // 2
        shadow_color = self.darken_color(color, 100)
        shadow_position = random.choice([
            (center[0], center[1] - radius // 2),           # Superior
            (center[0] + radius // 2, center[1] - radius // 2),  # Superior derecha
            (center[0] - radius // 2, center[1] - radius // 2)   # Superior izquierda
        ])
        cv2.circle(self.image, shadow_position, shadow_radius, shadow_color, -1)

        # Probabilidad de añadir un anillo transversal
        if random.random() < self.ring_probability:
            ring_color = self.darken_color(color, 100)
            ring_thickness = radius // 5
            cv2.ellipse(self.image, center, (radius + ring_thickness, radius + ring_thickness), 0, 0, 360, ring_color, ring_thickness)
        
        # Probabilidad de añadir un anillo como media luna
        if random.random() < self.half_ring_probability:
            ring_color = self.lighten_color(color, 50)
            ring_thickness = radius // 5
            cv2.ellipse(self.image, center, (radius + ring_thickness, radius + ring_thickness), 0, 0, 180, ring_color, ring_thickness)

    def draw_rocket(self):
        # Coordenadas aleatorias para el cohete
        x = random.randint(50, self.width - 50)
        y = random.randint(50, self.height - 50)

        # Colores para el cohete
        body_color = (128, 128, 128) 
        fin_color = (0, 0, 0)  
        flame_color = (0, 0, 255)  

        # Dibuja el cuerpo del cohete
        cv2.rectangle(self.image, (x-10, y), (x+10, y-40), body_color, -1)
        # Dibuja el cono del cohete
        points = np.array([[x-10, y-40], [x+10, y-40], [x, y-60]], np.int32)
        cv2.fillPoly(self.image, [points], body_color)
        # Dibuja las aletas
        cv2.rectangle(self.image, (x-15, y-10), (x-5, y), fin_color, -1)
        cv2.rectangle(self.image, (x+5, y-10), (x+15, y), fin_color, -1)
        # Dibuja las llamas
        cv2.line(self.image, (x-10, y), (x-20, y+20), flame_color, 2)
        cv2.line(self.image, (x+10, y), (x+20, y+20), flame_color, 2)
        cv2.line(self.image, (x-5, y), (x-15, y+20), flame_color, 2)
        cv2.line(self.image, (x+5, y), (x+15, y+20), flame_color, 2)

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

        # Dibujar cohete
        self.draw_rocket()

    def show(self):
        cv2.imshow("Space Drawing", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Uso de la clase
scene = SpaceScene(n_stars=100, n_planets=15, ring_probability=0.33, half_ring_probability=0.33)
scene.create_scene()
scene.show()
