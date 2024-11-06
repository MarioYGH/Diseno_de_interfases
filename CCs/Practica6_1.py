import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Función para actualizar la gráfica y los valores de los sliders
def update_plot(event=None):
    t_i = t_ini.get()
    t_i = float(t_i)
    tiempo_total = 10  # Tiempo total en segundos

    chi = m_slider.get()
    omega = b_slider.get()
    dt = 0.01
    if omega != 0:
        dt = abs(1 / (2 * omega))
    t = np.arange(t_i, tiempo_total, dt)  # Vector de tiempo
    x = np.zeros_like(t)
    z = np.zeros_like(t)

    x[0] = float(x_ini.get())  # Valor inicial de x
    z[0] = float(y_ini.get())  # Valor inicial de x'

    for i in range(1, len(t)):
        g1 = z[i - 1]
        f1 = -2 * chi * omega * z[i - 1] - ((omega) ** 2) * x[i - 1]
        g2 = z[i - 1] + (dt / 2) * f1
        f2 = -2 * chi * omega * (z[i - 1] + (dt / 2) * f1) - ((omega) ** 2) * (x[i - 1] + (dt / 2) * g1)
        g3 = z[i - 1] + (dt / 2) * f2
        f3 = -2 * chi * omega * g3 - ((omega) ** 2) * (x[i - 1] + (dt / 2) * g2)
        g4 = z[i - 1] + dt * f3
        f4 = -2 * chi * omega * g4 - ((omega) ** 2) * (x[i - 1] + dt * g3)
        x[i] = x[i - 1] + (dt / 6) * (g1 + 2 * g2 + 2 * g3 + g4)
        z[i] = z[i - 1] + (dt / 6) * (f1 + 2 * f2 + 2 * f3 + f4)

    tf = np.fft.fft(x)
    fr = np.fft.fftfreq(len(t), t[0] - t[1])

    # Limpiar el gráfico anterior
    ax.cla()
    ax1.cla()

    # Dibujar la nueva línea para la gráfica de la solución
    ax.plot(t, x, color='blue', label='x(t)', linewidth=2)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_xlim([0, tiempo_total])
    ax.set_ylim([min(x) - 1, max(x) + 1])
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend()
    ax.set_title("Gráfica de la solución")
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("x(t)")

    # Dibujar la nueva línea para la transformada de Fourier
    ax1.plot(fr, np.abs(tf), color='orange', label='Tf(x)', linewidth=2)  # Usar el valor absoluto de la FFT
    ax1.axhline(0, color='black', linewidth=0.5)
    ax1.axvline(0, color='black', linewidth=0.5)
    ax1.set_xlim([-10, 10])
    ax1.set_ylim([0, np.max(np.abs(tf)) + 1])  # Ajustar el límite superior
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.legend()
    ax1.set_title("Transformada de Fourier")
    ax1.set_xlabel("Frecuencia (Hz)")
    ax1.set_ylabel("Tf(x)")

    # Redibujar el canvas
    canvas.draw()

    # Actualizar las etiquetas de los sliders
    m_value_label.configure(text=f'Valor de z: {chi:.2f}')
    b_value_label.configure(text=f'Valor de omega: {omega:.2f}')
    x_value_label.configure(text=f'Valor de x0: {x_ini.get():.2f}')
    y_value_label.configure(text=f'Valor de y0: {y_ini.get():.2f}')
    t_value_label.configure(text=f'Valor de t0: {t_ini.get():.2f}')


# Crear la ventana principal
app = ctk.CTk()
app.title("Gráfica de oscilador armonico amortiguado")
app.geometry("900x600")  # Ajustar el tamaño de la ventana

# Crear el gráfico usando matplotlib
fig, (ax, ax1) = plt.subplots(2, 1, figsize=(7, 6))  # Aumentar el tamaño de las gráficas
plt.subplots_adjust(hspace=0.4)  # Ajustar el espacio entre las gráficas
canvas = FigureCanvasTkAgg(fig, master=app)
canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10, rowspan=6)

# Crear un marco para los sliders
slider_frame = ctk.CTkFrame(app)
slider_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Crear los sliders para m y b
m_slider = ctk.CTkSlider(slider_frame, from_=0, to=1, orientation='horizontal', command=update_plot)
m_slider.set(1)  # Valor inicial de m
m_slider.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
m_value_label = ctk.CTkLabel(slider_frame, text='Valor de z: 1.00')
m_value_label.grid(row=1, column=0)

b_slider = ctk.CTkSlider(slider_frame, from_=-10, to=10, orientation='horizontal', command=update_plot)
b_slider.set(0)  # Valor inicial de b
b_slider.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
b_value_label = ctk.CTkLabel(slider_frame, text='Valor de omega: 0.00')
b_value_label.grid(row=3, column=0)

x_ini = ctk.CTkSlider(slider_frame, from_=-10, to=10, orientation='horizontal', command=update_plot)
x_ini.set(0)  # Valor inicial de x0
x_ini.grid(row=4, column=0, padx=10, pady=10, sticky="ew")
x_value_label = ctk.CTkLabel(slider_frame, text='Valor de x0: 0.00')
x_value_label.grid(row=5, column=0)

y_ini = ctk.CTkSlider(slider_frame, from_=-10, to=10, orientation='horizontal', command=update_plot)
y_ini.set(0)  # Valor inicial de y0
y_ini.grid(row=6, column=0, padx=10, pady=10, sticky="ew")
y_value_label = ctk.CTkLabel(slider_frame, text='Valor de y0: 0.00')
y_value_label.grid(row=7, column=0)

t_ini = ctk.CTkSlider(slider_frame, from_=-1, to=1, orientation='horizontal', command=update_plot)
t_ini.set(0)  # Valor inicial de t0
t_ini.grid(row=8, column=0, padx=10, pady=10, sticky="ew")
t_value_label = ctk.CTkLabel(slider_frame, text='Valor de t0: 0.00')
t_value_label.grid(row=9, column=0)

# Dibujar la primera gráfica
update_plot()

# Iniciar el loop principal
app.mainloop()
