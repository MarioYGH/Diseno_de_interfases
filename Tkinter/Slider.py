import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Funcion diseñada para usar matplt en tkinter
import numpy as np

# Función para actualizar la gráfica
def update_plot(event=None):
    m = m_slider.get() # Adquirimos el valor de los sliders
    b = b_slider.get()
    
    # Limpiar el gráfico anterior
    ax.cla()  # Limpia los ejes, ax es el marco del plot 
    
    # Generar nuevos datos
    x = np.linspace(-10, 10, 100)
    y = m * x + b
    
    # Dibujar la nueva línea
    ax.plot(x, y, label=f'y = {m:.2f}x + {b:.2f}')
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.legend()
    
    # Redibujar el canvas
    canvas.draw()

# Crear la ventana principal
root = tk.Tk()
root.title("Gráfica de la ecuación y = mx + b")
root.resizable(False,False)

# Crear el gráfico usando matplotlib
fig, ax = plt.subplots(figsize=(5, 4)) # Genera la firgura y ejes en siultaneo
canvas = FigureCanvasTkAgg(fig, master=root) # La variable canvas va a asignar la fig de arriba en el root, o frame o lo que se tenga
canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10, rowspan=2) # Acá lo convierte en widget y asigna posicion

# Crear los sliders para m y b
m_slider = tk.Scale(root, from_=-10, to=10, orient='horizontal', label='Valor de m', resolution=0.1, command=update_plot) # El slider en un scale
m_slider.set(1)  # Valor inicial de m
m_slider.grid(row=0, column=1, padx=10, pady=10)

b_slider = tk.Scale(root, from_=-10, to=10, orient='horizontal', label='Valor de b', resolution=0.1, command=update_plot,)
b_slider.set(0)  # Valor inicial de b
b_slider.grid(row=1, column=1, padx=10, pady=10,sticky="e")



# Dibujar la primera gráfica
update_plot() # Va cambiando la grafica en tiempo real, MUY IMPORTANTE

# Iniciar el loop principal
root.mainloop()
