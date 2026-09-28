import numpy as np
import math
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def tanh(z):
    return np.tanh(z)

def relu(z):
    return np.maximum(0, z)


def Marvellous(inputs, weights, bias):
    print("Inputs:", inputs)
    print("Weights:", weights)
    print("Bias:", bias)

    z = 0
    for i in range(len(inputs)):
        z += inputs[i] * weights[i]

    z += bias
    print("Weighted sum:", z)

    y = sigmoid(z)
    print("Sigmoid output:", y)

    return y

def main():
    inputs = [-10, -9, 10, 9]
    weights = [0.4, 0.1, 0.3, 0.2]
    bias = 0.5

    result = Marvellous(inputs, weights, bias)
    print("Predicted result:", result)

    z = np.linspace(-10, 10, 400)

    plt.figure(figsize=(10, 6))
    plt.plot(z, sigmoid(z), label="Sigmoid", linewidth=2, color="blue")
    plt.plot(z, tanh(z), label="Tanh", linewidth=2, color="green")
    plt.plot(z, relu(z), label="ReLU", linewidth=2, color="red")

    plt.title("Activation Functions (Sigmoid, Tanh, ReLU)", fontsize=16)
    plt.xlabel("Input (z)", fontsize=14)
    plt.ylabel("Output", fontsize=14)
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
