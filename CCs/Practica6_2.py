# Diseñe una interfaz gráfica que permita ingresar los siguientes datos usando el objeto indicado en el paréntesis: Nombre (Edit Text), Edad (Edit Numeric), Estado
# de residencia (Drop down), Genero (Radio button), Nivel de estudios (Radio button), y preguntar sí estudia (Check box). El radio button “Nivel de estudios” solo
# debe ser visible si el Check Box está habilitado. Los datos ingresados en cada campo se deben guardar en un archivo TXT ó CSV cuando se presione un botón
# con etiqueta “Crear”. El archivo CSV debe almacenar todos los usuarios que fueron ingresados durante todo el proceso de captura.

import tkinter as tk
from tkinter import ttk  # Para el menú desplegable
from tkinter import messagebox
import numpy as np
import pandas as pd
import os

root = tk.Tk()
root.title("Registro")

# Variables para almacenar los valores seleccionados
var_estudios = tk.IntVar()
var_genero = tk.StringVar(value="Masculino")
var_estado = tk.StringVar(value="---")

# Función para guardar los datos en un archivo CSV
def guardar():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    genero = var_genero.get()
    estado_residencia = combo_estado.get()
    estudia = var_estudios.get()

    if not edad.isnumeric():
        messagebox.showerror("Error", "Por favor ingresa la edad como un número.")
        return

    lista = [nombre, edad, genero, estado_residencia, "Sí" if estudia else "No"]
    columnas = ["Nombre", "Edad", "Género", "Estado de Residencia", "Estudia"]
    
    archivo_existe = not os.path.isfile("DataBase.csv")

    df = pd.DataFrame([lista], columns=columnas)
    df.to_csv("DataBase.csv", mode="a", header=archivo_existe, index=False)
    
    messagebox.showinfo("Éxito", "Datos guardados correctamente.")
    borrar()

# Función para borrar los campos de entrada
def borrar():
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    var_genero.set("Masculino")
    combo_estado.set(opciones_estados[0])
    var_estudios.set(0)
    hide_estudios()

# Mostrar u ocultar el nivel de estudios
def hide_estudios():
    if var_estudios.get() == 1:
        label_estudios.grid(row=6, column=0, padx=10, pady=10)
        combo_estudios.grid(row=6, column=1, padx=10, pady=10)
    else:
        label_estudios.grid_forget()
        combo_estudios.grid_forget()

# Componentes de la interfaz gráfica

# Nombre
label_nombre = tk.Label(root, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=10, pady=10)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

# Edad
label_edad = tk.Label(root, text="Edad:")
label_edad.grid(row=1, column=0, padx=10, pady=10)
entry_edad = tk.Entry(root)
entry_edad.grid(row=1, column=1, padx=10, pady=10)

# Género (Radio Buttons)
label_genero = tk.Label(root, text="Género:")
label_genero.grid(row=2, column=0, padx=10, pady=10)

radio_masculino = tk.Radiobutton(root, text="Masculino", variable=var_genero, value="Masculino")
radio_masculino.grid(row=2, column=1, sticky="w")

radio_femenino = tk.Radiobutton(root, text="Femenino", variable=var_genero, value="Femenino")
radio_femenino.grid(row=3, column=1, sticky="w")

radio_otro = tk.Radiobutton(root, text="Otro", variable=var_genero, value="Otro")
radio_otro.grid(row=4, column=1, sticky="w")

# Estado de residencia (Drop down)
label_estado = tk.Label(root, text="Estado de Residencia:")
label_estado.grid(row=5, column=0, padx=10, pady=10)

opciones_estados = ["---", "CDMX", "Jalisco", "Nuevo León", "Puebla", "Guanajuato", "Veracruz", "Yucatán", "Chiapas", "Sonora", "Querétaro"]
combo_estado = ttk.Combobox(root, textvariable=var_estado, values=opciones_estados, state="readonly")
combo_estado.grid(row=5, column=1, padx=10, pady=10)
combo_estado.set(opciones_estados[0])

# Checkbox para "Estudia"
check_estudios = tk.Checkbutton(root, text="¿Estudia?", variable=var_estudios, onvalue=1, offvalue=0, command=hide_estudios)
check_estudios.grid(row=6, column=0, padx=10, pady=10)

# Nivel de estudios (Drop down)
label_estudios = tk.Label(root, text="Nivel de Estudios:")
opciones_estudios = ["---", "Ninguno", "Primaria", "Secundaria", "Preparatoria", "Universidad", "Maestría", "Doctorado"]
combo_estudios = ttk.Combobox(root, values=opciones_estudios, state="readonly")

# Botón para guardar los datos
boton_guardar = tk.Button(root, text="Guardar", command=guardar)
boton_guardar.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Iniciar la interfaz
root.mainloop()






root.mainloop()
