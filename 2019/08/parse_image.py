import sys

import numpy as np

width = int(sys.argv[1])
height = int(sys.argv[2])
filename = sys.argv[3]

layers = []
with open(filename, 'r') as f:
    data = f.read()
    layer_size = width * height
    for i in range(int(len(data) / layer_size)):
        try:
            layers.append(data[layer_size * i:layer_size * (i + 1)])
        except KeyError:
            break

min_zeros = np.inf
best_layer = None
for layer in layers:
    num_zeros = len([c for c in layer if c == '0'])
    if num_zeros < min_zeros:
        min_zeros = num_zeros
        best_layer = layer

num_ones = len([c for c in best_layer if c == '1'])
num_twos = len([c for c in best_layer if c == '2'])
print(num_ones * num_twos)
