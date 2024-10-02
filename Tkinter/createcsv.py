import tkinter as tk
from tkinter import ttk # Para menu desplegable
from tkinter import messagebox
import numpy as np
import pandas as pd
import os


root = tk.Tk()

root.title("Registro")

def guardar():
    nom = entry1.get()
    apell = entry2.get()
    edad = entry3.get()
    stud = combo.get()
    
    if not edad.isnumeric():
        messagebox.showerror("Error", "Por favor complete la edad numericamente.")
        return

    lista = np.array([nom, apell, edad, stud])
    columnas = ["Nombre", "Apellido", "Edad", "Estudios"]
    
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
    combo.set(opciones[0])


# Nombre
label1 = tk.Label(root, text="Nombre:")
label1.grid(row=0, column=0, sticky="e", padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

# Apellido
label2 = tk.Label(root, text="Apellido:")
label2.grid(row=1, column=0, sticky="e", padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=0, pady=10)

# Edad
label3 = tk.Label(root, text="Edad:")
label3.grid(row=2, column=0, sticky="e", padx=10, pady=10)
entry3 = tk.Entry(root)
entry3.grid(row=2, column=1, padx=0, pady=10)

# Estudios
label4 = tk.Label(root, text="Estudios:")
label4.grid(row=3, column=0, sticky="e", padx=10, pady=10)
opciones = ["---", "Ninguno", "Primaria", "Secundaria", "Preparatoria", "Universidad", "Maestria", "Doctorado"]
state_var = tk.StringVar(value=opciones[0])
combo = ttk.Combobox(root, textvariable=state_var, values=opciones,state='readonly')
combo.grid(row=3, column=1, padx=10, pady=10)

# Boton suma
boton = tk.Button(root, text="Guardar", width=10, command=guardar)
boton.grid(row=4, column=0, columnspan=2,  padx=10, pady=10, sticky="n")






root.mainloop()
