from math import sqrt

class Point:
    def __init__(coordinate, x_coordinate, y_coordinate):
        coordinate.x = x_coordinate
        coordinate.y = y_coordinate

    def distance(line, point2):
            dx = point2.x - line.x
            dy = point2.y - line.y
            result = sqrt(dx*dx + dy*dy)
            return result