#Implementar un programa de redes neuronales el cual contenga lo siguiente: 
# 3 Vectores de entrada con 3 valores cada uno.
# 1 Matriz De Pesos con 3 Valores Para Cada Vector.
# 3 Valores De Bias (Sesgo) Para Cada Vector.
# Obtener la representación del programa en razón de la expresión matricial es decir: R1→R1→R1→R1 por ejemplo.
# Obtener la representación utilizando NN-SVG y TensorFlowPlayGround.
# Para "las 2 capas ocultas" tienen libertad de implementación de funciones de activación (siempre y cuando cumpla con la arquitectura esperada del programa".

import numpy as np

#Enntradas

x = np.array([ [1, -2, 0.6], 
               [-1, 0.5, 1.5], 
               [-3, -0.5, 1]
])

#Pesos
w = np.array([
    [0.5, -0.7, 0.2],
    [0.8, 0.1, -0.4],
    [-0.9, 0.3, 0.5]
])
#Bias
b = np.array([1, 0.5, -1])

#Funcion sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# 1er capa oculta 

suma_capa1 = np.dot(x, w) + b
capa1 = np.tanh(suma_capa1)
print("La salida de la primer capa oculta (Tanh) es: \n", capa1)

#2da capa oculta

w1 = np.array([0.5, -2, 1])
b1 = np.array([0.7])

suma_capa2 = np.dot(capa1 , w1) + b1
capa2 = sigmoid(suma_capa2)

print("\nLa salida de la segunda capa oculta (Sigmoid) es: \n", capa2)

#Salida

w2 = np.array([0.9])  
b2 = 0.1

salida = (capa2 * w2) + b2
print("\nLa salida es: ", salida)

#todo bien hecho como debe ser
