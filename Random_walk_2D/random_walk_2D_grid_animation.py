import matplotlib.pyplot as plt # noqa
import numpy as np
import matplotlib.animation as animation

x_position = [0]
y_position = [0]


def random_step_2d(self):
    """Simulate 1 step of a random walk on a grid."""
    x_position.append(x_position[-1] + np.random.choice([-1, 0, 1]))
    y_position.append(y_position[-1] + np.random.choice([-1, 0, 1]))
    plt.plot(x_position, y_position, color="C0")


animation = animation.FuncAnimation(fig=plt.figure(), func=random_step_2d)

plt.show()
