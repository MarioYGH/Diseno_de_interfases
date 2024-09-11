import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parámetros clave para ajustar
kernel_size = 5  # Tamaño del kernel: aumentar suaviza más pero pierde detalle; disminuir retiene más detalle
sigma = 30       # Desviación estándar del Gaussiano: aumentar suaviza más; disminuir deja más ruido
polynomial_order = 5  # Orden del polinomio: aumentar captura más detalles del fondo; disminuir suaviza el ajuste

# Función para leer datos desde un archivo CSV
def read_data_from_csv(file_path):
    data = pd.read_csv(file_path)
    # Suponemos que el archivo tiene dos columnas: 'x' y 'y'
    x = data.iloc[:, 0].values  # Columna 'x'
    y = data.iloc[:, 1].values  # Columna 'y'
    
    return x, y

# Función para crear un kernel Gaussiano
def gaussian_kernel(size, sigma):
    """Generar un kernel Gaussiano de tamaño `size` con desviación estándar `sigma`."""
    kernel = np.exp(-0.5 * (np.arange(size) - size // 2) ** 2 / sigma ** 2)
    return kernel / np.sum(kernel)  # Normalizar

# Función que filtra la señal, ajusta un polinomio y elimina el fondo
def process_signal(x, y, kernel_size, sigma, polynomial_order):
    # Filtrar la señal con un núcleo Gaussiano
    gaussian_kernel_small = gaussian_kernel(kernel_size, sigma)
    y_filtered = np.convolve(y, gaussian_kernel_small, mode='same')  # Suavizado

    # Ajustar un polinomio a la señal filtrada
    coefficients = np.polyfit(x, y_filtered, polynomial_order)
    y_poly = np.polyval(coefficients, x)
    
    # Restar el polinomio de la señal filtrada
    y_final = y_filtered - y_poly
    
    return y_filtered, y_final, y_poly

# Función para graficar los resultados
def plot_results(x, y_original, y_filtered, y_final, y_poly):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y_original, 'gray', label='Datos Originales', alpha=0.5)
    plt.plot(x, y_filtered, 'blue', label='Datos Filtrados', alpha=0.7)
    plt.plot(x, y_poly, 'red', label='Fondo Estimado', alpha=0.7)
    plt.plot(x, y_final, 'green', label='Datos Filtrados sin Fondo', linewidth=2)
    
    plt.legend(loc='best')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Comparación de Señales: Original vs Filtrada vs Fondo')
    plt.show()

# Función principal
def main(csv_file_path):
    x, y = read_data_from_csv(csv_file_path)  # Cargar datos
    y_filtered, y_final, y_poly = process_signal(x, y, kernel_size, sigma, polynomial_order)  # Procesar señal
    plot_results(x, y, y_filtered, y_final, y_poly)  # Mostrar resultados

# Ejecutar con el archivo CSV
csv_file_path = 'espectro.csv'  # Especifica la ruta de tu archivo CSV
main(csv_file_path)
