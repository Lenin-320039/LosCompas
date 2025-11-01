import tensorflow as tf

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



