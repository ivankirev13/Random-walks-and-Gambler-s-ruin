import random # noqa
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

xposition = [0]
yposition = [0]


def random_walk(self):  # noqa
    """
    Simulate one step of a 2D random walk.

    The steps can be in any direction in the 2D plane.
    """
    polar_angle = random.random()*2*math.pi
    radius = 1
    xposition.append(xposition[-1] + radius*math.cos(polar_angle))
    yposition.append(yposition[-1] + radius*math.sin(polar_angle))
    plt.plot(xposition, yposition, color="C0")


animation = animation.FuncAnimation(fig=plt.figure(), func=random_walk)
plt.show()
