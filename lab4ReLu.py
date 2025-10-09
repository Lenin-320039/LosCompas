import numpy as np
import time 
import random

 
 
#* 3 entradas → 4 salidas
x = np.array([1.0, 0.5, -1.0])  # Vector de entrada (3 valores)
W = np.array([
    [0.5, -0.7, 0.2, -0.3],
    [0.8, 0.1, -0.4,  0.6],
    [-0.9, 0.3, 0.5, -0.2]
])


#* Feedforward (producto punto entrada * pesos)
y = x @ W  # Equivalente a np.dot(x, W)
#*np.dot()

def relu(z):
    return np.maximum(0,z)

activado = relu(y)

#* Mostrar resultados
print("Matriz de pesos (3x4):")
print(W)
print("\nEntrada:")
print(x)
print("\nSalida:")
print(y)
print("\nSalida despues de la activacion (Sigmoid):")
print(activado)