# coder: Haoming Chen
# listener and sharer: Yiting Han

import numpy as np
import numpy.random

def layer(shape, actv):
    def layer_output(inputs, weights, bias):
        print("inputs shape")
        print(inputs.shape)
        print("Weights shape")
        print(weights.shape)
        return actv(inputs.dot(weights) + bias)

    return layer_output

t = np.random.uniform(0.0, 1.0, 100).reshape(1,-1) # input to the network

shape1 = [100, 10]
shape2 = [10, 1]

layer1 = layer(shape1, np.tanh) # Define layer 1
layer2 = layer(shape2, np.tanh) # Define layer 2

# Initialize weights and biases
w1 = np.random.uniform(0.0, 1.0, (shape1[0], shape1[1]))
w2 = np.random.uniform(0.0, 1.0, (shape2[0], shape2[1]))
b1 = np.random.uniform(0.0, 1.0, shape1[1])
b2 = np.random.uniform(0.0, 1.0, shape2[1])

# Run through the network
h1 = layer1(t, w1, b1) # First layer
h2 = layer2(h1, w2, b2) # Last layer