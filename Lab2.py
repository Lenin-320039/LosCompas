#LAB_2
#Realizar el programa en Python con lo solicitado en clase de las diapositivas "HandsOn_Lab2".

import time
import math

from math import sqrt, pow

#USER 1 (Frijolito)
frijolito_pokemon = 3.5
frijolito_naruto = 5
frijolito_demon = None

#USER 2 (Pitochu)
pitochu_pokemon = 2.5
pitochu_naruto = None
pitochu_demon = 3.5

#USER 3 (Kenny)
kenny_pokemon = None
kenny_naruto = 4.5
kenny_demon = 4.5

#user 4 (Chow)
chow_pokemon = 2.5
chow_naruto = 3.5
chow_demon = 4.5


#SIMILITUDES...-------------------------------------#

#similitud 1---> frijolito y pitochu 

numeradorsim1 = frijolito_pokemon * pitochu_pokemon
denominadorsim1 = (math.sqrt(math.pow(frijolito_pokemon, 2))) * (math.sqrt(math.pow(pitochu_pokemon, 2)))
simFriPi = numeradorsim1 / denominadorsim1

#similitud 2---> Chow y Kenny

numeradorsim2 = (kenny_naruto * chow_naruto) + (kenny_demon * chow_demon)
denominadorsim2 = (math.sqrt((math.pow(kenny_naruto, 2)) + (math.pow(kenny_demon, 2)))) * (math.sqrt((math.pow(chow_naruto, 2)) + (math.pow(chow_demon, 2))))
simChKe = numeradorsim2 / denominadorsim2

#similitud 3---> Chow y Pitochu

numeradorsim3 = (pitochu_pokemon * chow_pokemon) + (pitochu_demon * chow_demon)
denominadorsim3 = (math.sqrt((math.pow(chow_pokemon, 2)) + (math.pow(chow_demon, 2)))) * (math.sqrt((math.pow(pitochu_pokemon, 2)) + (math.pow(pitochu_demon, 2))))
simChPi = numeradorsim3 / denominadorsim3

#similitud 4---> Chow y Frijolito

numeradorsim4 = (frijolito_pokemon * chow_pokemon) + (frijolito_naruto * chow_naruto)
denominadorsim4 = (math.sqrt((math.pow(chow_pokemon, 2)) + (math.pow(chow_naruto, 2)))) * (math.sqrt((math.pow(frijolito_pokemon, 2)) + (math.pow(frijolito_naruto, 2))))
simChFr = numeradorsim4 / denominadorsim4

#similitud 5---> Pitochu y Kenny

numeradorsim5 = pitochu_demon * kenny_demon
denominadorsim5 = (math.sqrt(math.pow(pitochu_demon, 2))) * (math.sqrt(math.pow(kenny_demon, 2)))
simPiKe = numeradorsim5 / denominadorsim5

#similitud 6---> Frijolito y Kenny

numeradorsim5 = frijolito_naruto * kenny_naruto
denominadorsim5 = (math.sqrt(math.pow(frijolito_naruto, 2))) * (math.sqrt(math.pow(kenny_naruto, 2)))
simFrKe = numeradorsim5 / denominadorsim5

#--------------------------------------------------#

# Predicciones

#prediccion #1 para frijolito ---> demon slayer
num_pre_Fri_demon = (simFriPi * pitochu_demon) + (simChFr * kenny_demon) + (simFrKe * chow_demon)
den_pre_Fri_demon = simFriPi + simChFr + simFrKe
pre_Fri_demon = num_pre_Fri_demon / den_pre_Fri_demon

#prediccion #2 para pitochu ---> naruto
num_pre_Pi_naruto = (simFriPi * frijolito_naruto) + (simChPi * kenny_naruto) + (simPiKe * chow_naruto)
den_pre_Pi_naruto = simFriPi + simChPi + simPiKe
pre_Pi_naruto = num_pre_Pi_naruto / den_pre_Pi_naruto

#prediccion #3 para kenny ---> pokemon
num_pre_Ke_pokemon = (simPiKe * frijolito_pokemon) + (simFrKe * pitochu_pokemon) + (simChKe * chow_pokemon)
den_pre_Ke_pokemon = simPiKe + simFrKe + simChKe
pre_Ke_pokemon = num_pre_Ke_pokemon / den_pre_Ke_pokemon 

# Resultado
print("La similitud entre Frijolito y Pitochu es: ", round(simFriPi, 0))
print("La similitud entre Kenny y Chow es: ", round(simChKe, 0))
print("La similitud entre Chow y Pitochu es: ", round(simChPi, 0))
print("La similitud entre Frijolito y Chow es: ", round(simChFr, 0))
print("La similitud entre Kenny y Pitochu es: ", round(simPiKe, 0))
print("La similitud entre Frijolito y Kenny es: ", round(simFrKe, 0))


print ("Frijolito calificara Demon Slayer con:",round(pre_Fri_demon, 0))
print ("Pitochu calificara Naruto con:", round(pre_Pi_naruto, 0))
print ("Kenny calificara Pokemon con:", round(pre_Ke_pokemon, 0))
