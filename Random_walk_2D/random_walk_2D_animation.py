import random # noqa
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x_position = [0]
y_position = [0]


def random_walk_2d(self):  # noqa
    """
    Simulate one step of a 2D random walk.

    The steps can be in any direction in the 2D plane.
    """
    polar_angle = random.random()*2*math.pi
    radius = 1
    x_position.append(x_position[-1] + radius*math.cos(polar_angle))
    y_position.append(y_position[-1] + radius*math.sin(polar_angle))
    plt.plot(x_position, y_position, color="C0")


animation = animation.FuncAnimation(fig=plt.figure(), func=random_walk_2d)
plt.show()
