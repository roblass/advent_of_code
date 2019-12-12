import sys
from math import fabs


class Moon:
    def __init__(self, x, y, z):
        self.x_pos = x
        self.y_pos = y
        self.z_pos = z

        self.x_vel = 0
        self.y_vel = 0
        self.z_vel = 0

    def apply_velocity(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel
        self.z_pos += self.z_vel

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

for t in range(int(sys.argv[2])):
    print('After {0} steps'.format(t))
    for moon in moons:
        print(moon)
    completed = []
    for moon1 in moons:
        for moon2 in moons:
            if moon1 == moon2 or moon2 in completed:
                continue
            moon1.apply_gravity(moon2)
        completed.append(moon1)
    for moon in moons:
        moon.apply_velocity()

print('After {0} steps'.format(t))
for moon in moons:
    print(moon)

energy = sum([(fabs(m.x_pos) + fabs(m.y_pos) + fabs(m.z_pos)) *
              (fabs(m.x_vel) + fabs(m.y_vel) + fabs(m.z_vel)) for m in moons])
print(energy)
