#Los operadores de comparación son: ==, !=, <,>, >=, <=
a1 = 3 == 3
a2 = 3 != 4

a3 = ('puerta'=='puerta')

#Operadores not, or, and

#Los operadores de membresia, estos son in, not in

resultado = 'a' in 'hola' #>>True

resultado = 'a' not in 'hola' #>>False

# %%Conversion de variables 
# int() - Convierte lo que se le pase a int
# float() - Convierte lo que se le pase a float
# str() - Convierte lo que se le pase a str
# bool() - Convierte lo que se le pase a bool

a1 = 3 
a2 = float(a1)
a3 = str(a2)
a4 = "3.1416"
a5 = float(a4) 
#No funciona con palabras 

print("El numeor es", a1, "y es un numero entero")
print("El numero es " + a4) #solo se puede pq a4 es un str
print("El numero es " + str(a1)) #aca se debe de convertir primero pq es entero, esto por el +
print("El numeor es {a4} y es caracter") #Aca no le importa el tipo de variable que se
print("El numeor es {a1} y es caracter") #Con el + si pq suma dos tipos de variables

a6 = 0
a7 = bool(a6)

# %%Estructura de control de flujo 
c=100
d=100

if c <= d:
    print('El numero a es menor que', d)
if (c == d):
    print("el numero a es igual a", d)
else:
    print("el numero a es mayor que", d)
    
# %%
a = int(input("ingresa tu edad: "))
b = str(input("Eres estudiante? Si/no: "))

if(a<18 and b=='Si'):
    print("beca chida")
if(a<18 and b!='Si'):
    print("media beca")
elif(a>18 and b=='Si'):
    print("media beca")
else:
    print("nadota")

# %%
for i in range(2,11,2): #donde inicia, restriccion, paso
    print(i)
# %%
i = 0
while i < 10:
    i = i + 2 #i += 2
    print(i)
    
# %%
mi_lista = ['Juan','Antonio','Pedro','Mario']
for nombre in mi_lista:
    print(nombre)
    
mi_lista = ['Juan','Antonio','Pedro','Mario']
for i in range(len(mi_lista)):
    print(mi_lista[i])
    
#Guardar cosas en una lista 
lista2 = []
for i in range(20):
    lista2.append(i)
print(lista2)
    





