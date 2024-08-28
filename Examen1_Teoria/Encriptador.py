import cv2
import numpy as np

def texto_a_binario(texto):
    return ''.join(format(ord(char), '08b') for char in texto)

def insertar_texto_en_imagen(img, texto_binario):
    # Dividir la imagen en canales RGB
    b, g, r = cv2.split(img)

    # Inicializar tensores para almacenar los bits
    alto, ancho = b.shape
    tensor_b = np.zeros((8, alto, ancho), dtype=np.uint8)
    tensor_g = np.zeros((8, alto, ancho), dtype=np.uint8)
    tensor_r = np.zeros((8, alto, ancho), dtype=np.uint8)

    # Extraer cada bit y almacenarlo en el tensor correspondiente
    for i in range(8):
        tensor_b[i] = (b >> i) & 1
        tensor_g[i] = (g >> i) & 1
        tensor_r[i] = (r >> i) & 1

    # Insertar el texto binario en los LSB de los tensores R, G y B
    idx = 0
    for i in range(alto):
        for j in range(ancho):
            if idx < len(texto_binario):
                # Insertar el bit en los LSB de R, G y B
                tensor_r[0, i, j] = int(texto_binario[idx])
                idx += 1
            if idx < len(texto_binario):
                tensor_g[0, i, j] = int(texto_binario[idx])
                idx += 1
            if idx < len(texto_binario):
                tensor_b[0, i, j] = int(texto_binario[idx])
                idx += 1

            if idx >= len(texto_binario):
                # Poner cero al resto
                while idx < len(texto_binario):
                    tensor_r[0, i, j] = 0
                    tensor_g[0, i, j] = 0
                    tensor_b[0, i, j] = 0
                    idx += 1
                    
                # Restablecer las posiciones restantes en la imagen
                for k in range(j, ancho):
                    tensor_r[0, i, k] = 0
                    tensor_g[0, i, k] = 0
                    tensor_b[0, i, k] = 0
                for l in range(i + 1, alto):
                    for k in range(ancho):
                        tensor_r[0, l, k] = 0
                        tensor_g[0, l, k] = 0
                        tensor_b[0, l, k] = 0
                break


    # Reconstruir los canales R, G, B con los nuevos LSB
    r_mod = np.zeros_like(r)
    g_mod = np.zeros_like(g)
    b_mod = np.zeros_like(b)

    for i in range(8):
        r_mod |= tensor_r[i] << i
        g_mod |= tensor_g[i] << i
        b_mod |= tensor_b[i] << i

    # Reconstruir la imagen
    img_mod = cv2.merge([b_mod, g_mod, r_mod])
    return img_mod

# Leer la imagen
img = cv2.imread('Examen.jpg')

# Pedir texto 
texto = input("Introduce texto que vas a encriptar: ")
texto_binario = texto_a_binario(texto)

# Verificar tamaño texto
if len(texto_binario) > img.size * 3:
   print("El texto es muy grande.")
else:
    # Insertar el texto en la imagen
    img_mod = insertar_texto_en_imagen(img, texto_binario)
    
    # Guardar y mostrar la nueva imagen
    cv2.imwrite('Examen_modificado.png', img_mod)
    cv2.imshow('Imagen Modificada', img_mod)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
