import math
import display

def cone_2(point, vector, radius):
    angle = ((90 - radius) * math.pi) / 180
    a = math.pow(vector[0], 2) + math.pow(vector[1], 2) - (math.pow(vector[2], 2)
    / math.pow(math.tan(angle), 2))
    b = (2 * point[0] * vector[0]) + (2 * point[1] * vector[1]) - ((2 * point[2]
    * vector[2]) / math.pow(math.tan(angle), 2))
    c = math.pow(point[0], 2) + math.pow(point[1], 2) - (math.pow(point[2], 2) /
    math.pow(math.tan(angle), 2))
    display.display(a, b, c, point, vector)

def cone(point, vector, radius):
    print("Cone with a %i degree angle" % radius)
    print('Line passing through the point (', point[0], sep='', end=', ')
    print(point[1], sep='', end=', ')
    print(point[2], sep='', end=') ')
    print('and parallel to the vector (', vector[0], sep='', end=', ')
    print(vector[1], sep='', end=', ')
    print(vector[2], sep='', end=')\n')
    cone_2(point, vector, radius)
    