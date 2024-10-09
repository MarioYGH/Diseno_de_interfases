import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import customtkinter as ctk
from tkinter import filedialog
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Parámetros iniciales
kernel_size = 5
sigma = 30
polynomial_order = 5

# Función para leer datos desde un archivo CSV
def read_data_from_csv(file_path):
    data = pd.read_csv(file_path)
    x = data.iloc[:, 0].values
    y = data.iloc[:, 1].values
    return x, y

# Función para crear un kernel Gaussiano
def gaussian_kernel(size, sigma):
    kernel = np.exp(-0.5 * (np.arange(size) - size // 2) ** 2 / sigma ** 2)
    return kernel / np.sum(kernel)

# Función para procesar la señal
def process_signal(x, y, kernel_size, sigma, polynomial_order):
    gaussian_kernel_small = gaussian_kernel(kernel_size, sigma)
    y_filtered = np.convolve(y, gaussian_kernel_small, mode='same')

    coefficients = np.polyfit(x, y_filtered, polynomial_order)
    y_poly = np.polyval(coefficients, x)

    y_final = y_filtered - y_poly

    return y_filtered, y_final, y_poly

# Función para graficar los resultados
def plot_results(x, y_original, y_filtered, y_final, y_poly, canvas):
    plt.clf()
    plt.plot(x, y_original, 'gray', label='Datos Originales', alpha=0.5)
    plt.plot(x, y_filtered, 'blue', label='Datos Filtrados', alpha=0.7)
    plt.plot(x, y_poly, 'red', label='Fondo Estimado', alpha=0.7)
    plt.plot(x, y_final, 'green', label='Datos Filtrados sin Fondo', linewidth=2)
    
    plt.legend(loc='best')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Comparación de Señales: Original vs Filtrada vs Fondo')
    
    canvas.draw()

# Función que se ejecuta cuando se selecciona un archivo
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            global x, y
            x, y = read_data_from_csv(file_path)
            update_plot()
        except Exception as e:
            messagebox.showerror("Error", f"Error al leer el archivo: {str(e)}")

# Función para actualizar la gráfica cuando cambian los parámetros
def update_plot():
    try:
        global kernel_size, sigma, polynomial_order
        y_filtered, y_final, y_poly = process_signal(x, y, kernel_size, sigma, polynomial_order)
        plot_results(x, y, y_filtered, y_final, y_poly, canvas)
    except Exception as e:
        messagebox.showerror("Error", f"Error al procesar la señal: {str(e)}")

# Función para actualizar los parámetros desde los sliders
def on_kernel_size_change(value):
    global kernel_size
    kernel_size = int(value)
    update_plot()

def on_sigma_change(value):
    global sigma
    sigma = float(value)
    update_plot()

def on_polynomial_order_change(value):
    global polynomial_order
    polynomial_order = int(value)
    update_plot()

# Crear la ventana principal
root = ctk.CTk()
root.title("Procesamiento de Señal en Tiempo Real")
root.geometry("900x700")

# Crear frame para la selección de archivo y sliders
frame_controls = ctk.CTkFrame(root)
frame_controls.pack(pady=10)

btn_select_file = ctk.CTkButton(frame_controls, text="Seleccionar Archivo", command=select_file)
btn_select_file.pack(pady=5)

# Sliders para ajustar los parámetros
slider_kernel_size = ctk.CTkSlider(frame_controls, from_=3, to=21, number_of_steps=19, command=on_kernel_size_change)
slider_kernel_size.set(kernel_size)
slider_kernel_size.pack(pady=5)
label_kernel = ctk.CTkLabel(frame_controls, text="Tamaño del Kernel")
label_kernel.pack()

slider_sigma = ctk.CTkSlider(frame_controls, from_=1, to=100, command=on_sigma_change)
slider_sigma.set(sigma)
slider_sigma.pack(pady=5)
label_sigma = ctk.CTkLabel(frame_controls, text="Sigma")
label_sigma.pack()

slider_polynomial_order = ctk.CTkSlider(frame_controls, from_=1, to=10, command=on_polynomial_order_change)
slider_polynomial_order.set(polynomial_order)
slider_polynomial_order.pack(pady=5)
label_polynomial = ctk.CTkLabel(frame_controls, text="Orden del Polinomio")
label_polynomial.pack()

# Crear un área para la gráfica
frame_plot = ctk.CTkFrame(root)
frame_plot.pack(fill='both', expand=True)

fig, ax = plt.subplots(figsize=(8, 6))
canvas = FigureCanvasTkAgg(fig, master=frame_plot)
canvas.get_tk_widget().pack(fill='both', expand=True)

# Iniciar el loop principal
root.mainloop()
