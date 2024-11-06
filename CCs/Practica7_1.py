import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


# Función para actualizar la gráfica
def update_plot(event=None):
    # Obtener valores de los parámetros desde los sliders
    t_i = t_ini_slider.get()
    tiempo_total = t_total_slider.get()
    chi = m_slider.get()
    omega = b_slider.get()
    x0 = x_ini_slider.get()
    v0 = y_ini_slider.get()
    dt = dt_slider.get()

    # Configurar el vector de tiempo
    t = np.arange(t_i, tiempo_total, dt)
    x = np.zeros_like(t)
    z = np.zeros_like(t)
    x[0] = x0  # Condición inicial de posición
    z[0] = v0  # Condición inicial de velocidad

    # Elegir método de integración
    if method.get() == "Runge-Kutta":
        for i in range(1, len(t)):
            g1 = z[i - 1]
            f1 = -2 * chi * omega * z[i - 1] - omega ** 2 * x[i - 1]
            g2 = z[i - 1] + (dt / 2) * f1
            f2 = -2 * chi * omega * (z[i - 1] + (dt / 2) * f1) - omega ** 2 * (x[i - 1] + (dt / 2) * g1)
            g3 = z[i - 1] + (dt / 2) * f2
            f3 = -2 * chi * omega * g3 - omega ** 2 * (x[i - 1] + (dt / 2) * g2)
            g4 = z[i - 1] + dt * f3
            f4 = -2 * chi * omega * g4 - omega ** 2 * (x[i - 1] + dt * g3)
            x[i] = x[i - 1] + (dt / 6) * (g1 + 2 * g2 + 2 * g3 + g4)
            z[i] = z[i - 1] + (dt / 6) * (f1 + 2 * f2 + 2 * f3 + f4)
    else:  # Método de Euler
        for i in range(1, len(t)):
            x[i] = x[i - 1] + dt * z[i - 1]
            z[i] = z[i - 1] + dt * (-2 * chi * omega * z[i - 1] - omega ** 2 * x[i - 1])

    # Transformada de Fourier
    tf = np.fft.fft(x)
    fr = np.fft.fftfreq(len(t), dt)

    # Limpiar el gráfico anterior
    ax.cla()
    ax1.cla()

    # Graficar la posición x(t)
    ax.plot(t, x, label='Posición x(t)', color='blue')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_xlim([0, tiempo_total])
    ax.set_title("Gráfica de la posición x(t)")
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Posición (x)")
    ax.legend()

    # Graficar la transformada de Fourier
    ax1.plot(fr, np.abs(tf), label='Transformada de Fourier', color='orange')
    ax1.axhline(0, color='black', linewidth=0.5)
    ax1.axvline(0, color='black', linewidth=0.5)
    ax1.set_xlim([-10, 10])
    ax1.set_ylim([0, 10])
    ax1.set_title("Transformada de Fourier")
    ax1.set_xlabel("Frecuencia (Hz)")
    ax1.set_ylabel("Magnitud")
    ax1.legend()

    # Redibujar el canvas
    canvas.draw()


# Crear la ventana principal
root = tk.Tk()
root.title("Simulación de Sistemas Dinámicos")
root.geometry("900x700")
root.resizable(True, True)

# Crear el gráfico usando matplotlib
fig, (ax, ax1) = plt.subplots(2, 1, figsize=(6, 8))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10, rowspan=2)

# Crear un marco para los controles
control_frame = tk.Frame(root)
control_frame.grid(row=0, column=1, padx=10, pady=10)

# Crear sliders para los parámetros
m_slider = tk.Scale(control_frame, from_=0, to=1, orient='horizontal', label='Damping Ratio (χ)', resolution=0.1,
                    command=update_plot)
m_slider.set(0.5)
m_slider.pack(fill='x', padx=5, pady=5)

b_slider = tk.Scale(control_frame, from_=0.1, to=10, orient='horizontal', label='Frecuencia Angular (ω)',
                    resolution=0.1, command=update_plot)
b_slider.set(1)
b_slider.pack(fill='x', padx=5, pady=5)

x_ini_slider = tk.Scale(control_frame, from_=-10, to=10, orient='horizontal', label='Posición Inicial (x₀)',
                        resolution=0.1, command=update_plot)
x_ini_slider.set(0.0)
x_ini_slider.pack(fill='x', padx=5, pady=5)

y_ini_slider = tk.Scale(control_frame, from_=-10, to=10, orient='horizontal', label='Velocidad Inicial (ẋ₀)',
                        resolution=0.1, command=update_plot)
y_ini_slider.set(0.0)
y_ini_slider.pack(fill='x', padx=5, pady=5)

t_ini_slider = tk.Scale(control_frame, from_=0, to=5, orient='horizontal', label='Tiempo Inicial (t₀)', resolution=0.1,
                        command=update_plot)
t_ini_slider.set(0.0)
t_ini_slider.pack(fill='x', padx=5, pady=5)

t_total_slider = tk.Scale(control_frame, from_=5, to=20, orient='horizontal', label='Tiempo de Simulación',
                          resolution=0.1, command=update_plot)
t_total_slider.set(10.0)
t_total_slider.pack(fill='x', padx=5, pady=5)

# Slider de paso de integración (Nyquist)
dt_slider = tk.Scale(control_frame, from_=0.001, to=0.05, orient='horizontal', label='Paso de Integración (dt)',
                     resolution=0.001, command=update_plot)
dt_slider.set(0.01)
dt_slider.pack(fill='x', padx=5, pady=5)

# Radio buttons para seleccionar el método de integración
method = tk.StringVar(value="Runge-Kutta")
tk.Radiobutton(control_frame, text="Runge-Kutta", variable=method, value="Runge-Kutta", command=update_plot).pack(
    anchor='w')
tk.Radiobutton(control_frame, text="Euler", variable=method, value="Euler", command=update_plot).pack(anchor='w')

# Iniciar la primera gráfica
update_plot()

# Iniciar el loop principal
root.mainloop()