wire_1 = open('3_1.txt').read().split(',')
wire_2 = open('3_2.txt').read().split(',')


#wire_1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')
#wire_2 = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')


def make_coordinates(wire):
    x = 0
    y = 0
    points = []
    for instructions in wire:
        length = int(instructions[1:])
        if instructions[0] == 'R':
            for i in range(0, length):
                points.append((x, y))
                x = x + 1
        elif instructions[0] == 'L':
            for i in range(0, length):
                points.append((x, y))
                x = x - 1
        elif instructions[0] == 'U':
            for i in range(0, length):
                points.append((x, y))
                y = y + 1
        elif instructions[0] == 'D':
            for i in range(0, length):
                points.append((x, y))
                y = y - 1
    return points


def get_crossings(coords_1, coords_2):
    return list(set(coords_1).intersection(set(coords_2)))


def get_closest_crossing_1(crossings):
    lowest = 999999999999
    crossing_index = 0
    for i in range(0, len(crossings)):
        if crossings[i][0] == 0 and crossings[i][1] == 0:
            continue
        else:
            distance = abs(crossings[i][0]) + abs(crossings[i][1])
            if distance < lowest:
                lowest = distance
                crossing_index = i
    return lowest


wire_1_coords = make_coordinates(wire_1)
wire_2_coords = make_coordinates(wire_2)


def get_closest_crossing_2(crossings):
    combined_steps = 999999999999999
    lowest_crossing = ()
    for crossing in crossings:
        if crossing[0] == 0 and crossing[1] == 0:
            continue
        wire_1_index = wire_1_coords.index(crossing)
        wire_2_index = wire_2_coords.index(crossing)
        steps = wire_1_index + wire_2_index
        if combined_steps > steps:
            combined_steps = steps
            lowest_crossing = crossing
    return combined_steps


crossings = get_crossings(wire_1_coords, wire_2_coords)
distance = get_closest_crossing_1(crossings)


print(get_closest_crossing_2(crossings))

