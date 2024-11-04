# Diseñe una interfaz gráfica que permita ingresar los siguientes datos usando el objeto indicado en el paréntesis: Nombre (Edit Text), Edad (Edit Numeric), Estado
# de residencia (Drop down), Genero (Radio button), Nivel de estudios (Radio button), y preguntar sí estudia (Check box). El radio button “Nivel de estudios” solo
# debe ser visible si el Check Box está habilitado. Los datos ingresados en cada campo se deben guardar en un archivo TXT ó CSV cuando se presione un botón
# con etiqueta “Crear”. El archivo CSV debe almacenar todos los usuarios que fueron ingresados durante todo el proceso de captura.

import customtkinter as ctk  # Usamos customtkinter en lugar de tkinter
import pandas as pd
import os
import numpy as np
from tkinter import messagebox

# Configuración básica de la ventana principal
ctk.set_appearance_mode("System")  # Opciones: "System", "Light", "Dark"
ctk.set_default_color_theme("blue")  # Puedes cambiar el color: "blue", "green", "dark-blue"

root = ctk.CTk()  # Inicializa la ventana principal
root.title("Registro")
root.geometry("400x500")

# Variables para almacenar los valores seleccionados
var_estudios = ctk.IntVar()
var_genero = ctk.StringVar(value="Masculino")
var_estado = ctk.StringVar(value="---")
var_nivel_estudios = ctk.StringVar(value="---")  # Nueva variable para el nivel de estudios

# Función para guardar los datos en un archivo CSV
def guardar():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    genero = var_genero.get()
    estado_residencia = combo_estado.get()

    # Manejar el nivel de estudios solo si el checkbox de estudios está activado
    nivel_estudios = combo_estudios.get() if var_estudios.get() == 1 else "N/A"

    if not edad.isnumeric():
        messagebox.showerror("Error", "Por favor ingresa la edad como un número.")
        return

    lista = [nombre, edad, genero, estado_residencia, nivel_estudios]
    columnas = ["Nombre", "Edad", "Género", "Estado de Residencia", "Nivel de Estudios"]
    
    archivo_existe = not os.path.isfile("DataBase.csv")

    df = pd.DataFrame([lista], columns=columnas)
    df.to_csv("DataBase.csv", mode="a", header=archivo_existe, index=False)
    
    messagebox.showinfo("Éxito", "Datos guardados correctamente.")
    borrar()

# Función para borrar los campos de entrada
def borrar():
    entry_nombre.delete(0, ctk.END)
    entry_edad.delete(0, ctk.END)
    var_genero.set("Masculino")
    combo_estado.set(opciones_estados[0])
    var_estudios.set(0)
    var_nivel_estudios.set("N/A")  # Resetear nivel de estudios
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
label_nombre = ctk.CTkLabel(root, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=10, pady=10)
entry_nombre = ctk.CTkEntry(root)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

# Edad
label_edad = ctk.CTkLabel(root, text="Edad:")
label_edad.grid(row=1, column=0, padx=10, pady=10)
entry_edad = ctk.CTkEntry(root)
entry_edad.grid(row=1, column=1, padx=10, pady=10)

# Género (Radio Buttons)
label_genero = ctk.CTkLabel(root, text="Género:")
label_genero.grid(row=2, column=0, padx=10, pady=10)

radio_masculino = ctk.CTkRadioButton(root, text="Masculino", variable=var_genero, value="Masculino")
radio_masculino.grid(row=2, column=1, sticky="w")

radio_femenino = ctk.CTkRadioButton(root, text="Femenino", variable=var_genero, value="Femenino")
radio_femenino.grid(row=3, column=1, sticky="w")

radio_otro = ctk.CTkRadioButton(root, text="Otro", variable=var_genero, value="Otro")
radio_otro.grid(row=4, column=1, sticky="w")

# Estado de residencia (Drop down)
label_estado = ctk.CTkLabel(root, text="Estado de Residencia:")
label_estado.grid(row=5, column=0, padx=10, pady=10)

opciones_estados = ["---", "CDMX", "Jalisco", "Nuevo Leon", "Puebla", "Guanajuato", "Veracruz", "Yucatan", "Chiapas", "Sonora", "Queretaro"]
combo_estado = ctk.CTkComboBox(root, values=opciones_estados)
combo_estado.grid(row=5, column=1, padx=10, pady=10)
combo_estado.set(opciones_estados[0])

# Checkbox para "Estudios"
check_estudios = ctk.CTkCheckBox(root, text="¿Estudia?", variable=var_estudios, command=hide_estudios)
check_estudios.grid(row=6, column=0, padx=10, pady=10)

# Nivel de estudios (Drop down)
label_estudios = ctk.CTkLabel(root, text="Nivel de Estudios:")
opciones_estudios = ["---", "Ninguno", "Primaria", "Secundaria", "Preparatoria", "Universidad", "Maestria", "Doctorado"]
combo_estudios = ctk.CTkComboBox(root, values=opciones_estudios)

# Botón para guardar los datos
boton_guardar = ctk.CTkButton(root, text="Guardar", command=guardar)
boton_guardar.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Iniciar la interfaz
root.mainloop()
