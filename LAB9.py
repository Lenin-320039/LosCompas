import random

#todo crear una solucion al azar (0 -- 10)

def crear_individuo():
    return random.randint(0, 10)

#calcular el fitness de un individuo

def fitness(x):
    return x   #entre mas grande mejor

#todo proceso de seleccion
def selection(poblacion):
    a = random.choice(poblacion)
    b = random.choice(poblacion)
    return a if fitness(a) > fitness(b) else b

def cruzar(p1, p2):
    return (p1 + p2) // 2

#crossover -- cambiar un individuo al azar
def mutar(x):
    if random.random() < 0.1: #probabilidad de mutacion
        return random.randint(0, 10)
    return x

#todo algoritmo genetico
def go():
    poblacion = [crear_individuo() for _ in range(5)]

    for gen in range(10): 
        print(f"Generacion {gen}: {poblacion}")

        nueva = []
        for _ in range (len(poblacion)):
            p1 = selection(poblacion)
            p2 = selection(poblacion)
            hijo = cruzar(p1, p2)
            hijo = mutar(hijo)
            nueva.append(hijo)

        poblacion = nueva

    mejor = max(poblacion, key=fitness)
    print("\nMejorSolucion_", mejor)

go()
#ya quedo mi brandon
#siu
