import numpy as np
from math import *

class Sphere:
    def __init__(self, origin_x = 200, origin_y = 200, radius = 10, scale = 20, rotation_speed = 0.003, surface_color = (200, 0, 200)):
        self.points = []

        self.r = radius
        self.scale = scale
        self.angle = 0
        self.centre = [origin_x, origin_y]
        self.angle_increment = rotation_speed
        self.surface_color = surface_color

        self.initpoints()

        self.projection_matrix = np.matrix([
            [1, 0, 0],
            [0, 1, 0]
        ])

        self.projected_points = [
            [n, n] for n in range(len(self.points))
        ]
        

    def initpoints(self):
        r = self.r
        for x in range(r + 1):
            y_max = ((r*r) - (x*x)) ** 0.5
            y_max = floor(y_max)

            for y in range(y_max + 1):
                z = ((r*r) - (x*x) - (y*y)) ** 0.5
                z = round(z, 1)

                self.points.append(np.matrix([x, y, z]))
                self.points.append(np.matrix([x, -y, z]))
                self.points.append(np.matrix([-x, y, z]))
                self.points.append(np.matrix([-x, -y, z]))
                self.points.append(np.matrix([x, y, -z]))
                self.points.append(np.matrix([x, -y, -z]))
                self.points.append(np.matrix([-x, y, -z]))
                self.points.append(np.matrix([-x, -y, -z]))

    def rotateSphere_AntiC(self):
        self.rotation_z = np.matrix([
            [cos(self.angle), -sin(self.angle), 0],
            [sin(self.angle), cos(self.angle), 0],
            [0, 0, 1],
        ])

        self.rotation_y = np.matrix([
            [cos(self.angle), 0, sin(self.angle)],
            [0, 1, 0],
            [-sin(self.angle), 0, cos(self.angle)],
        ])

        self.rotation_x = np.matrix([
            [1, 0, 0],
            [0, cos(self.angle), -sin(self.angle)],
            [0, sin(self.angle), cos(self.angle)],
        ])

        i = 0
        for point in self.points:
            rotated2d = np.dot(self.rotation_z, point.reshape((3, 1)))
            rotated2d = np.dot(self.rotation_y, rotated2d)
            #rotated2d = np.dot(self.rotation_x, rotated2d)

            projected2d = np.dot(self.projection_matrix, rotated2d)

            x = int(projected2d[0][0] * self.scale) + self.centre[0]
            y = int(projected2d[1][0] * self.scale) + self.centre[1]

            self.projected_points[i] = [x, y]
            i += 1

        self.angle += self.angle_increment

    def rotateSphere_C(self):
        self.rotation_z = np.matrix([
            [cos(self.angle), sin(self.angle), 0],
            [-sin(self.angle), cos(self.angle), 0],
            [0, 0, 1],
        ])

        self.rotation_y = np.matrix([
            [cos(self.angle), 0, -sin(self.angle)],
            [0, 1, 0],
            [sin(self.angle), 0, cos(self.angle)],
        ])

        self.rotation_x = np.matrix([
            [1, 0, 0],
            [0, cos(self.angle), sin(self.angle)],
            [0, -sin(self.angle), cos(self.angle)],
        ])

        i = 0
        for point in self.points:
            rotated2d = np.dot(self.rotation_z, point.reshape((3, 1)))
            rotated2d = np.dot(self.rotation_y, rotated2d)
            #rotated2d = np.dot(self.rotation_x, rotated2d)

            projected2d = np.dot(self.projection_matrix, rotated2d)

            x = int(projected2d[0][0] * self.scale) + self.centre[0]
            y = int(projected2d[1][0] * self.scale) + self.centre[1]

            self.projected_points[i] = [x, y]
            i += 1

        self.angle += self.angle_increment