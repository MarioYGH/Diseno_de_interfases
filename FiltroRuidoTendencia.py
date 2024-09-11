import numpy as np
import matplotlib.pyplot as plt

nb_points  = 500
x = np.linspace(50, 500, nb_points)

# gaussian peaks
p1 = 20.0 * np.exp(-np.log(2) * ((x-150.0)/15.0)**2)
p2 = 100.0 * np.exp(-np.log(2) * ((x-250.0)/5.0)**2)
p3 = 50.0 * np.exp(-np.log(2) * ((x-450.0)/1.0)**2)
p4 = 20.0 * np.exp(-np.log(2) * ((x-350.0)/30.0)**2)
p5 = 30.0 * np.exp(-np.log(2) * ((x-460.0)/5.0)**2)

# background: a large sin distortion + linear 
bkg = 10*np.sin(x/50) + 0.1*x

# noise
noise = 2.0 * np.random.normal(size=nb_points)

# observation
y = p1 + p2 + p3 + p4 + p5 + noise + bkg
y1 = y

# Creación manual del núcleo Gaussiano
def gaussian_kernel(size, sigma):
    """Crear un kernel Gaussiano de tamaño `size` y desviación estándar `sigma`."""
    kernel = np.exp(-0.5 * (np.arange(size) - size//2)**2 / sigma**2)
    return kernel / np.sum(kernel)  # Normalizar el kernel

# Tamaño y sigma del kernel
kernel_size = 25
sigma = 6

# Crear el kernel Gaussiano
gaussian_kernel = gaussian_kernel(kernel_size, sigma)

# Convolución de los datos usando np.convolve
y_convoluted = np.convolve(y1, gaussian_kernel, mode='same')

# Visualización de los resultados
plt.plot(x, y1, label='Original Data')

plt.figure(figsize=(10, 6))
plt.plot(x, y_convoluted, 'b-', label='Convoluted Data', alpha=0.7, linewidth=2)
plt.legend(loc='best')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Original vs Convoluted Data')
plt.show()
