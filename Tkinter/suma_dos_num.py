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

# Num 1
label1 = tk.Label(miframe, text="Numero 1:")
label1.grid(row=0, column=0, sticky="e", padx=10, pady=10)
entry1 = tk.Entry(miframe)
entry1.grid(row=0, column=1, padx=10, pady=10)

# Num 2
label2 = tk.Label(miframe, text="Numero 2:")
label2.grid(row=1, column=0, sticky="e", padx=10, pady=10)
entry2 = tk.Entry(miframe)
entry2.grid(row=1, column=1, padx=10, pady=10)

def sumar():
    try:
        
        # Obtener los valores de las entradas
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        resultado.set(str(num1+num2))
    
    except ValueError:
        # None
        messagebox.showerror("Error", "Por favor ingresa solo números.")

# Boton suma
boton = tk.Button(miframe, text="Suma", width=10, command=sumar)
boton.grid(row=2,column=1)

# Resultado
label3 = tk.Label(miframe, text="Resultado:")
label3.grid(row=3, column=0, sticky="e", padx=10, pady=10)
entry3 = tk.Entry(miframe, textvariable=resultado, state='readonly')
entry3.grid(row=3, column=1, padx=0, pady=10)



root.mainloop()
