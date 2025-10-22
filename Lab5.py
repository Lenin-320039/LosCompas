#Laboratorio 5, en este programa activaremos las funciones de Tanh, ReLu o Sigmoid dependiento de lo que elija el usuario
import time
import numpy as np
import math
import matplotlib.pyplot as plt

opcion = int(input("Elige una opción, Sigmoid (1), ReLu (2) o Tanh (3): "))

match opcion:
    case 1:
        print("\n""Elegiste la funcion de activacion Sigmoid:")
        #Empieza funcion de activacion Sigmoid
        rng = np.random.default_rng(42)  
         
        #* 3 entradas → 4 salidas
        W = rng.random((3, 4))   # Matriz de pesos 3x4
        x = np.array([1.0, 0.5, -1.0])  # Vector de entrada (3 valores)
        
        
        #* Feedforward (producto punto entrada * pesos)
        y = x @ W  # Equivalente a np.dot(x, W)
        #*np.dot()
        
        def sigmoid(z):
            return 1 / (1 + np.exp(-z))
        
        activado = sigmoid(y)
        
        #* Mostrar resultados
        print("\n""Matriz de pesos (3x4):")
        print(W)
        print("\nEntrada:")
        print(x)
        print("\nSalida:")
        print(y)
        print("\nSalida despues de la activacion (Sigmoid):")
        print(activado, "\n")

        x = np.linspace(-5, 5, 100)
        y = sigmoid(x)
        plt.plot(x, y)
        plt.title("Funcion de activacion Sigmoid")
        plt.xlabel("Entrada")
        plt.ylabel("Salida Sigmoid(x)")
        plt.grid(True)
        plt.show()

        
        
    case 2:
        print("\n""Elegiste la funcion de activacion ReLu:")
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
        print("\n""Matriz de pesos (3x4):")
        print(W)
        print("\nEntrada:")
        print(x)
        print("\nSalida:")
        print(y)
        print("\nSalida despues de la activacion (ReLu):")
        print(activado, "\n")

        x = np.linspace(-5, 5, 100)
        y = relu(x)
        plt.plot(x, y)
        plt.title("Funcion de activacion ReLu")
        plt.xlabel("Entrada")
        plt.ylabel("Salida ReLu(x)")
        plt.grid(True)
        plt.show()

    case 3:
        print("\n""Elegiste la funcion de activacion Tanh:")
        #entradas de la funcion de mi neurona:

        inputs = np.array([-100.0, 2.0, -3.0])
        
        #todo: assign weigh for each one input:
        
        weights = np.array([0.2, 0.5, 0.3])
        
        #bias(ajustar el valor de la salida)
        bias = 0.4
        
        #Suma ponderada
        suma_ponderada = np.dot(inputs, weights) + bias
        print("\n""Suma ponderada: ", suma_ponderada)
        
        output = np.tanh(suma_ponderada)
        print("Salida activada (tanh):", output, "\n")

        x = np.linspace(-5, 5, 100)
        y = np.tanh(x)
        plt.plot(x, y)
        plt.title("Funcion de activacion tanh")
        plt.xlabel("Entrada")
        plt.ylabel("Salida tanh(x)")
        plt.grid(True)
        plt.show()

    case _:
        print("Opción no válida")

#* ya estufas mi brandom.
#gracias condiciones por existir
# mire nomas, de puro hacer "case" se logro

