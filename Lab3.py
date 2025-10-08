#Simulacion de una Compuerta logica NAND 

#ñd de entrada (x1, x2)
entradas = [[0,0], [0,1], [1,0], [1,1]]

#*Pesos y bias 
w1, w2, b = -1, -1, 1.5

#Función de activación 
def step(x):
    """Función de activación escalón"""
    if x >= 0:
        return 1
    else:
        return 0

print("Simulación de una sola neurona (NAND lógico):\n")
for x in entradas:
    x1, x2 = x
    # cálculo de la neurona:
    z = x1*w1 + x2*w2 + b
    salida = step(z)
    print(f"Entrada: {x} -> z={z:.1f}, salida={salida}")

    #INCREIBLE johan
    #Trabajo en equipo en llamada Lenin aaaa
