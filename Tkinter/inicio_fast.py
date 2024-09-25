import tkinter as tk

root = tk.Tk() # nuestro objeto/ventana 

root.title("Ventana de pruebas") # para titulo 

root.resizable(True,True) # Para que sea ajustable

#root.iconbitmap("incono.ico") # Para poner el icono que deseamos en la parte superior izq

miframe = tk.Frame(root, width = 1200, height = 600) # Generar un frame dentro de otro frame
miframe.pack() # Empaqueta el frame dentro del root, eso se definio en la linea de arriba
miframe.config(bg = "blue") # background, pero este comando sirve para estilo de la pantalla,
# Tipo de letra, color, estilo, etc

root.mainloop() #bucle infinito 
