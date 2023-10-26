from point import Point

class Plane():
    def __init__(self, x=0, y=0, z=0, height=1, lenght=1,
                 rotation_x=0, rotation_y=0, rotation_z=0):
        # =OBJECTS INFO=
        self.object_position = Point(-height/2, -lenght/2, 0)
        self.object_size = Point(height, lenght, 0)

        # =WORLD INFO=
        self.position = Point(x, y, z)
        self.rotation = Point(rotation_x, rotation_y, rotation_z)

    def get_normal_plane(self):
        