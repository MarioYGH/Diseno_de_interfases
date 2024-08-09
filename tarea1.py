import numpy as np
import time


n = 100
m = 100
A = np.zeros((n, m))

for i in range(m):
    A[:, i] = np.random.permutation(np.arange(1, m + 1))

print(A)

numero_a_buscar = 1

resultado = np.full(m, -1)  

tic = time.time()


for columna in range(m):
    for fila in range(n):
        if A[fila, columna] == numero_a_buscar:
            resultado[columna] = fila
            break  # Salir del bucle de filas si se encuentra el número

print(f"Vector resultado: {resultado}")

toc = time.time()
tiempo = toc - tic
print(tiempo)

