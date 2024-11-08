# Diseñe una interfaz gráfica que permita ingresar el número de términos de la la serie de Fourier de la función f(t) que fue proporcionada en clase. Incluya un Axes que
# muestre la función f(t) y un segundo Axes donde se muestren las funciones f(t) y la serie de Fourier.
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Función para calcular la serie de Fourier para -x en [-1, 0]
def fourier_series_negative_x(x, n_terms):
    a0 = 0  # Coeficiente constante
    series = a0 / 2
    for n in range(1, n_terms + 1):
        bn = 2 * ((-1) ** n) / (n * np.pi)
        series += bn * np.sin(n * np.pi * x)
    return series

# Función para calcular la serie de Fourier para x en [0, 1]
def fourier_series_positive_x(x, n_terms):
    a0 = 0  # Coeficiente constante
    series = a0 / 2
    for n in range(1, n_terms + 1):
        bn = -2 * ((-1) ** n) / (n * np.pi)
        series += bn * np.sin(n * np.pi * x)
    return series

# Función para actualizar la gráfica
def update_plot(event=None):
    n_terms = terms_slider.get()
    domain = domain_slider.get()  # Obtener el intervalo del dominio

    # Definimos los intervalos basados en el valor del dominio
    x1 = np.linspace(-domain, 0, 5000)
    x2 = np.linspace(0, domain, 5000)

    # Calculamos las funciones originales
    y1 = -x1
    y2 = x2

    # Calculamos las aproximaciones de Fourier
    y1_fourier = fourier_series_negative_x(x1, n_terms)
    y2_fourier = fourier_series_positive_x(x2, n_terms)

    # Unimos los intervalos
    x_combined = np.concatenate((x1, x2))
    y_combined = np.concatenate((y1, y2))
    y_fourier_combined = np.concatenate((y1_fourier, y2_fourier))

    # Limpiar los gráficos anteriores
    ax.cla()

    # Graficar las funciones originales y la serie de Fourier
    ax.plot(x_combined, y_combined, label='|X|', color='black')
    ax.plot(x_combined, y_fourier_combined, label=f'Serie de Fourier con {n_terms} términos', color='red')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.set_title('Aproximación de Fourier para -x y x')
    ax.grid()

    # Redibujar el canvas
    canvas.draw()

# Crear la ventana principal
root = tk.Tk()
root.title("Aproximación de Fourier de -x y x con Dominio Variable")
root.geometry("900x700")

# Crear el gráfico usando matplotlib
fig, ax = plt.subplots(figsize=(8, 6))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Crear un marco para los controles
control_frame = tk.Frame(root)
control_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

# Slider para seleccionar el número de términos de la serie de Fourier
terms_slider = tk.Scale(control_frame, from_=1, to=100, orient="horizontal", label="Número de Términos de Fourier",
                        command=update_plot)
terms_slider.set(1)  # Valor inicial ajustado a 1
terms_slider.pack(fill="x", padx=5, pady=5)

# Slider para seleccionar el intervalo del dominio
domain_slider = tk.Scale(control_frame, from_=1, to=5, resolution=0.1, orient="horizontal", label="Intervalo del Dominio",
                         command=update_plot)
domain_slider.set(2)  # Valor inicial ajustado a 2
domain_slider.pack(fill="x", padx=5, pady=5)

# Iniciar la primera gráfica con n_terms = 1 y dominio = 2
update_plot()

# Iniciar el loop principal
root.mainloop()

# es que me dijo ah simon y si lo cambias a intervalo de 2, y yo dije si jala
