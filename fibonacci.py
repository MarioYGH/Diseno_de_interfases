import numpy as np

n = 11
x = 0 #primer numero
y = 1 #segundo numero

for i in range(1,n):
    z = y + x #suma de los dos numeros
    y = x #cambias el valor del segundo numero por el que tenia el primero
    x = z #asignas el valor de de z al primer numero 
    
    print(x)
    
