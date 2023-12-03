import numpy as np
from math import *

class Cube:
    def __init__(self, origin_x = 200, origin_y = 200, size = 100, line_thickness = 1, line_color = (255, 0, 0)):
        self.points = []

        self.size = size
        self.line_thickness = line_thickness
        self.origin_pos = [origin_x, origin_y]
        self.angle = 0
        self.FPS = 60
        self.angle_increment_step = 0.005
        self.line_color = line_color

        self.points.append(np.matrix([-1, -1, 1]))
        self.points.append(np.matrix([1, -1, 1]))
        self.points.append(np.matrix([1,  1, 1]))
        self.points.append(np.matrix([-1, 1, 1]))
        self.points.append(np.matrix([-1, -1, -1]))
        self.points.append(np.matrix([1, -1, -1]))
        self.points.append(np.matrix([1, 1, -1]))
        self.points.append(np.matrix([-1, 1, -1]))

        self.projected_points = [
            [n, n] for n in range(len(self.points))
        ]

        self.projection_matrix = np.matrix([
            [1, 0, 0],
            [0, 1, 0]
        ])

    def rotatePoints(self):
        rotation_z = np.matrix([
            [cos(self.angle), -sin(self.angle), 0],
            [sin(self.angle), cos(self.angle), 0],
            [0, 0, 1],
        ])

        rotation_y = np.matrix([
            [cos(self.angle), 0, sin(self.angle)],
            [0, 1, 0],
            [-sin(self.angle), 0, cos(self.angle)],
        ])

        rotation_x = np.matrix([
            [1, 0, 0],
            [0, cos(self.angle), -sin(self.angle)],
            [0, sin(self.angle), cos(self.angle)],
        ])

        i = 0
        for point in self.points:
            rotated2d = np.dot(rotation_z, point.reshape((3, 1)))
            rotated2d = np.dot(rotation_y, rotated2d)
            rotated2d = np.dot(rotation_x, rotated2d)

            projected2d = np.dot(self.projection_matrix, rotated2d)

            x = int(projected2d[0][0] * self.size) + self.origin_pos[0]
            y = int(projected2d[1][0] * self.size) + self.origin_pos[1]

            self.projected_points[i] = [x, y]
            i += 1

        self.angle += self.angle_increment_step