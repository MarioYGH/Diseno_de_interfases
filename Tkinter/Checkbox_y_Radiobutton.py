import tkinter as tk

root = tk.Tk()
root.title('My window')
root.resizable(False, False)

# Variables
var1 = tk.IntVar()
var2 = tk.IntVar()
msg1 = tk.StringVar()
msg2 = tk.StringVar()
opcion_fruta = tk.StringVar()
opcion_verdura = tk.StringVar()
f = " "
v = " "

def print_selection(): # Dependiendo del valor de las variables, imprime un msj distinto
    
    if(var1.get() == 1) & (var2.get() == 0):
        msg1.set("Me gustan las frutas")
        vegetal()
        hide()
    elif(var1.get() == 0) & (var2.get() == 1):
        msg1.set("Me gustan las verduras")
        vegetal()
        hide()  
    elif(var1.get() == 0) & (var2.get() == 0):
        msg1.set("Odio los vegetales")
        vegetal()
        hide()  
    else:
        msg1.set("Quiero ambas")
        vegetal()
        hide()
        

def hide(): #Dependiendo de las varibales y su valor, voy ocultando y mostrando los labels
    if (var1.get() == 1) and (var2.get() == 0):
        l3.grid(row=3, column=0, padx=10, pady=10)
        l4.grid_forget()
        r1.grid(row=4, column=0, padx=10, pady=1,sticky="w") # Es importente justificar pq sino se desalinea
        r2.grid(row=5, column=0, padx=10, pady=1,sticky="w")
        r3.grid(row=6, column=0, padx=10, pady=1,sticky="w")
        r4.grid_forget()
        r5.grid_forget()
        r6.grid_forget()
        opcion_verdura.set(" ")
        # opcion()
        
    elif (var1.get() == 0) and (var2.get() == 1):
        l3.grid_forget()
        l4.grid(row=3, column=1, padx=10, pady=10)
        r1.grid_forget()
        r2.grid_forget()
        r3.grid_forget()
        r4.grid(row=4, column=1, padx=10, pady=1,sticky="w")
        r5.grid(row=5, column=1, padx=10, pady=1,sticky="w")
        r6.grid(row=6, column=1, padx=10, pady=1,sticky="w")
        opcion_fruta.set(" ")
        # opcion()

    elif (var1.get() == 0) and (var2.get() == 0):
        l3.grid_forget() # Para quitar o con grid remove
        l4.grid_forget()
        r1.grid_forget()
        r2.grid_forget()
        r3.grid_forget()
        r4.grid_forget()
        r5.grid_forget()
        r6.grid_forget()
        opcion_fruta.set(" ")
        opcion_verdura.set(" ")
        msg2.set(" ")

    else:
        l3.grid(row=3, column=0, padx=10, pady=10)
        l4.grid(row=3, column=1, padx=10, pady=10)
        r1.grid(row=4, column=0, padx=10, pady=1,sticky="w")
        r2.grid(row=5, column=0, padx=10, pady=1,sticky="w")
        r3.grid(row=6, column=0, padx=10, pady=1,sticky="w")
        r4.grid(row=4, column=1, padx=10, pady=1,sticky="w")
        r5.grid(row=5, column=1, padx=10, pady=1,sticky="w")
        r6.grid(row=6, column=1, padx=10, pady=1,sticky="w")
        
def imprimir(): # Para imprir el msj
    if f != " ":
        msg2.set("Me gustan las " + f)
    if v != " ":
        msg2.set("Me gustan las " + v)
    if f != " " and v != " ":
        msg2.set("Me gustan las " + f + " y las " + v)  
    if f == " " and v == " ":
        msg2.set(" ")
        

def vegetal(): # Imprimimos la opcion seleccionada
    global f, v
    f = opcion_fruta.get()
    v = opcion_verdura.get()
    
    if (var1.get() == 1) and (var2.get() == 0):
        imprimir()

        
    elif (var1.get() == 0) and (var2.get() == 1):
        imprimir()


    elif (var1.get() == 0) and (var2.get() == 0):

        msg2.set(" ")
    else:
        imprimir()
        

        # msg2.set("Me gustan las " + f + " y las " + v)

# Etiqueta 1
l1 = tk.Label(root, text = 'Selecciona una opción:')
l1.grid(row = 0, column = 0, padx = 10, pady = 10)

# Checkbox
ch1 = tk.Checkbutton(root, text = 'Frutas', variable = var1, onvalue = 1, offvalue = 0, command = print_selection)
ch1.grid(row = 1, column = 0, padx = 10, pady = 10)
ch1 = tk.Checkbutton(root, text = 'Verdura', variable = var2, onvalue = 1, offvalue = 0, command = print_selection)
ch1.grid(row = 1, column = 1, padx = 10, pady = 10)

# Etiqueta 2
msg1.set(" ")
l2 = tk.Label(root, textvariable = msg1) # No tiene texto, pq el texto va a ser movil
l2.grid(row= 2, column = 0, padx = 10, pady = 10, columnspan = 2) # Columnspan fuciona columnas, también hay rowspan

# Etiqueta 3
l3 = tk.Label(root, text = 'Frura que te gusta más',) 

# Etiqueta 4
l4 = tk.Label(root, text = 'Verdura que te gusta más',) 

# Radiobutton frutas
opcion_fruta.set(" ")
r1 = tk.Radiobutton(root, text = 'Piña', variable = opcion_fruta, value = "Piñas", command = vegetal)
r2 = tk.Radiobutton(root, text = 'Naranja', variable = opcion_fruta, value = "Naranja", command = vegetal)
r3 = tk.Radiobutton(root, text = 'Manzana', variable = opcion_fruta, value = "Manzana", command = vegetal)


# Radiobutton Verduras
opcion_verdura.set(" ")
r4 = tk.Radiobutton(root, text = 'Lechuga', variable = opcion_verdura, value = "Lechuga", command = vegetal)
r5 = tk.Radiobutton(root, text = 'Espinaca', variable = opcion_verdura, value = "Espinaca", command = vegetal)
r6 = tk.Radiobutton(root, text = 'Remolacha', variable = opcion_verdura, value = "Remolacha", command = vegetal)

# Etiqueta 5
msg2.set(" ")
l5 = tk.Label(root, textvariable = msg2)
l5.grid(row = 10, column = 0, padx = 10, pady = 10, columnspan = 2)

root.mainloop()
