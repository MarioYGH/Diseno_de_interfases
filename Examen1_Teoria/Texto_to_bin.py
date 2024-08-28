from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
# image = Image.open('Examen.jpg') 
image = plt.imread('Examen2.jpg')

# Mostrar la imagen original
plt.imshow(image)
#plt.axis('off')
#plt.show()

igray = np.round((1/3)*np.sum(image, 2)*255)

plt.imshow(igray)

# Texto a binario

def texto_a_binario(texto):
    binario = ''.join(format(ord(char), '08b') for char in texto)
    return binario

# Ejemplo de uso
texto = "Hola "
resultado_binario = texto_a_binario(texto)
print(resultado_binario)
