# Esta es solo la interfaz 
import customtkinter as ctk
from tkinter import PhotoImage
from PIL import Image, ImageTk  # Importar PIL para redimensionar imágenes

# Configuración de la ventana principal
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Simulación de LEDs")
root.state("zoomed")  # Maximizar la ventana

# Función para cargar y redimensionar imágenes
def cargar_imagen(ruta, ancho, alto):
    imagen = Image.open(ruta)  # Abrir la imagen con PIL
    imagen = imagen.resize((ancho, alto), Image.LANCZOS)  # Redimensionar la imagen
    return ImageTk.PhotoImage(imagen)  # Convertir a un objeto ImageTk

# Cargar y redimensionar las imágenes de LED
led_off_image = cargar_imagen("C:/Users/rayoy/Documents/Spyder/LEDRojoA.png", 100, 130)  # LED apagado
led_on_image = cargar_imagen("C:/Users/rayoy/Documents/Spyder/LEDRojoE.png", 100, 130)   # LED encendido

# Variables para almacenar el estado de los LEDs
led_states = [False] * 8  # 8 LEDs apagados inicialmente

# Función para alternar el estado de un LED
def toggle_led(index, button):
    led_states[index] = not led_states[index]  # Cambiar el estado
    if led_states[index]:
        button.configure(image=led_on_image)  # Encender LED
    else:
        button.configure(image=led_off_image)  # Apagar LED

# Crear un marco para centrar los botones
frame = ctk.CTkFrame(root)
frame.pack(expand=True)  # Usar 'expand' para centrar el marco en la ventana

# Crear botones de LED más pequeños con imágenes escaladas
led_buttons = []

for i in range(8):
    button = ctk.CTkButton(
        frame,
        text="",  # Sin texto en el botón
        image=led_off_image,  # Imagen del LED apagado
        width=100,  # Ancho del botón
        height=130,  # Alto del botón
        fg_color=None,  # Sin color de fondo
        hover_color="gray",  # Color al pasar el cursor
        command=lambda i=i: toggle_led(i, led_buttons[i])
    )
    led_buttons.append(button)

# Colocar los botones en una cuadrícula 4x2 centrada
for i in range(4):
    led_buttons[i].grid(row=0, column=i, padx=30, pady=30)  # Espaciado ajustado
    led_buttons[i+4].grid(row=1, column=i, padx=30, pady=30)

# Iniciar la interfaz
root.mainloop()
