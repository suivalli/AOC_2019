f_name = '6_test2.txt'
DEBUG = True

node_1 = 'YOU'
node_2 = 'SAN'

class Planet:
    def __init__(self, name, orbits=None):
        self.name = name
        self.orbits = orbits

    def __str__(self):
        if self.orbits:
            str = "Name: " + self.name + ", orbits : \n"
            orbit_names = []
            for orbit in self.orbits:
                str += 'Orbit ' + orbit.name + "\n"
            return str
        else:
            return "Name: " + self.name + ", no orbits\n"

    def num_orbits(self):
        return len(self.orbits)

    def num_children(self):
        count = self.num_orbits()
        for orbit in self.orbits:
            count += orbit.num_children()
        return count


def init_planets(f_name):
    planets = []
    with open(f_name) as fp:
        line = fp.readline()
        while line:
            name, orbit = line.split(')')
            orbit = orbit.rstrip()
            planets.append((name, orbit))
            line = fp.readline()
    return create_tree(planets, 'COM')


def find(planets, find):
    found = []
    for i in range(0, len(planets)):
        if planets[i][0] == find:
            found.append(i)
    return found


def create_tree(planets, node):
    found = find(planets, node)
    planet = Planet(node)
    orbits = []
    for f in found:
        orbits.append(create_tree(planets, planets[f][1]))
    planet.orbits = orbits
    return planet


tree = init_planets(f_name)


def print_tree(tree):
    if tree is None:
        return
    print(tree)
    for orbit in tree.orbits:
        print_tree(orbit)


def count_all(tree):
    count = tree.num_children()
    for orbit in tree.orbits:
        count += count_all(orbit)
    return count


def find_parent(tree, node):
    for f in tree.orbits:
        if f.name == node:
            print(tree.name)
            return tree.name
        else:
            print(tree.name)
            return find_parent(f, node)





print(find_parent(tree, node_1))
