import cv2 as cv
import numpy as np
import random as rand

class Scene:
    def __init__(self, img):
        self.img = img
        self.time_of_day = rand.choice(['morning', 'afternoon', 'night'])
        self.sun_position = rand.randint(100, 800)
        self.sun_radius = rand.randint(60, 75)
        self.update_scene()

    def update_scene(self):
        # Establecer fondo según la hora del día
        self.draw_background()
        
        # Dibujar sol si no es de noche
        if self.time_of_day != 'night':
            self.draw_sun()
        
        # Dibujar carretera, edificios, carro
        self.draw_road()
        self.draw_buildings()
        self.draw_car()

    def draw_background(self):
        if self.time_of_day == 'morning':
            self.img[:] = (135, 206, 235)  # Azul claro
        elif self.time_of_day == 'afternoon':
            self.img[:] = (255, 165, 0)    # Rojizo
        elif self.time_of_day == 'night':
            self.img[:] = (0, 0, 0)        # Negro
            self.draw_stars(100)           # Dibujar estrellas
            # Opcionalmente, puedes dibujar una luna si quieres en la noche
            cv.circle(self.img, (rand.randint(100, 800), 90), rand.randint(60, 75), (128, 128, 128), -1)

    def draw_stars(self, n_stars):
        for _ in range(n_stars):
            x = rand.randint(0, self.img.shape[1] - 1)
            y = rand.randint(0, self.img.shape[0] - 1)
            size = rand.randint(1, 3)
            cv.circle(self.img, (x, y), size, (255, 255, 255), -1)

    def draw_sun(self):
        cv.circle(self.img, (self.sun_position, 90), int(self.sun_radius - self.sun_radius * 0.2), (0, 255, 255), 1)
        cv.circle(self.img, (self.sun_position, 90), self.sun_radius, (220, 255, 255), 10)

    def draw_road(self):
        # carretera
        for i in range(250):
            cv.rectangle(self.img, (150 + i, 600 - i), (750 - i, 599 - i), (0, 0, 0), -1)

        # líneas de la carretera
        cv.rectangle(self.img, (445, 351), (450, 361), (255, 255, 255), -1)
        cv.rectangle(self.img, (443, 400), (453, 430), (255, 255, 255), -1)
        cv.rectangle(self.img, (441, 449), (456, 500), (255, 255, 255), -1)

        # área verde
        for i in range(250):
            cv.rectangle(self.img, (0, 351 + i), (398 - i, 350 + i), (123, 179, 105), -1)
            cv.rectangle(self.img, (502 + i, 351 + i), (900, 350 + i), (123, 179, 105), -1)

    def draw_buildings(self):
        class Buildings:
            def __init__(self, image, position=None, height=None):
                self.position = position if position is not None else rand.randint(0, 700)
                self.height = height if height is not None else rand.randint(1, 3)  # Aseguramos que la altura sea al menos 1
                self.img = image

            def draw(self):
                i = 0
                if self.height == 2:
                    i = 75
                cv.rectangle(self.img, (self.position, 200 - i), (self.position + 150, 350), (156, 156, 156), -1)
                # columna izquierda
                cv.rectangle(self.img, (self.position + 37 - 10, 200 + 37 - 10), (self.position + 37 + 10, 200 + 37 + 10), (255, 255, 255), -1)
                cv.rectangle(self.img, (self.position + 37 - 10, 350 - 37 - 10), (self.position + 37 + 10, 350 - 37 + 10), (255, 255, 255), -1)
                # columna derecha
                cv.rectangle(self.img, (self.position + 150 - 37 - 10, 200 + 37 - 10), (self.position + 150 - 37 + 10, 200 + 37 + 10), (255, 255, 255), -1)
                cv.rectangle(self.img, (self.position + 150 - 37 - 10, 350 - 37 - 10), (self.position + 150 - 37 + 10, 350 - 37 + 10), (255, 255, 255), -1)
                if self.height == 2:
                    cv.rectangle(self.img, (self.position + 37 - 10, 200 - 75 + 37 - 10), (self.position + 37 + 10, 200 - 75 + 37 + 10), (255, 255, 255), -1)
                    cv.rectangle(self.img, (self.position + 150 - 37 - 10, 200 - 75 + 37 - 10), (self.position + 150 - 37 + 10, 200 - 75 + 37 + 10), (255, 255, 255), -1)

        # Crear y dibujar edificios
        Buildings(self.img, height=2).draw()
        Buildings(self.img).draw()
        Buildings(self.img).draw()

    def draw_car(self):
        x, y = rand.randint(200, 600), 540
        width, height = 100, 50
        cv.rectangle(self.img, (x, y), (x + width, y + height), (0, 0, 255), -1)  # Carro rojo
        cv.circle(self.img, (x + 20, y + height), 15, (128, 128, 128), -1)  # Rueda izquierda
        cv.circle(self.img, (x + width - 20, y + height), 15, (128, 128, 128), -1)  # Rueda derecha

# Crear y actualizar la escena con tiempo del día aleatorio
img = np.zeros((600, 900, 3), dtype=np.uint8)
scene = Scene(img)
cv.imshow("Scene", img)
cv.waitKey(0)
cv.destroyAllWindows()
