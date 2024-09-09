import math
import display

def cylinder_two(point, vector, radius):
    if (math.pow(point[0], 2) + math.pow(point[1], 2) - math.pow(radius, 2)) == 0:
        print("There is an infinite number of intersection points.")
        return 0
    else:
        a = float((math.pow(vector[0], 2) + math.pow(vector[1], 2)))
        b = float((2 * point[0] * vector[0]) + (2 * point[1] * vector[1]))
        c = float((math.pow(point[0], 2) + math.pow(point[1], 2) - math.pow(radius, 2)))
        display.display(a, b, c, point, vector)
        return 0



def cylinder(point, vector, radius):
    print("Cylinder of radius", radius)
    print('Line passing through the point (', point[0], sep='', end=', ')
    print(point[1], sep='', end=', ')
    print(point[2], sep='', end=') ')
    print('and parallel to the vector (', vector[0], sep='', end=', ')
    print(vector[1], sep='', end=', ')
    print(vector[2], sep='', end=')\n')
    cylinder_two(point, vector, radius)
