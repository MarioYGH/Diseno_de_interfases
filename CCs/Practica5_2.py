# Diseñe una interfaz gráfica que permita calcular la resistencia total, la corriente y el voltaje de un circuito compuesto por cinco resistores. La interfaz debe contener 6
# objetos para ingresar datos (Ustedes eligen que tipo de Edit Field usarán), cinco para ingresar el valor de resistor, y uno para elegir el resistor donde se calculará la
# corriente y el voltaje. Asimismo, la interfaz debe contener tres objetos para mostrar los resultados de la resistencia total, la corriente y el voltaje. A través de dos botones
# el usuario podrá seleccionar si la configuración de los resistores es serie o paralelo. Para el caso serie considere que hay una fuente de voltaje de 5V alimentando el
# circuito, y para el caso paralelo, una fuente de corriente de 2 A. Los resultados para ambas configuraciones tienen que mostrarse en los mismos objetos de visualización.

import tkinter as tk
from tkinter import messagebox

# Creacion de contenedor principal
root = tk.Tk()

# Nombre de la ventana del contenedor
root.title("Cálculo de Circuitos - Serie y Paralelo")
root.resizable(False, False)

# Creacion del frame principal
miframe = tk.Frame(root, padx=20, pady=20)
miframe.pack()

# Variables
resultado = tk.StringVar()
corriente = tk.StringVar()
voltage = tk.StringVar()
voltageind = tk.StringVar()
corrienteind = tk.StringVar()
resistencia_seleccionada = tk.StringVar(value="R1") 

# Estilos comunes
label_font = ("Arial", 12)
entry_font = ("Arial", 12)

# Resistencia 1
label1 = tk.Label(miframe, text="Resistencia 1:", font=label_font)
label1.grid(row=0, column=0, sticky="e", padx=10, pady=10)
entry1 = tk.Entry(miframe, font=entry_font)
entry1.grid(row=0, column=1, padx=10, pady=10, ipady=5)

# Resistencia 2
label2 = tk.Label(miframe, text="Resistencia 2:", font=label_font)
label2.grid(row=1, column=0, sticky="e", padx=10, pady=10)
entry2 = tk.Entry(miframe, font=entry_font)
entry2.grid(row=1, column=1, padx=10, pady=10, ipady=5)

# Resistencia 3
label3 = tk.Label(miframe, text="Resistencia 3:", font=label_font)
label3.grid(row=2, column=0, sticky="e", padx=10, pady=10)
entry3 = tk.Entry(miframe, font=entry_font)
entry3.grid(row=2, column=1, padx=10, pady=10, ipady=5)

# Resistencia 4
label4 = tk.Label(miframe, text="Resistencia 4:", font=label_font)
label4.grid(row=3, column=0, sticky="e", padx=10, pady=10)
entry4 = tk.Entry(miframe, font=entry_font)
entry4.grid(row=3, column=1, padx=10, pady=10, ipady=5)

# Resistencia 5
label5 = tk.Label(miframe, text="Resistencia 5:", font=label_font)
label5.grid(row=4, column=0, sticky="e", padx=10, pady=10)
entry5 = tk.Entry(miframe, font=entry_font)
entry5.grid(row=4, column=1, padx=10, pady=10, ipady=5)

def sumarserie():
    try:
        # Obtener los valores de las entradas
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        num4 = float(entry4.get())
        num5 = float(entry5.get())
        r = num1+num2+num3+num4+num5
        resultado.set(str(r))
        A = 5/r
        corriente.set(str(A))
        voltage.set(str(A*r))
        
        if resistencia_seleccionada.get() == "R1":
            voltaje = A * num1
            c = voltaje/num1
        elif resistencia_seleccionada.get() == "R2":
            voltaje = A * num2
            c = voltaje/num2
        elif resistencia_seleccionada.get() == "R3":
            voltaje = A * num3
            c = voltaje/num3
        elif resistencia_seleccionada.get() == "R4":
            voltaje = A * num4
            c = voltaje/num4
        elif resistencia_seleccionada.get() == "R5":
            voltaje = A * num5
            c = voltaje/num5
            
        voltageind.set(str(voltaje))
        corrienteind.set(str(c))
    
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa solo números.")
        
