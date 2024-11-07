# Diseñe una interfaz gráfica de un osciloscopio que integre controles de amplitud y tiempo. Para visualizar las señales adquiridas incluya un Axes. La adquisición de
# señales debe ser realizada con el ADC del Arduino. Es importante mencionar que la interfaz gráfica debe cumplir con las características de un osciloscopio estándar,
# es decir, los ejes horizontal y vertical deben estar graduados, la pantalla se debe de limpiar cuando la señal alcance el tiempo máximo de visualización establecida
# en el control de escala temporal y reiniciar la adquisición, y los controles de amplitud y tiempo deben actualizar las escalas del objeto Axes de forma inmediata.
# Asimismo, la interfaz debe de incluir un botón para iniciar la adquisición y otro botón para detenerla.

import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import serial
import threading
import time
import serial.tools.list_ports
from PIL import Image, ImageTk

# Configuración de la ventana principal
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Osciloscopio con ESP32")
root.geometry("900x750")

# Variables para la adquisición de señales
running = False
paused = False
amplitude_scale = 1.0
time_scale = 1.0
data = []
esp = None  # Inicializar la variable serial

# Crear la figura de Matplotlib
fig, ax = plt.subplots()
ax.set_title("Señal del Osciloscopio")
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Voltaje (V)")
line, = ax.plot([], [], color="blue")

# Función para cargar y redimensionar imágenes
def cargar_imagen(ruta, ancho, alto):
    imagen = Image.open(ruta)
    imagen = imagen.resize((ancho, alto), Image.LANCZOS)
    return ImageTk.PhotoImage(imagen)

# Cargar imágenes para los botones
start_image = cargar_imagen("C:/Users/rayoy/Documents/Spyder/start.png", 60, 60)
stop_image = cargar_imagen("C:/Users/rayoy/Documents/Spyder/stop.png", 60, 60)
pause_image = cargar_imagen("C:/Users/rayoy/Documents/Spyder/pause.png", 60, 60)
resume_image = cargar_imagen("C:/Users/rayoy/Documents/Spyder/resume.png", 60, 60)

# Función para actualizar la escala de amplitud
def update_amplitude(value):
    global amplitude_scale
    amplitude_scale = float(value)
    ax.set_ylim(-amplitude_scale, amplitude_scale)
    fig.canvas.draw()
    amplitude_value_label.configure(text=f"Amplitud: {amplitude_scale:.2f}")

# Función para actualizar la escala de tiempo
def update_time(value):
    global time_scale
    time_scale = float(value)
    ax.set_xlim(0, time_scale)
    fig.canvas.draw()
    time_value_label.configure(text=f"Tiempo: {time_scale:.2f}")

# Función para seleccionar el puerto COM
def select_com():
    global esp
    com_port = com_combobox.get()
    try:
        esp = serial.Serial(com_port, 115200, timeout=1)
        time.sleep(2)  # Esperar a que la conexión se estabilice
        status_label.configure(text=f"Conectado a {com_port}")
    except Exception as e:
        status_label.configure(text=f"Error: {e}")

# Función para manejar el botón de encendido/apagado
def toggle_acquisition():
    global running, data
    if running:
        running = False
        data = []  # Limpiar los datos
        line.set_data([], [])
        fig.canvas.draw()
        start_stop_button.configure(image=start_image)
    else:
        if esp is None:
            status_label.configure(text="Selecciona un puerto COM primero")
            return
        running = True
        data = []  # Reiniciar los datos
        start_stop_button.configure(image=stop_image)
        threading.Thread(target=acquire_data, daemon=True).start()

# Función para manejar el botón de pausa/reanudar
def toggle_pause():
    global paused
    paused = not paused
    if paused:
        pause_resume_button.configure(image=resume_image)
    else:
        pause_resume_button.configure(image=pause_image)
        data.clear()  # Limpiar los datos y reiniciar la adquisición

# Función para adquirir datos del ESP32
def acquire_data():
    global data, running, paused
    start_time = time.time()

    while running:
        if not paused:
            try:
                esp.write(b"READ\n")  # Enviar comando al ESP32 (puedes cambiarlo según el protocolo)
                line_data = esp.readline().decode().strip()
                if line_data.startswith("Voltage:"):
                    voltage = float(line_data.split(":")[1].strip().split()[0])
                    current_time = time.time() - start_time
                    data.append((current_time, voltage))

                    # Limitar la cantidad de datos a solo el tiempo de escala
                    if current_time > time_scale:
                        data = [(t, v) for t, v in data if t > current_time - time_scale]

                    # Limpiar y reiniciar la señal si ha pasado el tiempo de escala
                    if current_time > 2 * time_scale:
                        data = []  # Limpiar completamente
                        start_time = time.time()  # Reiniciar el tiempo

                    # Actualizar la gráfica
                    times, voltages = zip(*data) if data else ([], [])
                    line.set_data(times, voltages)
                    ax.relim()
                    ax.autoscale_view()
                    fig.canvas.draw()
            except Exception as e:
                print(f"Error: {e}")
        else:
            time.sleep(0.1)  # Pausa breve cuando está en pausa

# Crear un marco principal para contener todos los elementos
main_frame = ctk.CTkFrame(root)
main_frame.pack(pady=20, padx=20, fill="x")

# Frame izquierdo para el puerto COM
frame_left = ctk.CTkFrame(main_frame)
frame_left.pack(side="left", padx=20)

com_combobox = ctk.CTkComboBox(frame_left, values=[port.device for port in serial.tools.list_ports.comports()])
com_combobox.pack(pady=5)

select_com_button = ctk.CTkButton(frame_left, text="Seleccionar COM", command=select_com)
select_com_button.pack(pady=5)

status_label = ctk.CTkLabel(frame_left, text="Selecciona un puerto COM")
status_label.pack()

# Frame central para los controles de amplitud y tiempo
frame_center = ctk.CTkFrame(main_frame)
frame_center.pack(side="left", padx=20)

amplitude_slider = ctk.CTkSlider(frame_center, from_=0.1, to=6.0, command=update_amplitude)
amplitude_slider.set(1.0)  # Valor por defecto
amplitude_slider.pack(pady=5)
amplitude_value_label = ctk.CTkLabel(frame_center, text="Amplitud: 1.00")
amplitude_value_label.pack()

time_slider = ctk.CTkSlider(frame_center, from_=0.1, to=15.0, command=update_time)
time_slider.set(1.0)  # Valor por defecto
time_slider.pack(pady=5)
time_value_label = ctk.CTkLabel(frame_center, text="Tiempo: 1.00")
time_value_label.pack()

# Frame derecho para los botones de encendido y pausa
frame_right = ctk.CTkFrame(main_frame)
frame_right.pack(side="right", padx=20)

start_stop_button = ctk.CTkButton(frame_right, image=start_image, text="", command=toggle_acquisition, width=80, height=80)
start_stop_button.pack(pady=5)

pause_resume_button = ctk.CTkButton(frame_right, image=pause_image, text="", command=toggle_pause, width=80, height=80)
pause_resume_button.pack(pady=5)

# Integrar la figura de Matplotlib en la interfaz de Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill="both", expand=True)

# Iniciar la interfaz
root.mainloop()

# Cerrar la conexión serial al salir
if esp:
    esp.close()
