import math


def fuel_1(mass):
    return math.floor(mass / 3) - 2


def fuel_2(mass):
    new_mass = math.floor(mass / 3) - 2
    if new_mass <= 0:
        return 0
    return new_mass + fuel_2(new_mass)


with open("1_1.csv", "r") as f:
    module_masses = f.read().splitlines()

total_fuel1 = 0
total_fuel2 = 0

for module_mass in module_masses:
    total_fuel1 += fuel_1(int(module_mass))
    total_fuel2 += fuel_2(int(module_mass))

print('Total fuel 1: ' + str(total_fuel1))
print('Total fuel 2: ' + str(total_fuel2))

