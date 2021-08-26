import matplotlib.pyplot as plt # noqa
import numpy as np
import matplotlib.animation as animation

x_position = [0]
y_position = [0]
z_position = [0]


def random_step_3d(self):
    """Simulate 1 step of a 3D random walk on a grid."""
    x_position.append(x_position[-1] + np.random.choice([-1, 0, 1]))
    y_position.append(y_position[-1] + np.random.choice([-1, 0, 1]))
    z_position.append(z_position[-1] + np.random.choice([-1, 0, 1]))
    ax = plt.axes(projection='3d')
    ax.plot3D(x_position, y_position, z_position)
    ax.scatter(0, 0, 0, color="red")
    ax.text(0, 0, 0, "Start")


animation = animation.FuncAnimation(fig=plt.figure(), func=random_step_3d)
plt.show()
