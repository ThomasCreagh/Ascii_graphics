from time import sleep
import numpy as np
from fractions import Fraction


# defining vectors
#   (x, y, z)
cube_x_dim = 1
cube_y_dim = 1
cube_z_dim = 1

cube_x_pos = 0
cube_y_pos = 0
cube_z_pos = 0

cube_theta = 45

cube_x_rot = 0
cube_y_rot = 0
cube_z_rot = 0

# cube_y_pos += 0.5

frame_neg = 10
frame_scale = 50

frame_length = (frame_neg*2)+frame_scale 
frame_width = (frame_neg*2)+frame_scale

frame = [[0 for i in range(frame_width)] for i in range(frame_length)]
frame_reset = [[0 for i in range(frame_width)] for i in range(frame_length)]

a = [cube_x_pos,
     cube_y_pos,
     cube_z_pos]

b = [cube_x_pos + cube_x_dim,
     cube_y_pos,
     cube_z_pos]

c = [cube_x_pos,
     cube_y_pos + cube_y_dim,
     cube_z_pos]

d = [cube_x_pos + cube_x_dim,
     cube_y_pos + cube_y_dim,
     cube_z_pos]


e = [cube_x_pos,
     cube_y_pos,
     cube_z_pos + cube_z_dim]

f = [cube_x_pos + cube_x_dim,
     cube_y_pos,
     cube_z_pos + cube_z_dim]

g = [cube_x_pos,
     cube_y_pos + cube_y_dim,
     cube_z_pos + cube_z_dim]

h = [cube_x_pos + cube_x_dim,
     cube_y_pos + cube_y_dim,
     cube_z_pos + cube_z_dim]


plane_point = [2, 0.5, 0.5]
plane_norm = np.array([1, 0, 0])
focal_point = [3, 0.5, 0.5]

class Vertex():
    def __init__(self, a_base, b_base, c_base, focal_point=focal_point, plane_norm=plane_norm, plane_point=plane_point):
        self.focal_point = focal_point
        self.plane_norm = plane_norm
        self.plane_point = plane_point
        self.a = a_base
        self.b = b_base
        self.c = c_base
        self.point_on_plane = self.get_point_on_plane()

    def get_vector(self, p1, p2):
        return np.array([p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2]])

    def get_norm(self, v1, v2):
        return np.cross(v1, v2)
    
    def get_point_on_plane(self):

        focal_a = self.get_vector(self.focal_point, self.a)
        focal_b = self.get_vector(self.focal_point, self.b)
        focal_c = self.get_vector(self.focal_point, self.c)

        norm_d = self.get_norm(focal_a, focal_b)
        norm_f = self.get_norm(focal_a, focal_c)


        d_sum = sum([(focal_point[0]) * (norm_d[0]),
                     (focal_point[1]) * (norm_d[1]),
                     (focal_point[2]) * (norm_d[2])])

        f_sum = sum([(focal_point[0]) * (norm_f[0]),
                     (focal_point[1]) * (norm_f[1]),
                     (focal_point[2]) * (norm_f[2])])

        plane_sum = sum([(plane_norm[0] * plane_point[0]),
                         (plane_norm[1] * plane_point[1]),
                         (plane_norm[2] * plane_point[2])])

        A = np.array([[norm_d[0], norm_d[1], norm_d[2]],
                      [norm_f[0], norm_f[1], norm_f[2]],
                      [plane_norm[0], plane_norm[1], plane_norm[2]]])


        B = np.array([d_sum, f_sum, plane_sum])

        A_inv = np.linalg.inv(A)

        return A_inv.dot(B)


