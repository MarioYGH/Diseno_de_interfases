import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

# Lectura de archivo .csv 
data = pd.read_csv("espectro.csv")

# Columna x
x_vals = data["x"]

# Columna y
y_vals = data["y"]

# %% Plotting

#Tamaño de letra del plot
tamaño = 14
plt.rcParams.update({'font.size':tamaño})

#Tamaño de figura e indezado de figuras
plt.figure(1,figsize=(10,7)) #El 1 es el numero de figura 

# Curva de ajuste en linea solida 
plt.plot(x_vals, y_vals, linewidth = 1, solid_capstyle="round", linestyle="solid",color="red",alpha=1.0)
#solid_capstyle "round" redondea los bordes de la funcion, tambien sirve para unir funciones 
#alpha transparencia de la funcion 

#Etiquetado
plt.title("Row Spectra")
plt.xlabel("energy [eV]")
plt.ylabel("Intensity [a.u.]")
plt.legend("data")

plt.xlim(min(x_vals), max(x_vals))
plt.ylim(0.95*min(y_vals),1.1*max(y_vals))

# Guardar imagen en buena calidad (Se guarda donde este gurdado el script)
plt.savefig("Spectra raw.png", format="png", dpi=600, bbox_inches="tight")
#dpi = dot for inches, bbox_inches quita un marco feo 





