import tkinter as tk

# Creación de contenedor principal
root = tk.Tk() # nuestro objeto/ventana 

# Variables
mensaje = tk.StringVar() # Variable vacia de tipo texto de tkinter, un char pues

# Fuhnción mostrar msj
def accion():
    mensaje.set("Hola mundo")

#  Nombre de la ventana del contenedor
root.title("Ventana de pruebas") # para titulo 
root.resizable(True,True) # Para que sea ajustable

# Creación del frame principal
miframe = tk.Frame(root, width = 1200, height = 600) # Generar un frame dentro de otro frame
miframe.pack() # Empaqueta el frame dentro del root, eso se definio en la linea de arriba

# Botón mensaje
boton = tk.Button(miframe, text = "Mensaje", width = 10, command = accion) 
boton.grid(row = 0, column = 0, padx = 50, pady = 10) # pad_x, pad_y mueve en x y y el frame

# Resultado 
label1 = tk.Label(miframe, text = "") # igual así se puede poner texto sin etiquetas
label1.config(textvariable = mensaje)
label1.grid(row = 1, column = 0, sticky = "e", padx = 50, pady = 10) # sticky es posicion, posicion con norte = n, sur = s, este = e, oeste = w

root.mainloop() #bucle infinito 
