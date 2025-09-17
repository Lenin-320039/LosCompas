import time 
#? Luis record
luis_matrix = 4
luis_frozen = 2
#? Luis record
ana_matrix = 5
ana_frozen = None
#! known records

# Paso 1: calcular similitud entre Ana(U) y Luis(V)
numerador = ana_matrix * luis_matrix
denominador = (ana_matrix**2)**0.5 * (ana_matrix**2)**0.5
similitud = numerador / denominador
#todo paso 1: calcular

#todo paso 2
prediction = (similitud * luis_frozen) / similitud
#?Resultados:
print("similitud Ana-Luis:", round (similitud,2))
print("prediccion de Ana para Frozen:", round(prediction,2))
# estuvo buena la practica
# hola como estas
#hola necesitamos corregir el punto 2, #2 predicción.
