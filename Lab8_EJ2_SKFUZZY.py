import numpy as np
import skfuzzy as fuzz

# 1. Rango del universo (0 a 30)
x_temp = np.arange(0, 31, 1)

# 2. Función de pertenencia triangular
mu_frio = fuzz.trimf(x_temp, [0, 0, 20])

# 3. Evaluar pertenencia de varios valores
valores = [0, 5, 10, 15, 20]
for v in valores:
    pertenencia = fuzz.interp_membership(x_temp, mu_frio, v)
    print(f"Temperatura {v}°C → μ_frío({v}) = {pertenencia:.2f}")
#ya quedo mi brandon