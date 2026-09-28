import numpy as np
import math

def Sigmoid(z):
  return 1/(1+math.exp(-z))
X1 = 2
X2 = 3
W1 = 0.4
W2 = 0.6
bias = 0.5

y = (W1 * X1  + W2 * X2  + bias)

x = Sigmoid(y)
print("Weihted sum:",y)
print("Sigmoid:",x)

# Output is near to 1