def sumarparalelo():
    try:
        # Obtener los valores de las entradas
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        num4 = float(entry4.get())
        num5 = float(entry5.get())
        r = (1/((1/num1)+(1/num2)+(1/num3)+(1/num4)+(1/num5)))
        resultado.set(str(r))
        V = r*2
        voltage.set(str(V))
        corriente.set(str(V/r))
        
        if resistencia_seleccionada.get() == "R1":
            c = V / num1
            voltaje = c*num1
        elif resistencia_seleccionada.get() == "R2":
            c = V / num2
            voltaje = c*num2
        elif resistencia_seleccionada.get() == "R3":
            c = V / num3
            voltaje = c*num3
        elif resistencia_seleccionada.get() == "R4":
            c = V / num4
            voltaje = c*num4
        elif resistencia_seleccionada.get() == "R5":
            c = V / num5
            voltaje = c*num5
            
        voltageind.set(str(voltaje))
        corrienteind.set(str(c))
        
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa solo números.")

# Menú desplegable para seleccionar la resistencia
tk.Label(miframe, text="Seleccionar Resistencia:", font=label_font).grid(row=5, column=0, padx=10, pady=10)
opciones_resistencias = ["R1", "R2", "R3", "R4", "R5"]
menu_resistencias = tk.OptionMenu(miframe, resistencia_seleccionada, *opciones_resistencias)
menu_resistencias.grid(row=5, column=1, padx=10, pady=10)

# Boton Serie
boton = tk.Button(miframe, text="Serie", width=10, font=entry_font, command=sumarserie)
boton.grid(row=6, column=1, pady=10, padx=10)

# Boton Paralelo
boton = tk.Button(miframe, text="Paralelo", width=10, font=entry_font, command=sumarparalelo)
boton.grid(row=6, column=2, pady=10, padx=10)

# Resistencia Total
label6 = tk.Label(miframe, text="Resistencia Total:", font=label_font)
label6.grid(row=7, column=0, sticky="e", padx=10, pady=10)
entry6 = tk.Entry(miframe, textvariable=resultado, font=entry_font, state='readonly')
entry6.grid(row=7, column=1, padx=10, pady=10)

# Voltaje Total
label7 = tk.Label(miframe, text="Voltaje Total:", font=label_font)
label7.grid(row=8, column=0, sticky="e", padx=10, pady=10)
entry7 = tk.Entry(miframe, textvariable=voltage, font=entry_font, state='readonly')
entry7.grid(row=8, column=1, padx=10, pady=10)

# Corriente Total
label8 = tk.Label(miframe, text="Corriente Total:", font=label_font)
label8.grid(row=9, column=0, sticky="e", padx=10, pady=10)
entry8 = tk.Entry(miframe, textvariable=corriente, font=entry_font, state='readonly')
entry8.grid(row=9, column=1, padx=10, pady=10)

# Voltaje Individual
label9 = tk.Label(miframe, text="Voltaje:", font=label_font)
label9.grid(row=10, column=0, sticky="e", padx=10, pady=10)
entry9 = tk.Entry(miframe, textvariable=voltageind, font=entry_font, state='readonly')
entry9.grid(row=10, column=1, padx=10, pady=10)

# Corriente Individual
label10 = tk.Label(miframe, text="Corriente:", font=label_font)
label10.grid(row=11, column=0, sticky="e", padx=10, pady=10)
entry10 = tk.Entry(miframe, textvariable=corrienteind, font=entry_font, state='readonly')
entry10.grid(row=11, column=1, padx=10, pady=10)

root.mainloop()

