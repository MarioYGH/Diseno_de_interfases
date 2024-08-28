import cv2
import numpy as np

def binario_a_texto(binario):
    texto = ""
    for i in range(0, len(binario), 8):
        byte = binario[i:i+8]
        if len(byte) < 8:
            break
        texto += chr(int(byte, 2))
    return texto

def extraer_texto_de_imagen(img):
    # Dividir la imagen en canales RGB
    b, g, r = cv2.split(img)

    # Extraer cada bit de los LSB de los canales R, G y B
    binario_extraido = []
    alto, ancho = b.shape
    
    for i in range(alto):
        for j in range(ancho):
            binario_extraido.append(str(r[i, j] & 1))
            binario_extraido.append(str(g[i, j] & 1))
            binario_extraido.append(str(b[i, j] & 1))

    # Convertir la lista de bits a una cadena de texto
    binario_extraido = ''.join(binario_extraido)

    longitud_restablecer = (len(binario_extraido) // 8) * 8
    binario_extraido = binario_extraido[:longitud_restablecer]

    return binario_a_texto(binario_extraido)

# Leer la imagen
img = cv2.imread('Examen_modificado.png')

# Extraer el texto de la imagen
texto_extraido = extraer_texto_de_imagen(img)

# Mostrar el texto extraído
print("Texto extraído:", texto_extraido)