def set_verties():
    global a, b, c, d, e, f, g, h

    a = [cube_x_pos,
        cube_y_pos,
        cube_z_pos]

    b = [cube_x_pos + cube_x_dim,
        cube_y_pos,
        cube_z_pos]

    c = [cube_x_pos,
        cube_y_pos + cube_y_dim,
        cube_z_pos]

    d = [cube_x_pos + cube_x_dim,
        cube_y_pos + cube_y_dim,
        cube_z_pos]


    e = [cube_x_pos,
        cube_y_pos,
        cube_z_pos + cube_z_dim]

    f = [cube_x_pos + cube_x_dim,
        cube_y_pos,
        cube_z_pos + cube_z_dim]

    g = [cube_x_pos,
        cube_y_pos + cube_y_dim,
        cube_z_pos + cube_z_dim]

    h = [cube_x_pos + cube_x_dim,
        cube_y_pos + cube_y_dim,
        cube_z_pos + cube_z_dim]

    h_point = Vertex(h, d, f)
    d_point = Vertex(d, b, h)
    b_point = Vertex(b, f, d)
    f_point = Vertex(f, h, b)

    g_point = Vertex(g, c, e)
    c_point = Vertex(c, g, a)
    a_point = Vertex(a, c, e)
    e_point = Vertex(e, a, g)
    
    # 3 lines from a
    calculate_line(a_point.point_on_plane[1], a_point.point_on_plane[2],
                   b_point.point_on_plane[1], b_point.point_on_plane[2])

    calculate_line(a_point.point_on_plane[1], a_point.point_on_plane[2],
                   c_point.point_on_plane[1], c_point.point_on_plane[2])
    # print_frame()
    # quit()
    calculate_line(a_point.point_on_plane[1], a_point.point_on_plane[2],
                   e_point.point_on_plane[1], e_point.point_on_plane[2])


    # 3 lines from d
    calculate_line(d_point.point_on_plane[1], d_point.point_on_plane[2],
                   b_point.point_on_plane[1], b_point.point_on_plane[2])
    
    calculate_line(d_point.point_on_plane[1], d_point.point_on_plane[2],
                   c_point.point_on_plane[1], c_point.point_on_plane[2])
    
    calculate_line(d_point.point_on_plane[1], d_point.point_on_plane[2],
                   h_point.point_on_plane[1], h_point.point_on_plane[2])
    

    # 3 lines from f
    calculate_line(f_point.point_on_plane[1], f_point.point_on_plane[2],
                   h_point.point_on_plane[1], h_point.point_on_plane[2])

    calculate_line(f_point.point_on_plane[1], f_point.point_on_plane[2],
                   e_point.point_on_plane[1], e_point.point_on_plane[2])
    
    calculate_line(f_point.point_on_plane[1], f_point.point_on_plane[2],
                   b_point.point_on_plane[1], b_point.point_on_plane[2])
    

    # 3 lines from g
    calculate_line(g_point.point_on_plane[1], g_point.point_on_plane[2],
                   c_point.point_on_plane[1], c_point.point_on_plane[2])
    
    calculate_line(g_point.point_on_plane[1], g_point.point_on_plane[2],
                   e_point.point_on_plane[1], e_point.point_on_plane[2])
    
    calculate_line(g_point.point_on_plane[1], g_point.point_on_plane[2],
                   h_point.point_on_plane[1], h_point.point_on_plane[2])
    

    # print("h", h_point.point_on_plane)
    # print("d", d_point.point_on_plane)
    # print("b", b_point.point_on_plane)
    # print("f", f_point.point_on_plane)

    # print("g", g_point.point_on_plane)
    # print("c", c_point.point_on_plane)
    # print("a", a_point.point_on_plane)
    # print("e", e_point.point_on_plane)
    # print()


def print_frame():
    global frame
    for i in range(1, len(frame)-1):
        line = list(map(lambda x: "." if x == 0 else "@", frame[-i]))
        print(*line)

def calculate_line(x1, y1, x2, y2):
    global frame
    x1, y1, x2, y2 = (round(x1*frame_scale),
                      round(y1*frame_scale),
                      round(x2*frame_scale),
                      round(y2*frame_scale))
    
    if x2 - x1 == 0:
        for y in range(0, abs(round(y1-y2))):
            if y2 > y1:
                frame[round(y+y1)+frame_neg][round(x1)+frame_neg] = 1
            else:
                frame[round(y+y2)+frame_neg][round(x1)+frame_neg] = 1
    elif y2 - y1 == 0:
        for x in range(0, abs(round(x1-x2))):
            if x2 > x1:
                frame[round(y1)+frame_neg][round(x+x1)+frame_neg] = 1
            else:
                frame[round(y1)+frame_neg][round(x+x2)+frame_neg] = 1
    else:
        slope = (y2 - y1)/(x2 - x1)
        # if x1 == 37.5 and x2 == 12.5:
        #     print("debug")


        if x1 >= y1:
            for y in range(round(y1), round(y2)):
                x = (slope*(y-y1))+x1
                frame[round(y)+frame_neg][round(x)+frame_neg] = 1
        else:
            for x in range(round(x1), round(x2)):
                y = (slope*(x-x1)) + y1
                frame[round(y)+frame_neg][round(x)+frame_neg] = 1

    

