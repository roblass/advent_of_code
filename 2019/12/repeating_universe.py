import sys
from collections import defaultdict
from math import fabs


class Moon:
    def __init__(self, x, y, z):
        self.x_pos = x
        self.y_pos = y
        self.z_pos = z

        self.original_x = x
        self.original_y = y
        self.original_z = z

        self.x_vel = 0
        self.y_vel = 0
        self.z_vel = 0
        self.history = defaultdict(list)

    def apply_velocity(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel
        self.z_pos += self.z_vel

    def happened_before(self, axis):
        if axis == 0:
            if self.x_pos in self.history[0]:
                return True
            else:
                self.history[0].append(self.x_pos)
                return False

        if axis == 1:
            if self.y_pos in self.history[1]:
                return True
            else:
                self.history[1].append(self.y_pos)
                return False

        if axis == 2:
            if self.z_pos in self.history[2]:
                return True
            else:
                self.history[2].append(self.z_pos)
                return False

        print('what the fuck')
        sys.exit()

    def apply_gravity(self, other_moon):
        if self.x_pos > other_moon.x_pos:
            self.x_vel -= 1
            other_moon.x_vel += 1
        elif self.x_pos < other_moon.x_pos:
            self.x_vel += 1
            other_moon.x_vel -= 1

        if self.y_pos > other_moon.y_pos:
            self.y_vel -= 1
            other_moon.y_vel += 1
        elif self.y_pos < other_moon.y_pos:
            self.y_vel += 1
            other_moon.y_vel -= 1

        if self.z_pos > other_moon.z_pos:
            self.z_vel -= 1
            other_moon.z_vel += 1
        elif self.z_pos < other_moon.z_pos:
            self.z_vel += 1
            other_moon.z_vel -= 1

    def is_original(self):
        if self.x_pos != self.original_x or self.y_pos != self.original_y or \
                self.z_pos != self.original_z:
            return False
        if self.x_vel != 0 or self.y_vel != 0 or self.z_vel != 0:
            return False
        return True

    def __repr__(self):
        pos = 'pos=<x={0}, y={1}, z={2}>'.format(self.x_pos, self.y_pos, self.z_pos)
        vel = 'vel=<x={0}, y={1}, z={2}>'.format(self.x_vel, self.y_vel, self.z_vel)
        return '{0}, {1}'.format(pos, vel)


scan = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        scan.append([int(s.strip().split('=')[1]) for s in line[1:-2].split(',')])

moons = []
for pos in scan:
    moons.append(Moon(*pos))

done = False
t = 0
num_cycles = {}
while not done:
    if t % 10000 == 0:
        print('step', t, 'cycles found', num_cycles)
    completed = []
    for moon1 in moons:
        for moon2 in moons:
            if moon1 == moon2 or moon2 in completed:
                continue
            moon1.apply_gravity(moon2)
        completed.append(moon1)
    done = True
    for index, moon in enumerate(moons):
        moon.apply_velocity()
        for axis in (0, 1, 2):
            if '{0}{1}'.format(index, axis) not in num_cycles.keys() and moon.happened_before(axis):
                print('*******GOT ONE*********')
                num_cycles['{0}{1}'.format(index, axis)] = t
            else:
                done = False
    if len(num_cycles) == 12:
        done = True
        print(num_cycles)
    t += 1

print('took this many iterations', t)

print('After {0} steps'.format(t))
for moon in moons:
    print(moon)

energy = sum([(fabs(m.x_pos) + fabs(m.y_pos) + fabs(m.z_pos)) *
              (fabs(m.x_vel) + fabs(m.y_vel) + fabs(m.z_vel)) for m in moons])
print(energy)
