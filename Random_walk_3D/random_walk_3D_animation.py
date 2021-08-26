import matplotlib.pyplot as plt  # noqa
import matplotlib.animation as animation
import numpy as np
import random
import math

x_position = [0]
y_position = [0]
z_position = [0]


def random_walk_3d(self):  # noqa
    """
    Simulate one step of a 2D random walk.

    The steps can be in any direction in the 2D plane.
    """
    polar_angle = random.random()*2*math.pi
    radius = 1
    x_position.append(x_position[-1] + radius*math.cos(polar_angle))
    y_position.append(y_position[-1] + radius*math.sin(polar_angle))
    z_position.append(z_position[-1] + np.random.choice([-1, 0, 1]))
    ax = plt.axes(projection='3d')
    ax.plot3D(x_position, y_position, z_position)
    ax.scatter(0, 0, 0, color="red")
    ax.text(0, 0, 0, "Start")


animation = animation.FuncAnimation(fig=plt.figure(), func=random_walk_3d)
plt.show()
