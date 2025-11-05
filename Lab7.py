import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

# 2 entradas y 2 pesos correspondientes a la neurona 1 de la capa oculta
x1 = tf.constant([[1., -1.]])       
w1 = tf.constant([[-0.5], [2.0]])   
b1 = 0.8

# 2 entradas y 2 pesos correspondientes a la neurona 2 de la capa oculta
x2 = tf.constant([[-0.7, 2.0]])     
w2 = tf.constant([[-0.5], [0.4]])   
b2 = -0.2

# Neurona 1: activación Sigmoid
z1 = tf.tensordot(x1, w1, axes=1) + b1
h1 = tf.nn.sigmoid(z1)

# Neurona 2: activación ReLU
z2 = tf.tensordot(x2, w2, axes=[[1],[0]]) + b2
h2 = tf.nn.relu(z2)

# Combinación de las salidas
wS = tf.constant([[1.1], [-0.7]])   
bS = 0.1

concat = tf.concat([h1, h2], axis=1)

# Salida final (tanh)
c = tf.tensordot(concat, wS, axes=[[1],[0]]) + bS
y = tf.nn.tanh(c)

print("\nSalida de la neurona 1 (Sigmoid): \n", h1)
print("\nSalida de la neurona 2 (ReLU): \n", h2)
print("\nSalida final (Tanh): \n", y)

print("--- Ahora, la parte gráfica de la tarea ---")

# Creamos un rango de entradas (eje X) de -10 a 10
x_range = np.linspace(-10, 10, 100) # 100 puntos entre -10 y 10
x_tensor = tf.constant(x_range, dtype=tf.float32) # Convertimos a Tensor

#Calculamos la salida de cada función de activación para ese rango
y_sigmoid = tf.nn.sigmoid(x_tensor)
y_tanh = tf.nn.tanh(x_tensor)
y_relu = tf.nn.relu(x_tensor)

#Graficamos los resultados con Matplotlib
plt.figure(figsize=(10, 6))

# Dibujar cada curva
plt.plot(x_range, y_sigmoid, label='Sigmoid')
plt.plot(x_range, y_tanh, label='Tanh')
plt.plot(x_range, y_relu, label='ReLU')

#Añadir títulos y ayudas visuales
plt.title('Comportamiento de Funciones de Activación')
plt.xlabel('Valor de entrada (z)')
plt.ylabel('Valor de activación')
plt.legend() # Muestra las etiquetas (labels)
plt.grid(True) # Pone una cuadrícula
plt.ylim(-1.5, 2.5) # Ajusta los límites del eje Y para que se vea bien
plt.axhline(0, color='black', linewidth=0.5) # Dibuja el eje X
plt.axvline(0, color='black', linewidth=0.5) # Dibuja el eje Y

#Mostrar la gráfica
plt.show()


