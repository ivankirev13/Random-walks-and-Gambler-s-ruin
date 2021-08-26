import matplotlib.pyplot as plt # noqa
import numpy as np


def random_walk_2d(number_steps):
    """Simulate 2D random walk on a grid."""
    origin = np.zeros((1, 2))
    # possible directions for each axis
    step_set = [-1, 0, 1]
    step_shape = (number_steps, 2)

    # randomly choose directions for each step
    steps = np.random.choice(a=step_set, size=step_shape)
    path = np.concatenate([origin, steps]).cumsum(0)

    plt.plot(path[:, 0], path[:, 1])
    # label the end point
    plt.scatter(path[-1, 0], path[-1, 1])
    plt.text(path[-1, 0], path[-1, 1], "Finish")


number_of_walks = 3
for i in range(number_of_walks):
    random_walk_2d(1000)
plt.scatter(0, 0)
plt.text(0, 0, "Start")
plt.show()
