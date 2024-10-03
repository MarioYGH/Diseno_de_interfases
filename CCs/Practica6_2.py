# Diseñe una interfaz gráfica que permita ingresar los siguientes datos usando el objeto indicado en el paréntesis: Nombre (Edit Text), Edad (Edit Numeric), Estado
# de residencia (Drop down), Genero (Radio button), Nivel de estudios (Radio button), y preguntar sí estudia (Check box). El radio button “Nivel de estudios” solo
# debe ser visible si el Check Box está habilitado. Los datos ingresados en cada campo se deben guardar en un archivo TXT ó CSV cuando se presione un botón
# con etiqueta “Crear”. El archivo CSV debe almacenar todos los usuarios que fueron ingresados durante todo el proceso de captura.

import tkinter as tk
from tkinter import ttk # Para menu desplegable
from tkinter import messagebox
import numpy as np
import pandas as pd
import os


root = tk.Tk()
var1 = tk.IntVar()

root.title("Registro")

def guardar():
    nom = entry1.get()
    edad = entry2.get()
    gen = entry3.get()
    etd = entry4.get()
    stud = combo.get()
    
    if not edad.isnumeric():
        messagebox.showerror("Error", "Por favor complete la edad numericamente.")
        return

    lista = np.array([nom, edad, gen, etd, stud])
    columnas = ["Nombre", "Edad", "Genero", "Estado_Residencia", "Estudios"]
    
    archivo_existe = not os.path.isfile("DataBase.csv") # Verifica si el archivo existe
    
    df = pd.DataFrame(columns=columnas )#.reset_index(drop=True)
    df.loc[len(df.index)] = lista # la funcion .loc es un localizador con el que podemos ir a una direccion o asignar un valor
    # Busca la ultima posicion del index, en la primera iteracion es un cero y guarda ahí los datos y va aumentando para que ahora los datos se guarden en la siguiente posición
    df.to_csv("DataBase.csv",mode="a", header=archivo_existe, index=False) # Crea el csv y el index false quita el numero de cada dato, el mode 'a' concatena
    messagebox.showinfo("Éxito", "Datos guardados correctamente.")
    
    Borrar()

def Borrar():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    combo.set(opciones[0])

def hide(): #Dependiendo de las varibales y su valor, voy ocultando y mostrando los labels
    if (var1.get() == 1):
        label5.grid(row=5, column=0, sticky="e", padx=10, pady=10)
        combo.grid(row=5, column=1, padx=10, pady=10)
    else:
        label5.grid_forget()
        combo.grid_forget()

# Nombre
label1 = tk.Label(root, text="Nombre:")
label1.grid(row=0, column=0, sticky="e", padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

# Edad
label2 = tk.Label(root, text="Edad:")
label2.grid(row=1, column=0, sticky="e", padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=0, pady=10)

# Genero
label3 = tk.Label(root, text="Genero:")
label3.grid(row=2, column=0, sticky="e", padx=10, pady=10)
entry3 = tk.Entry(root)
entry3.grid(row=2, column=1, padx=0, pady=10)

# Estado Residencia
label4 = tk.Label(root, text="Estado Residencia:")
label4.grid(row=3, column=0, sticky="e", padx=10, pady=10)
entry4 = tk.Entry(root)
entry4.grid(row=3, column=1, padx=0, pady=10)

# Checkbox
ch1 = tk.Checkbutton(root, text = 'Estudios', variable = var1, onvalue = 1, offvalue = 0, command = hide)
ch1.grid(row = 4, column = 0, padx = 10, pady = 10, columnspan = 2)

# Estudios
label5 = tk.Label(root, text="Estudios:")
opciones = ["---", "Ninguno", "Primaria", "Secundaria", "Preparatoria", "Universidad", "Maestria", "Doctorado"]
state_var = tk.StringVar(value=opciones[0])
combo = ttk.Combobox(root, textvariable=state_var, values=opciones,state='readonly')

# Boton suma
boton = tk.Button(root, text="Guardar", width=10, command=guardar)
boton.grid(row=6, column=0, columnspan=2,  padx=10, pady=10, sticky="n")






root.mainloop()
