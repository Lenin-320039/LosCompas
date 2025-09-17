import time 
# calificaciones de pelicula de sherk 
pepito_sherk = 5
ramona_sherk = 1
alvinyakitori_sherk = 4
# calificaciones de pelicula jackass
pepito_jackass = 5
ramona_jackass = None
alvinyakitori_jackass = 2 

# 1) calcular entre pepito y ramona pelicula sherk 
numerador = pepito_sherk * ramona_sherk 
numerador2 = pepito_sherk * alvinyakitori_sherk 
dedominador = (pepito_sherk**2)**0.5 * (ramona_sherk**2)**0.5
dedominador2 = (pepito_sherk**2)**0.5 * (alvinyakitori_sherk**2)**0.5
similitud2 = numerador2 / dedominador2
similitud = numerador / dedominador

# 2)calcular la similitud 

prediccion = ((similitud * pepito_jackass) + (similitud2 * alvinyakitori_jackass)) / (similitud + similitud2) 
# resultados 
print ("similitud pepito-ramona:", round (similitud, 2))
print ("similitud pepito-alvin:", round (similitud2, 2))
print ("prediccion de ramona para jackass", round (prediccion, 3))

# Lo hicimos en clase todo el equipo en la compu de Johan
#me gano una impresora :<
# wtf why 2 codes? :0
