import sys
from collections import defaultdict
from math import gcd


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

    def back_to_start(self, axis):
        if axis == 0:
            if self.x_pos != self.original_x:
                return False
            return True
        if axis == 1:
            if self.y_pos != self.original_y:
                return False
            return True
        if axis == 2:
            if self.z_pos != self.original_z:
                return False
            return True
        print('should not get here')
        return False

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
    for moon in moons:
        moon.apply_velocity()
    for axis in (0, 1, 2):
        all_lined_up = True
        if axis in num_cycles:
            continue
        for moon in moons:
            if not moon.back_to_start(axis):
                all_lined_up = False
                done = False
                break
        if all_lined_up:
            print('*******GOT ONE*********')
            num_cycles[axis] = t + 2
    if len(num_cycles) == 3:
        done = True
    t += 1

print('num cycles', num_cycles)
print('took this many iterations', t)

total_cycles = num_cycles[0]
total_cycles *= num_cycles[1] / gcd(total_cycles, num_cycles[1])
total_cycles *= num_cycles[2] / gcd(int(total_cycles), num_cycles[2])
print(total_cycles)
