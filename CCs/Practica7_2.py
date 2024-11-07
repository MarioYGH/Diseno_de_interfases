# Diseñe una interfaz gráfica que permita ingresar los siguientes las amplitudes y frecuencias angulares de tres funciones armónicas, específicamente funciones de
# la forma A sin ωt. La interfaz debe incluir un Axes para mostrar la combinación lineal
# de las tres funciones armónicas (y), y un Axes adicional para mostrar el plano fase (y, ẏ).

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Función para actualizar la gráfica
def update_plot(event=None):
    # Obtener los valores de amplitud y frecuencia
    A1 = A1_slider.get()
    A2 = A2_slider.get()
    A3 = A3_slider.get()
    w1 = w1_slider.get()
    w2 = w2_slider.get()
    w3 = w3_slider.get()

    # Configurar el vector de tiempo
    t = np.linspace(0, 10, 1000)  # 10 segundos de simulación
    y = A1 * np.sin(w1 * t) + A2 * np.sin(w2 * t) + A3 * np.sin(w3 * t)
    dy_dt = np.gradient(y, t)  # Derivada de y para el plano fase

    # Limpiar los gráficos anteriores
    ax1.cla()
    ax2.cla()

    # Graficar la combinación lineal de las funciones armónicas
    ax1.plot(t, y, label="y(t)", color="blue")
    ax1.set_title("Combinación Lineal de Funciones Armónicas")
    ax1.set_xlabel("Tiempo (t)")
    ax1.set_ylabel("y(t)")
    ax1.legend()

    # Graficar el plano fase (y, dy/dt)
    ax2.plot(y, dy_dt, label="Plano Fase (y, dy/dt)", color="orange")
    ax2.set_title("Plano Fase")
    ax2.set_xlabel("y(t)")
    ax2.set_ylabel("dy/dt")
    ax2.legend()

    # Redibujar el canvas
    canvas.draw()

# Crear la ventana principal
root = tk.Tk()
root.title("Simulación de Funciones Armónicas")
root.geometry("900x700")
root.resizable(True, True)

# Crear el gráfico usando matplotlib
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10, rowspan=2)

# Crear un marco para los sliders
control_frame = tk.Frame(root)
control_frame.grid(row=0, column=1, padx=10, pady=10)

# Sliders para las amplitudes
A1_slider = tk.Scale(control_frame, from_=0, to=10, orient="horizontal", label="Amplitud A1", resolution=0.1, command=update_plot)
A1_slider.set(1)
A1_slider.pack(fill="x", padx=5, pady=5)

A2_slider = tk.Scale(control_frame, from_=0, to=10, orient="horizontal", label="Amplitud A2", resolution=0.1, command=update_plot)
A2_slider.set(1)
A2_slider.pack(fill="x", padx=5, pady=5)

A3_slider = tk.Scale(control_frame, from_=0, to=10, orient="horizontal", label="Amplitud A3", resolution=0.1, command=update_plot)
A3_slider.set(1)
A3_slider.pack(fill="x", padx=5, pady=5)

# Sliders para las frecuencias angulares
w1_slider = tk.Scale(control_frame, from_=0.1, to=10, orient="horizontal", label="Frecuencia Angular ω1", resolution=0.1, command=update_plot)
w1_slider.set(1)
w1_slider.pack(fill="x", padx=5, pady=5)

w2_slider = tk.Scale(control_frame, from_=0.1, to=10, orient="horizontal", label="Frecuencia Angular ω2", resolution=0.1, command=update_plot)
w2_slider.set(1)
w2_slider.pack(fill="x", padx=5, pady=5)

w3_slider = tk.Scale(control_frame, from_=0.1, to=10, orient="horizontal", label="Frecuencia Angular ω3", resolution=0.1, command=update_plot)
w3_slider.set(1)
w3_slider.pack(fill="x", padx=5, pady=5)

# Iniciar la primera gráfica
update_plot()

# Iniciar el loop principal
root.mainloop()
