from line import Line
from point import Point

p1 = Point(0, 0, 0)
p2 = Point(1, 0, 0)

line1 = Line(p1, p2)

print(line1.get_distance())
