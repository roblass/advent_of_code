import sys

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

image = {}
for x in range(width):
    for y in range(height):
        for layer in layers:
            pixel = layer[x + y * width]
            if int(pixel) < 2:
                try:
                    _ = image[(x, y)]
                except:
                    # i found this easier to read
                    if pixel == '0':
                        image[(x, y)] = ' '
                    else:
                        image[(x, y)] = pixel

s = ''
for y in range(height):
    for x in range(width):
        s += image[(x, y)]
    s += '\n'

print(s)
