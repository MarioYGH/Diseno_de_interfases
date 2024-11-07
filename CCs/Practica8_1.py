# Diseñe una interfaz gráfica que permita recuperar los datos de un archivo CSV o TXT. En particular, integré esta nueva interfaz grafica con la interfaz de la practica
# 6 donde se solicitaban al usuario los siguientes datos Nombre (Edit Text), Edad (Edit Numeric), Estado de residencia (Drop down), Genero (Radio button), Nivel de
# estudios (Radio button), y preguntar sí estudia (Check box). Los datos recuperados del archivo CSV se deben mostrar en una Tabla

import customtkinter as ctk
import pandas as pd
import os
from tkinter import messagebox, filedialog
from tkinter import ttk  # Usamos ttk para la tabla

# Configuración básica de la ventana principal
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Registro y Recuperación de Datos")
root.geometry("600x600")

# Variables para almacenar los valores seleccionados
var_estudios = ctk.IntVar()
var_genero = ctk.StringVar(value="Masculino")
var_estado = ctk.StringVar(value="---")
var_nivel_estudios = ctk.StringVar(value="---")

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
    var_nivel_estudios.set("N/A")
    hide_estudios()

# Mostrar u ocultar el nivel de estudios
def hide_estudios():
    if var_estudios.get() == 1:
        label_estudios.grid(row=6, column=0, padx=10, pady=10)
        combo_estudios.grid(row=6, column=1, padx=10, pady=10)
    else:
        label_estudios.grid_forget()
        combo_estudios.grid_forget()

# Función para cargar datos desde un archivo CSV o TXT y mostrarlos en una tabla
def cargar_datos():
    archivo = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Text files", "*.txt")])
    if not archivo:
        return

    try:
        # Leer el archivo usando la primera fila como encabezado
        if archivo.endswith(".csv"):
            df = pd.read_csv(archivo, on_bad_lines='skip')
        else:
            df = pd.read_csv(archivo, delimiter="\t", on_bad_lines='skip')

        # Borrar cualquier widget previo en el frame de la tabla
        for widget in frame_tabla.winfo_children():
            widget.destroy()

        # Crear la tabla
        tabla = ttk.Treeview(frame_tabla, show="headings")
        tabla.pack(fill="both", expand=True)

        # Configurar las columnas de la tabla usando los encabezados del DataFrame
        columnas = list(df.columns)
        tabla["columns"] = columnas

        # Agregar encabezados a la tabla
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, anchor="center")

        # Insertar las filas en la tabla (sin incluir la fila de encabezados)
        for _, row in df.iterrows():
            tabla.insert("", "end", values=list(row))

        messagebox.showinfo("Éxito", "Datos cargados correctamente.")

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar el archivo: {str(e)}")

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
label_genero = ctk.CTkLabel(root, text="Genero:")
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

# Botón para cargar los datos desde un archivo
boton_cargar = ctk.CTkButton(root, text="Cargar Datos", command=cargar_datos)
boton_cargar.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# Frame para la tabla de datos
frame_tabla = ctk.CTkFrame(root)
frame_tabla.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Configurar la expansión de la tabla
root.grid_rowconfigure(9, weight=1)
root.grid_columnconfigure(1, weight=1)

# Iniciar la interfaz
root.mainloop()
