import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import serial
import threading
import time
import numpy as np

# Configura la comunicación serial con el ESP32
esp = serial.Serial('COM3', 115200, timeout=1)  # Reemplaza 'COM3' con el puerto correcto
time.sleep(2)  # Espera a que la conexión se estabilice

# Configuración de la ventana principal
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Osciloscopio con ESP32")
root.geometry("800x600")

# Variables para la adquisición de señales
running = False
amplitude_scale = 1.0
time_scale = 1.0
data = []

# Crear la figura de Matplotlib
fig, ax = plt.subplots()
ax.set_title("Señal del Osciloscopio")
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Voltaje (V)")
line, = ax.plot([], [], color="blue")  # Crear la línea correctamente

# Función para actualizar la escala de amplitud
def update_amplitude(value):
    global amplitude_scale
    amplitude_scale = float(value)
    ax.set_ylim(-amplitude_scale, amplitude_scale)
    fig.canvas.draw()

# Función para actualizar la escala de tiempo
def update_time(value):
    global time_scale
    time_scale = float(value)
    ax.set_xlim(0, time_scale)
    fig.canvas.draw()

# Función para iniciar la adquisición
def start_acquisition():
    global running
    running = True
    threading.Thread(target=acquire_data, daemon=True).start()

# Función para detener la adquisición
def stop_acquisition():
    global running
    running = False

# Función para adquirir datos del ESP32
def acquire_data():
    global data, running
    data = []  # Reiniciar los datos
    start_time = time.time()

    while running:
        try:
            esp.write(b"READ\n")  # Enviar comando al ESP32 (puedes cambiarlo según el protocolo)
            line_data = esp.readline().decode().strip()
            if line_data.startswith("Voltage:"):
                voltage = float(line_data.split(":")[1].strip().split()[0])
                current_time = time.time() - start_time
                data.append((current_time, voltage))

                # Limitar la cantidad de datos para la visualización
                if current_time > time_scale:
                    data = [(t, v) for t, v in data if t > current_time - time_scale]

                # Actualizar la gráfica
                times, voltages = zip(*data)
                line.set_data(times, voltages)  # Usar set_data correctamente
                ax.relim()
                ax.autoscale_view()
                fig.canvas.draw()
        except Exception as e:
            print(f"Error: {e}")

# Controles de amplitud y tiempo
amplitude_slider = ctk.CTkSlider(root, from_=0.1, to=5.0, command=update_amplitude)
amplitude_slider.set(1.0)  # Valor por defecto
amplitude_slider.pack(pady=10)

time_slider = ctk.CTkSlider(root, from_=0.1, to=10.0, command=update_time)
time_slider.set(1.0)  # Valor por defecto
time_slider.pack(pady=10)

# Botones para iniciar y detener la adquisición
start_button = ctk.CTkButton(root, text="Iniciar", command=start_acquisition)
start_button.pack(pady=10)

stop_button = ctk.CTkButton(root, text="Detener", command=stop_acquisition)
stop_button.pack(pady=10)

# Integrar la figura de Matplotlib en la interfaz de Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill="both", expand=True)

# Iniciar la interfaz
root.mainloop()

# Cerrar la conexión serial al salir
esp.close()
