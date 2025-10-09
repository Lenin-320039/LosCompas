import numpy as np

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

valor_unico = 0
print(f"Sigmoid de {valor_unico}: {sigmoid(valor_unico)}")

valores = np.array([-10, 0, 10])
print(f"Sigmoid de {valores}: {sigmoid(valores)}")
