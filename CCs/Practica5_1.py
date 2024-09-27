# Diseñe una interfaz grafica de una calculadora que incluya los dígitos del 0 al 9, las operaciones: suma, resta, multiplicación y división, y un botón (AC) para limpiar la
# pantalla y habilite el ingreso de una nueva operación. La calculadora debe permitir el ingreso de “n” operandos.
import tkinter as tk
from tkinter import messagebox

# Creación de contenedor principal
root = tk.Tk()

# Nombre de la ventana del contenedor
root.title("Calculadora")
root.resizable(True, True)

# Creación del frame principal
miframe = tk.Frame(root, padx=20, pady=20)
miframe.pack()

# Variables
resultado = tk.StringVar()

pantalla = ""

def var(j):
    global pantalla
    pantalla += str(j)
    resultado.set(pantalla)

# Pantalla de resultados
entry = tk.Entry(miframe, textvariable=resultado, state='readonly', justify='right', font=("Arial", 16), bd=10, width=20)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Estilo de los botones
button_font = ("Helvetica", 16, "bold")  # Fuente más grande y estilizada

# Num 1
boton1 = tk.Button(miframe, text="1", width=10, height=3, command=lambda: var(1), font=button_font)
boton1.grid(row=1, column=1, padx=5, pady=5)

# Num 2
boton2 = tk.Button(miframe, text="2", width=10, height=3, command=lambda: var(2), font=button_font)
boton2.grid(row=1, column=2, padx=5, pady=5)

# Num 3
boton3 = tk.Button(miframe, text="3", width=10, height=3, command=lambda: var(3), font=button_font)
boton3.grid(row=1, column=3, padx=5, pady=5)

# Num 4
boton4 = tk.Button(miframe, text="4", width=10, height=3, command=lambda: var(4), font=button_font)
boton4.grid(row=2, column=1, padx=5, pady=5)

# Num 5
boton5 = tk.Button(miframe, text="5", width=10, height=3, command=lambda: var(5), font=button_font)
boton5.grid(row=2, column=2, padx=5, pady=5)

# Num 6
boton6 = tk.Button(miframe, text="6", width=10, height=3, command=lambda: var(6), font=button_font)
boton6.grid(row=2, column=3, padx=5, pady=5)

# Num 7
boton7 = tk.Button(miframe, text="7", width=10, height=3, command=lambda: var(7), font=button_font)
boton7.grid(row=3, column=1, padx=5, pady=5)

# Num 8
boton8 = tk.Button(miframe, text="8", width=10, height=3, command=lambda: var(8), font=button_font)
boton8.grid(row=3, column=2, padx=5, pady=5)

# Num 9
boton9 = tk.Button(miframe, text="9", width=10, height=3, command=lambda: var(9), font=button_font)
boton9.grid(row=3, column=3, padx=5, pady=5)

# Botón de operación
def operacion():
    global pantalla
    if len(pantalla) > 10000:
       return messagebox.showerror("Error", "Por favor ingresa solo números.")
    try:
        r = eval(pantalla)
        r = str(r)
        resultado.set(r)
        pantalla = ""

    except ValueError:
        return messagebox.showerror("Error", "Por favor ingresa solo números.")

    except SyntaxError:
        return messagebox.showerror("Error", "Por favor ingresa una operación válida.")
    return

# Botón para borrar
def borrar():
    global pantalla
    pantalla = ""
    resultado.set(pantalla)

# Botones de operaciones
boton_suma = tk.Button(miframe, text="+", width=10, height=3, command=lambda: var("+"), font=button_font)
boton_suma.grid(row=4, column=1, padx=5, pady=5)

boton_resta = tk.Button(miframe, text="-", width=10, height=3, command=lambda: var("-"), font=button_font)
boton_resta.grid(row=4, column=2, padx=5, pady=5)

boton_multiplicacion = tk.Button(miframe, text="*", width=10, height=3, command=lambda: var("*"), font=button_font)
boton_multiplicacion.grid(row=4, column=3, padx=5, pady=5)

boton_division = tk.Button(miframe, text="/", width=10, height=3, command=lambda: var("/"), font=button_font)
boton_division.grid(row=3, column=4, padx=5, pady=5)

# Botón igual
boton_igual = tk.Button(miframe, text="=", width=10, height=3, command=operacion, font=button_font)
boton_igual.grid(row=4, column=4, padx=5, pady=5)

# Botón borrar
boton_borrar = tk.Button(miframe, text="C", width=10, height=3, command=borrar, font=button_font)
boton_borrar.grid(row=5, column=4, padx=5, pady=5)

# Botón cero
boton_cero = tk.Button(miframe, text="0", width=10, height=3, command=lambda: var(0), font=button_font)
boton_cero.grid(row=5, column=2, padx=5, pady=5)

root.mainloop()
