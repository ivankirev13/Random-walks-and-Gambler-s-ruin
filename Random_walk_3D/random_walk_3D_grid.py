import matplotlib.pyplot as plt  # noqa
import numpy as np


def random_walk_3d(number_steps):
    """Simulate 3D random walk on a grid."""
    origin = np.zeros((1, 3))
    step_set = [-1, 0, 1]
    step_shape = (number_steps, 3)

    steps = np.random.choice(a=step_set, size=step_shape)
    path = np.concatenate([origin, steps]).cumsum(0)
    ax = plt.axes(projection='3d')
    ax.plot3D(path[:, 0], path[:, 1], path[:, 2])
    ax.scatter(0, 0, 0, color="red")
    ax.text(0, 0, 0, "Start")
    ax.scatter(path[-1, 0], path[-1, 1], path[-1, 2], color="red")
    ax.text(path[-1, 0], path[-1, 1], path[-1, 2], "End")


fig = plt.figure()
random_walk_3d(1000)
plt.show()
