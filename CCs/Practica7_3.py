import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


# Función para calcular la serie de Fourier de f(t) = |t|
def fourier_series(t, terms):
    approx = np.zeros_like(t)
    for n in range(1, terms + 1):
        # Calculando los términos de la serie de Fourier para |t|
        coef = (-1) ** (n + 1) * 2 / (n * np.pi)
        approx += coef * np.sin(n * t)
    return approx + np.pi / 2  # Ajuste para centrar la aproximación


# Función para actualizar la gráfica
def update_plot(event=None):
    # Obtener el número de términos
    terms = terms_slider.get()

    # Calcular la función original y la serie de Fourier
    t = np.linspace(-np.pi, np.pi, 1000)
    f_t = np.abs(t)  # Función original
    f_approx = fourier_series(t, terms)  # Aproximación de la serie de Fourier

    # Limpiar los gráficos anteriores
    ax1.cla()
    ax2.cla()

    # Graficar la función original f(t) = |t|
    ax1.plot(t, f_t, label="f(t) = |t|", color="blue")
    ax1.set_title("Función f(t) = |t|")
    ax1.set_xlabel("t")
    ax1.set_ylabel("f(t)")
    ax1.legend()

    # Graficar la función original y la aproximación de la serie de Fourier
    ax2.plot(t, f_t, label="f(t) = |t|", color="blue", linestyle="--")
    ax2.plot(t, f_approx, label=f"Serie de Fourier con {terms} términos", color="orange")
    ax2.set_title("Aproximación de Fourier de f(t)")
    ax2.set_xlabel("t")
    ax2.set_ylabel("f(t)")
    ax2.legend()

    # Redibujar el canvas
    canvas.draw()


# Crear la ventana principal
root = tk.Tk()
root.title("Aproximación de Fourier de la Función |t|")
root.geometry("900x700")
root.resizable(True, True)

# Crear el gráfico usando matplotlib
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10, rowspan=2)

# Crear un marco para los controles
control_frame = tk.Frame(root)
control_frame.grid(row=0, column=1, padx=10, pady=10)

# Slider para seleccionar el número de términos de la serie de Fourier
terms_slider = tk.Scale(control_frame, from_=1, to=50, orient="horizontal", label="Número de Términos de Fourier",
                        command=update_plot)
terms_slider.set(5)
terms_slider.pack(fill="x", padx=5, pady=5)

# Iniciar la primera gráfica
update_plot()

# Iniciar el loop principal
root.mainloop()