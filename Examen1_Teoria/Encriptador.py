import cv2
import numpy as np

def texto_a_binario(texto):
    return ''.join(format(ord(char), '08b') for char in texto)

def insertar_texto_en_imagen(img, texto_binario):
    # Dividir la imagen en canales RGB
    b, g, r = cv2.split(img)

    # Inicializar tensores para almacenar los bits
    tensor_b = np.zeros((8, b.shape[0], b.shape[1]), dtype=np.uint8)
    tensor_g = np.zeros((8, g.shape[0], g.shape[1]), dtype=np.uint8)
    tensor_r = np.zeros((8, r.shape[0], r.shape[1]), dtype=np.uint8)

    # Extraer cada bit y almacenarlo en el tensor correspondiente
    for i in range(8):  
        tensor_b[i] = (b >> i) & 1
        tensor_g[i] = (g >> i) & 1
        tensor_r[i] = (r >> i) & 1

    # Insertar el texto binario en los LSB de los tensores R, G y B
    idx = 0
    for i in range(tensor_r.shape[1]): # Alto y ancho de imagen 
        for j in range(tensor_r.shape[2]):
            if idx < len(texto_binario):
                tensor_r[0, i, j] = int(texto_binario[idx])
                idx += 1
            elif idx < len(texto_binario):
                tensor_g[0, i, j] = int(texto_binario[idx])
                idx += 1
            elif idx < len(texto_binario):
                tensor_b[0, i, j] = int(texto_binario[idx])
                idx += 1

    # Reconstruir los canales R, G, B con los nuevos LSB
    r_mod = (tensor_r[7] << 7 | tensor_r[6] << 6 | tensor_r[5] << 5 |
             tensor_r[4] << 4 | tensor_r[3] << 3 | tensor_r[2] << 2 |
             tensor_r[1] << 1 | tensor_r[0])
    g_mod = (tensor_g[7] << 7 | tensor_g[6] << 6 | tensor_g[5] << 5 |
             tensor_g[4] << 4 | tensor_g[3] << 3 | tensor_g[2] << 2 |
             tensor_g[1] << 1 | tensor_g[0])
    b_mod = (tensor_b[7] << 7 | tensor_b[6] << 6 | tensor_b[5] << 5 |
             tensor_b[4] << 4 | tensor_b[3] << 3 | tensor_b[2] << 2 |
             tensor_b[1] << 1 | tensor_b[0])

    # Reconstruir la imagen
    img_mod = cv2.merge([b_mod, g_mod, r_mod])
    return img_mod

# Leer la imagen
img = cv2.imread('Examen.jpg')

# Pedir texto 
texto = input("Introduce textoq que vas a encriptar: ")
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
