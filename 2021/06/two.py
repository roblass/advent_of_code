import sys

days = int(sys.argv[2])
originals = [int(e.strip()) for e in open(sys.argv[1], 'r').read().split(',')]

population = [0 for i in range(9)]
for o in originals:
    population[o] += 1

print(population)

for day in range(days):
    population.append(0)
    born = population.pop(0)
    population[6] += born # mama fish
    population[8] += born # baby fish
    print(population)

print(sum(population))
