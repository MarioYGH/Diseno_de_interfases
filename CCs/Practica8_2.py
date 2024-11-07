# Diseñe una interfaz gráfica que lea la base de datos de pacientes COVID proporcionada en classroom y muestre las densidades de probabilidad asociadas a las 
# posibles respuestas de una característica seleccionada. Las características decada paciente están numeradas en la imagen proporcionada en classroom y dentro 
# de la interfaz, el usuario la podrá seleccionar a través de un panel de radio buttons. Tenga en cuenta que la variable aleatoria x en todos los casos será la edad.

import customtkinter as ctk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from tkinter import filedialog, messagebox
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Configuración básica de la ventana principal
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Análisis de Densidades de Pacientes COVID")
root.geometry("1200x700")

# Variables y opciones para las características
var_caracteristica = ctk.StringVar()
caracteristicas = [
    "DIABETES", "EPOC", "INMUSUPR", "HIPERTENSION",
    "RENAL_CRONICA", "CARDIOVASCULAR", "OBESIDAD",
    "OTRA_COM", "SEXO", "ENTIDAD_NAC", "ENTIDAD_RES", "EDAD"
]

df = None  # Variable para almacenar el DataFrame
canvas = None  # Variable para almacenar el canvas del gráfico

# Función para cargar y mostrar la base de datos
def cargar_base_datos():
    global df
    archivo = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not archivo:
        return

    try:
        df = pd.read_csv(archivo, on_bad_lines='skip')

        # Borrar cualquier widget previo en el frame de la tabla
        for widget in frame_tabla.winfo_children():
            widget.destroy()

        # Crear la tabla
        tabla = ttk.Treeview(frame_tabla, show="headings")
        tabla.pack(fill="both", expand=True)

        # Configurar las columnas de la tabla usando los encabezados del DataFrame
        columnas = list(df.columns)
        tabla["columns"] = columnas

        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, anchor="center")

        # Insertar las primeras 100 filas para previsualización
        for index, row in df.iterrows():
            if index >= 100:  # Limitar a 100 filas para no sobrecargar la interfaz
                break
            tabla.insert("", "end", values=list(row))

        messagebox.showinfo("Éxito", "Datos cargados correctamente y mostrados en la tabla.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar el archivo: {str(e)}")

# Función para graficar la densidad de probabilidad
def graficar_densidad():
    global canvas
    if df is None:
        messagebox.showerror("Error", "Primero debes cargar un archivo CSV.")
        return

    caracteristica = var_caracteristica.get()
    if caracteristica not in df.columns:
        messagebox.showerror("Error", f"La característica '{caracteristica}' no está en los datos.")
        return

    # Filtrar los datos: solo incluir las edades donde la característica es positiva (por ejemplo, 1 para Sí)
    try:
        datos_filtrados = df[df[caracteristica] == 1]['EDAD'].dropna()
        if datos_filtrados.empty:
            messagebox.showwarning("Advertencia", f"No hay datos positivos para '{caracteristica}'.")
            return
    except Exception as e:
        messagebox.showerror("Error", f"Error al filtrar los datos: {str(e)}")
        return

    # Calcular la densidad de probabilidad usando gaussian_kde
    densidad = gaussian_kde(datos_filtrados)
    x_vals = np.linspace(datos_filtrados.min(), datos_filtrados.max(), 100)
    y_vals = densidad(x_vals)

    # Crear la figura de Matplotlib
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.plot(x_vals, y_vals, label=f"Densidad de {caracteristica}")
    ax.set_title(f"Densidad de Probabilidad de la Edad por {caracteristica}")
    ax.set_xlabel("Edad")
    ax.set_ylabel("Densidad de Probabilidad")
    ax.legend()
    ax.grid(visible=True)

    # Borrar el gráfico anterior si existe
    if canvas:
        canvas.get_tk_widget().destroy()

    # Mostrar el gráfico en la interfaz de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

# Crear los componentes de la interfaz
boton_cargar = ctk.CTkButton(root, text="Cargar Archivo CSV", command=cargar_base_datos)
boton_cargar.pack(pady=10)

frame_tabla = ctk.CTkFrame(root)
frame_tabla.pack(fill="both", expand=True, pady=10)

frame_caracteristicas = ctk.CTkFrame(root)
frame_caracteristicas.pack(side="left", padx=20, pady=20)

label_instrucciones = ctk.CTkLabel(frame_caracteristicas, text="Seleccione una característica:")
label_instrucciones.pack()

for caracteristica in caracteristicas:
    radio = ctk.CTkRadioButton(
        frame_caracteristicas, text=caracteristica, variable=var_caracteristica, value=caracteristica
    )
    radio.pack(anchor="w")

# Frame para el gráfico
frame_grafico = ctk.CTkFrame(root, width=500, height=400)
frame_grafico.pack(side="right", padx=20, pady=20, fill="both", expand=True)

# Botón para graficar la densidad
boton_graficar = ctk.CTkButton(root, text="Graficar Densidad", command=graficar_densidad)
boton_graficar.pack(pady=10)

# Iniciar la interfaz
root.mainloop()
