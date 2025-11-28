import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

#Cargar los datos de pandas
data = pd.read_csv("personas.csv") #columnas: Nombre, Edad
print("Datos originales: \n", data)

#Normalizar edades (usando Numpy)
max_edad = np.max(data["Edad"])
data["Edad_Normalizada"] = data["Edad"] / max_edad

print("\nDatos normalizados:\n", data)

#Graficar edades originales y normalizadas
plt.plot(data["Nombre"], data["Edad"] , label="Edad real", marker = "o")
plt.plot(data["Nombre"], data["Edad_Normalizada"] * max_edad, label="Edad Normalizada * max", marker="x")
plt.title("Comparacion entre Edad real y normalizada")
plt.xlabel("Nombre")
plt.ylabel("Edad")
plt.legend()
plt.grid(True)
plt.show()