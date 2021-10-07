# coder: Diwei Zhang; listener & sharer: Yiting Han.
# File created: 10/07

import numpy as np

class Layer():
    def __init__(self, shape, actv):
        self.shape = shape
        self.actv = actv
        self.weights = np.random.uniform(0.0, 0.02, size=shape)
        self.bias = np.random.uniform(size=shape[1]).reshape(1,-1)
    def forward(self, inputs):
        out_mat = inputs.dot(self.weights)
        out_mat += self.bias
        out = self.actv(out_mat)
        return out
    def __str__(self):
        string =  "shape: (%d, %d)" % (self.shape[0], self.shape[1])
        string += "; actv:" + self.actv.__name__
        return string
    def __repr__(self) -> str:
        return "Layer(shape=(%d, %d)"%(self.shape[0], self.shape[1]) + ", actv=" + self.actv.__name__ + ")"
    def __len__(self):
        return self.shape[1]

shape1 = (100, 50)
shape2 = (50, 1)
actv = np.tanh
inputs = np.random.uniform(0.0, 1.0, 100).reshape(1,-1)

layer1 = Layer(shape1, actv)
layer2 = Layer(shape2, actv)


print(layer1)
print(len(layer1))
print(repr(layer2))
h1 = layer1.forward(inputs)
print(h1)
h2 = layer2.forward(h1)
print(h2)