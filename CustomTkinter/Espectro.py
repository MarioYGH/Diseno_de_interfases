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

# Función para graficar los resultados en dos gráficas separadas
def plot_results(x, y_original, y_filtered, y_final, y_poly, canvas1, canvas2):
    # Primera gráfica: datos originales, filtrados y fondo estimado
    ax1.cla()  # Limpiar el gráfico
    ax1.plot(x, y_original, 'gray', label='Datos Originales', alpha=0.5)
    ax1.plot(x, y_filtered, 'blue', label='Datos Filtrados', alpha=0.7)
    ax1.plot(x, y_poly, 'red', label='Fondo Estimado', alpha=0.7)
    ax1.legend(loc='best')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_title('Datos Originales y Filtrados')
    canvas1.draw()

    # Segunda gráfica: datos filtrados sin fondo
    ax2.cla()  # Limpiar el gráfico
    ax2.plot(x, y_final, 'green', label='Datos Filtrados sin Fondo', linewidth=2)
    ax2.legend(loc='best')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_title('Datos Filtrados sin Fondo')
    canvas2.draw()

# Función para guardar los resultados en un archivo CSV
def save_to_csv():
    file_path = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            data = pd.DataFrame({
                'X': x,
                'Original': y,
                'Filtrado': y_filtered,
                'Fondo Estimado': y_poly,
                'Filtrado sin Fondo': y_final
            })
            data.to_csv(file_path, index=False)
            messagebox.showinfo("Guardar Datos", f"Datos guardados exitosamente en {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar el archivo: {str(e)}")

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

# Función para actualizar las gráficas cuando cambian los parámetros
def update_plot():
    try:
        global y_filtered, y_final, y_poly, kernel_size, sigma, polynomial_order
        y_filtered, y_final, y_poly = process_signal(x, y, kernel_size, sigma, polynomial_order)
        plot_results(x, y, y_filtered, y_final, y_poly, canvas1, canvas2)
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

# Configuración de estilo
ctk.set_appearance_mode("dark")  # Estilo oscuro para la interfaz
ctk.set_default_color_theme("dark-blue")  # Tema de color oscuro

# Crear la ventana principal
root = ctk.CTk()
root.title("Procesamiento de Señal en Tiempo Real")
root.geometry("900x700")
root.configure(bg='black')  # Fondo negro de la ventana

# Crear frame para la selección de archivo y sliders
frame_controls = ctk.CTkFrame(root, fg_color="black")
frame_controls.pack(pady=10)

btn_select_file = ctk.CTkButton(frame_controls, text="Seleccionar Archivo", command=select_file)
btn_select_file.pack(pady=5)

# Botón para guardar los datos
btn_save = ctk.CTkButton(frame_controls, text="Guardar Datos", command=save_to_csv)
btn_save.pack(pady=5)

# Sliders para ajustar los parámetros
slider_kernel_size = ctk.CTkSlider(frame_controls, from_=3, to=21, number_of_steps=19, command=on_kernel_size_change)
slider_kernel_size.set(kernel_size)
slider_kernel_size.pack(pady=5)
label_kernel = ctk.CTkLabel(frame_controls, text="Tamaño del Kernel", text_color="white")
label_kernel.pack()

slider_sigma = ctk.CTkSlider(frame_controls, from_=1, to=100, command=on_sigma_change)
slider_sigma.set(sigma)
slider_sigma.pack(pady=5)
label_sigma = ctk.CTkLabel(frame_controls, text="Sigma", text_color="white")
label_sigma.pack()

slider_polynomial_order = ctk.CTkSlider(frame_controls, from_=1, to=10, command=on_polynomial_order_change)
slider_polynomial_order.set(polynomial_order)
slider_polynomial_order.pack(pady=5)
label_polynomial = ctk.CTkLabel(frame_controls, text="Orden del Polinomio", text_color="white")
label_polynomial.pack()

# Crear un área para las gráficas
frame_plot = ctk.CTkFrame(root, fg_color="black")
frame_plot.pack(fill='both', expand=True)

# Crear dos figuras diferentes para las gráficas
fig1, ax1 = plt.subplots(figsize=(6, 4))
canvas1 = FigureCanvasTkAgg(fig1, master=frame_plot)
canvas1.get_tk_widget().pack(side='left', fill='both', expand=True)

fig2, ax2 = plt.subplots(figsize=(6, 4))
canvas2 = FigureCanvasTkAgg(fig2, master=frame_plot)
canvas2.get_tk_widget().pack(side='left', fill='both', expand=True)

# Iniciar el loop principal
root.mainloop()
