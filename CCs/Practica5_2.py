import tkinter as tk
from tkinter import messagebox

# Creacion de contenedor principal
root = tk.Tk()

# Nombre de la ventana del contenedor
root.title("Ventana de prueba")
root.resizable(True,True)

# Creacion del frame principal
miframe = tk.Frame(root, width=1200,height=600)
miframe.pack()

# Variables
resultado = tk.StringVar()
corriente = tk.StringVar()
voltage = tk.StringVar()
voltageind = tk.StringVar()
corrienteind = tk.StringVar()
resistencia_seleccionada = tk.StringVar(value="R1") 

# Resistencia 1
label1 = tk.Label(miframe, text="Resistencia 1:")
label1.grid(row=0, column=0, sticky="e", padx=10, pady=10)
entry1 = tk.Entry(miframe)
entry1.grid(row=0, column=1, padx=10, pady=10)

# Resistencia 2
label2 = tk.Label(miframe, text="Resistencia 2:")
label2.grid(row=1, column=0, sticky="e", padx=10, pady=10)
entry2 = tk.Entry(miframe)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Resistencia 3
label3 = tk.Label(miframe, text="Resistencia 3:")
label3.grid(row=2, column=0, sticky="e", padx=10, pady=10)
entry3 = tk.Entry(miframe)
entry3.grid(row=2, column=1, padx=10, pady=10)

# Resistencia 4
label4 = tk.Label(miframe, text="Resistencia 4:")
label4.grid(row=3, column=0, sticky="e", padx=10, pady=10)
entry4 = tk.Entry(miframe)
entry4.grid(row=3, column=1, padx=10, pady=10)

# Resistencia 5
label5 = tk.Label(miframe, text="Resistencia 5:")
label5.grid(row=4, column=0, sticky="e", padx=10, pady=10)
entry5 = tk.Entry(miframe)
entry5.grid(row=4, column=1, padx=10, pady=10)

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
        # None
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
        # None
        messagebox.showerror("Error", "Por favor ingresa solo números.")

# Boton Serie
boton = tk.Button(miframe, text="Serie", width=10, command=sumarserie)
boton.grid(row=5,column=1)

# Boton Paralelo
boton = tk.Button(miframe, text="Paralelo", width=10, command=sumarparalelo)
boton.grid(row=5,column=2)

# # Boton Resistencia
# boton = tk.Button(miframe, text="Resistencia", width=10, command=sumarserie)
# boton.grid(row=5,column=0)

# # Menú desplegable para seleccionar la resistencia para Ley de Ohm
# etiqueta_seleccion = tk.Label(miframe, text="Resistencia:")
# etiqueta_seleccion.grid(row=5, column=0, padx=10, pady=10)

opciones_resistencias = ["R1", "R2", "R3", "R4", "R5"]
menu_resistencias = tk.OptionMenu(miframe, resistencia_seleccionada, *opciones_resistencias)
menu_resistencias.grid(row=5, column=0, padx=10, pady=10)

# Resistencia Total
label6 = tk.Label(miframe, text="Resistencia Total:")
label6.grid(row=6, column=0, sticky="e", padx=10, pady=10)
entry6 = tk.Entry(miframe, textvariable=resultado, state='readonly')
entry6.grid(row=6, column=1, padx=0, pady=10)

# Voltaje Total
label7 = tk.Label(miframe, text="Voltaje Total:")
label7.grid(row=7, column=0, sticky="e", padx=10, pady=10)
entry7 = tk.Entry(miframe, textvariable=voltage, state='readonly')
entry7.grid(row=7, column=1, padx=0, pady=10)

# Corriente Total
label8 = tk.Label(miframe, text="Corriente Total:")
label8.grid(row=8, column=0, sticky="e", padx=10, pady=10)
entry8 = tk.Entry(miframe, textvariable=corriente, state='readonly')
entry8.grid(row=8, column=1, padx=0, pady=10)

# Voltaje
label7 = tk.Label(miframe, text="Voltaje:")
label7.grid(row=9, column=0, sticky="e", padx=10, pady=10)
entry7 = tk.Entry(miframe, textvariable=voltageind, state='readonly')
entry7.grid(row=9, column=1, padx=0, pady=10)

# Corriente
label8 = tk.Label(miframe, text="Corriente:")
label8.grid(row=10, column=0, sticky="e", padx=10, pady=10)
entry8 = tk.Entry(miframe, textvariable=corrienteind, state='readonly')
entry8.grid(row=10, column=1, padx=0, pady=10)



root.mainloop()
