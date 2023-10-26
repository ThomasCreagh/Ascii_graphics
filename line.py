from point import Point

from math import sqrt

class Line():
    def __init__(self, p1: Point, p2: Point):
        self.point_1 = p1
        self.point_2 = p2

    def get_distance(self):
        return sqrt((self.point_1.x - self.point_2.x)**2 +
                    (self.point_1.y - self.point_2.y)**2 +
                    (self.point_1.z - self.point_2.z)**2)