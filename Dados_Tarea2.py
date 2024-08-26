# 2 Dados-6D

# Reglas conejo
# * = 12 ---> 24
# * <= 3 --->-pasos*2

# Reglas Ratón 
# >= 8 ----> 2*pasos
# <= 5 ----> -2*pasos

# Tortuga 
# pasos = pasos

# Sapo 
# Par ---> 3*pasos
# Mult 3 ---> -20
# resto ----> 0 

# Escarabajo 
# >= 10 ----> 50
# <10 ----> 0 

import random as rnd

# Inicializar variables para acumular las sumas de cada simulación
suma_total_dados = 0
suma_total_dadoconejo = 0
suma_total_dadoraton = 0
suma_total_dadotortuga = 0
suma_total_dadosapo = 0
suma_total_dadoescarabajo = 0

total_juegos = 1000
total_tiradas = total_juegos*100

for _ in range(total_juegos):
    # Inicializar listas para guardar los resultados
    dados = []
    dadoconejo = []
    dadoraton = []
    dadotortuga = []
    dadosapo = []
    dadoescarabajo = []
    
    # Simulación de 100 lanzamientos
    for _ in range(100):
        r1 = rnd.randrange(1, 7)
        r2 = rnd.randrange(1, 7)
        dado = r1 + r2
        dados.append(dado)
    
        # Conejo
        if dado == 12:
            dadoconejo.append(24)
        elif dado <= 3:
            dadoconejo.append(dado * -1 * 2)
        else:
            dadoconejo.append(dado)
    
        # Ratón
        if dado >= 8:
            dadoraton.append(2 * dado)
        elif dado <= 5:
            dadoraton.append(dado * -1 * 2)
        else:
            dadoraton.append(dado)
    
        # Tortuga
        dadotortuga.append(dado)
    
        # Sapo
        if dado % 2 == 0:
            dadosapo.append(3 * dado)
        elif dado % 3 == 0:
            dadosapo.append(-20)
        else:
            dadosapo.append(0)
    
        # Escarabajo
        if dado >= 10:
            dadoescarabajo.append(50)
        else:
            dadoescarabajo.append(0)
    
    # # Imprimir resultados finales
    # print("Dados:", dados)
    # print("Conejo:", dadoconejo)
    # print("Ratón:", dadoraton)
    # print("Tortuga:", dadotortuga)
    # print("Sapo:", dadosapo)
    # print("Escarabajo:", dadoescarabajo)
    
    # Sumar los elementos de cada lista
    suma_dados = sum(dados)
    suma_dadoconejo = sum(dadoconejo)
    suma_dadoraton = sum(dadoraton)
    suma_dadotortuga = sum(dadotortuga)
    suma_dadosapo = sum(dadosapo)
    suma_dadoescarabajo = sum(dadoescarabajo)

    # Acumular las sumas en las variables totales
    suma_total_dados += suma_dados
    suma_total_dadoconejo += suma_dadoconejo
    suma_total_dadoraton += suma_dadoraton
    suma_total_dadotortuga += suma_dadotortuga
    suma_total_dadosapo += suma_dadosapo
    suma_total_dadoescarabajo += suma_dadoescarabajo

# Imprimir las sumas totales después de 1000 simulaciones
print("Suma total de dados:", suma_total_dados)
print("Suma total de Conejo:", suma_total_dadoconejo)
print("Suma total de Ratón:", suma_total_dadoraton)
print("Suma total de Tortuga:", suma_total_dadotortuga)
print("Suma total de Sapo:", suma_total_dadosapo)
print("Suma total de Escarabajo:", suma_total_dadoescarabajo)

print("Promedio de Conejo:", suma_total_dadoconejo/total_tiradas)
print("Promedio de Ratón:", suma_total_dadoraton/total_tiradas)
print("Promedio de Tortuga:", suma_total_dadotortuga/total_tiradas)
print("Promedio de Sapo:", suma_total_dadosapo/total_tiradas)
print("Promedio de Escarabajo:", suma_total_dadoescarabajo/total_tiradas)

 






