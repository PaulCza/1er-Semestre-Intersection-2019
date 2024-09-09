import math

def display(a, b, c, point, vector):
    d = math.pow(b, 2) - 4 * (a * c)
    if d > 0:
        print("2 intersection points:")
        x1 = float(((-1 * b) + math.sqrt(d)) / (2 * a))
        x2 = float(((-1 * b) - math.sqrt(d)) / (2 * a))
        a = float(point[0] + x1 * vector[0])
        b = float(point[1] + x1 * vector[1])
        c = float(point[2] + x1 * vector[2])
        print("(%.3f" % a, sep='', end=', ')
        print("%.3f" % b, sep='', end=', ')
        print("%.3f" % c, sep='', end=')\n')
        a = float(point[0] + x2 * vector[0])
        b = float(point[1] + x2 * vector[1])
        c = float(point[2] + x2 * vector[2])
        print("(%.3f" % a, sep='', end=', ')
        print("%.3f" % b, sep='', end=', ')
        print("%.3f" % c, sep='', end=')\n')
    if d == 0:
        print("1 intersection point:")
        x1 = ((-1 * b) / (2 * a))
        a = float(point[0] + x1 * vector[0])
        b = float(point[1] + x1 * vector[1])
        c = float(point[2] + x1 * vector[2])
        print("(%.3f" % a, sep='', end=', ')
        print("%.3f" % b, sep='', end=', ')
        print("%.3f" % c, sep='', end=')\n')
    if d < 0:
        print("No intersection point.")
    return 0
