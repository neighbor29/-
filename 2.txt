import itertools
import math


def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


with open("input.txt", "r") as file:
    points = [tuple(map(float, line.split())) for line in file]
combinations = itertools.permutations(points, 4)

shortest_route = None
shortest_distance = float('inf')

for route in combinations:
    route_distance = sum(distance(route[i], route[i+1]) for i in range(3))
    if route_distance < shortest_distance:
        shortest_distance = route_distance
        shortest_route = route

with open("output.txt", "w") as file:
    for point in shortest_route:
        file.write("{:.2f} {:.2f}\n".format(point[0], point[1]))
        file.write("{:.2f}".format(shortest_distance))