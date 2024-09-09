import math
import display

def sphere_two(point, vector, radius):
    h = (math.pow(vector[0], 2) + math.pow(vector[1], 2) + math.pow(vector[2], 2))
    i = ((2 * point[0] * vector[0]) + (2 * point[1] * vector[1]) + (2 * point[2] * vector[2]))
    j = (math.pow(point[0], 2) + math.pow(point[1], 2) + math.pow(point[2], 2) - math.pow(radius, 2))
    display.display(h, i, j, point, vector)

def sphere(point, vector, radius):
    print("Sphere of radius", radius)
    print('Line passing through the point (', point[0], sep='', end=', ')
    print(point[1], sep='', end=', ')
    print(point[2], sep='', end=') ')
    print('and parallel to the vector (', vector[0], sep='', end=', ')
    print(vector[1], sep='', end=', ')
    print(vector[2], sep='', end=')\n')
    sphere_two(point, vector, radius)
