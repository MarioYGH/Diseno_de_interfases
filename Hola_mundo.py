# ctrl + 1 es para agregar un comentario, se pueden seleccionar varias lineas
# la extension .py es de python
# ctrl + l limpia la consola 
# F5 ejecutra el script, igual ctrl + enter 
# F9 corren la linea activa 
# La bolita roja es indicador de un error de sintaxis
# Todo lo que este dentro de comillas es caracter
# Python cuenta desde cero
# La identacion es vital en python 

a = 5 
b = 3.5
z = "Hola mundo "
print(z)
print("\nHola mundo otra vez")

z2 = z*3 #aca estamos multiplicando una cadena de caracteres

a, b, c = 41, 42, 43 #asignacion multiple
x1 = x2 = x3 = 456 #otro modo de asignacion multiple

# %%
# así se divide y crea un apartado que se puede ejecutar por separado 
m = 56 

suma = 6 + 4
resta = 6 - 2 
mult = 6*6
div = 6 / 2
potencia = 2**2 #con doble asterisco, el gorrito no jala
raiz = 2**(0.5)
div_entera = 5//2 #doble slash
madulo = 5%2

numeros_complejos = 3 + 6j #la j es el imaginario y debe de estar pegada al numero 
#Se puede hacer calculo simbolico 
lista0 = [] #lista vacia
lista = [3,5,8] #lista
lista1 = [1,4,89,"hola",2+5j,"Mateo","Alan",lista] #Puedes guardar cualquier cosa en una lista  

r1 = lista1[0] #primer elemento 
r2 = lista1[-1] #ultimo elemento
r3 = lista1[-2] #pen ultimo elemento
r4 = lista1[2:5] #del elemento 2 al 4, antes del 5, pero si toma el 2
# En la izq si considera en numero en la derecha nel
r5 = lista1[2:] #del 2 a que acabe 
r6 = lista1[:5] #del principio al 4 
r7 = lista1[:] #toda la lista 
r8 = lista1[-1][1] #si el ultimo elemento que es el que llama es iterable, es decir una lista, llama el elemento 2 de la lista 

# Las listas no son vectores, no se puede hacer producto punto, si algunas operaciones

q1 = len(lista1) #tamaño de la lista 
r9 = lista1[-1][1] + lista[0] #Suma de dos listas