# def calculate_line(x1, y1, x2, y2):
#     global frame
#     x1, y1, x2, y2 = (round(x1*frame_scale),
#                       round(y1*frame_scale),
#                       round(x2*frame_scale),
#                       round(y2*frame_scale))
#     numerator = y2 - y1
#     denominator = x2 - x1
#     # print(numerator, denominator)
#     # if x1 == 7 and x2 == 7 and y1 == 7 and y2 == 4:
#     #     print("debug")
#     def get_frac(numerator, denominator):
#         frac = []
#         if denominator != 0:
#             frac = str(Fraction(numerator, denominator)).split("/")
#         if numerator == 0:
#             numerator = 1
#             frac = str(Fraction(numerator, denominator)).split("/")


#         if len(frac) > 1:
#             rise, run = abs(int(frac[0])), abs(int(frac[1]))
#         elif len(frac) == 1:
#             rise, run = abs(int(frac[0])), 1
#         else:
#             rise, run = abs(numerator), abs(denominator)
        
#         return rise, run

#     if numerator%2 != 0 and denominator %2 == 0:
#         numerator += 1
#     if denominator%2 != 0 and numerator %2 == 0:
#         denominator += 1
    
#     rise, run = get_frac(numerator, denominator)
#     # if rise%2 != 0 and run %2 == 0:
#     #     rise += 1
#     # if run%2 != 0 and rise %2 == 0:
#     #     run += 1
#     # rise, run = get_frac(rise, run)
    

#     num_lim, den_lim = y1, x1
#     num_count, den_count = y2, x2

#     first_time = True
#     while (num_count != num_lim and den_count != den_lim) or (first_time):
#         first_time = False
#         frame[(num_count)+frame_neg][(den_count)+frame_neg] = 1
#         for i in range(rise):
#             # print((num_count)+frame_neg, (den_count)+frame_neg)
#             if num_lim > num_count:
#                 num_count += 1
#             else:
#                 num_count -= 1
#             frame[(num_count)+frame_neg][(den_count)+frame_neg] = 1
#         for i in range(run):
#             if den_lim > den_count:
#                 den_count += 1
#             else:
#                 den_count -= 1
#             frame[(num_count)+frame_neg][(den_count)+frame_neg] = 1

# def rotate(x1, y1, x2, x3, y3, x4,T):
#     h = (x1 + x2)/2
#     k = (y1 + y3)/2

#     r = ((h - x1)**2+(k - y1)**2)**0.5

#     def x_circle(x, h=h, k=k, r=r):
#         a = 1
#         b = 2 * k
#         c = (x - h)**2 - r**2 + k**2
#         return ((-b + (b**2 - (4 * (a) * (c)))**0.5)/2,
#                 (-b - (b**2 - (4 * (a) * (c)))**0.5)/2)

#     # x1 = x1 * np.cos(T)
#     # print(x1, T)
#     # x2 = x2 * np.cos(T)
#     # x3 = x3 * np.cos(T)
#     # x4 = x4 * np.cos(T)
#     x1 += 0.1
#     x2 += 0.1
#     x3 += 0.1
#     x4 += 0.1

#     y2, y1 = x_circle(x1)
#     y4, y3 = x_circle(x3)

#     return x1, y1, x2, y2, x3, y3, x4, y4


def rotate(x1, x2, y1, y3, A):
    global cube_theta, cube_x_rot, cube_y_rot
    cube_theta += A
    h = (x1 + x2)/2
    k = (y1 + y3)/2

    r = ((h - x1)**2+(k - y1)**2)**0.5
    # print(r)

    cube_x_rot = r * np.cos(cube_theta)
    cube_y_rot = r * np.sin(cube_theta)

    if (cube_theta) >= 90:
        cube_theta = 0


while 1:
    frame = [[0 for i in range(frame_width)] for i in range(frame_length)]
    # rotate(a[0], b[0], a[1], c[1], 5)
    set_verties()
    # calculate_line(0, 0, 0.5, 0)
    print_frame()
    print()
    cube_y_pos += 0.1

    sleep(.5)
