import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from IPython.display import HTML


def animate_field(x, y, field, n_val, vmin=None, vmax=None):
    fig, ax = plt.subplots()

    xx, yy = np.meshgrid(x, y)
    if not vmin:
        vmin = np.amin(field[:, n_val])
    if not vmax:
        vmax = np.amax(field[:, n_val])

    imgs = []
    for f in field:
        qm = plt.pcolormesh(xx, yy, f[n_val], vmin=vmin, vmax=vmax)
        imgs.append((qm,))

    fig.colorbar(qm)

    ani = animation.ArtistAnimation(fig, imgs)
    return HTML(ani.to_jshtml())


def animate_velocity(x, y, field):
    fig, ax = plt.subplots()

    xx, yy = np.meshgrid(x, y)
    imgs = [(plt.quiver(xx, yy, f[7], f[8], scale_units='xy', scale=2.0),)
            for f in field]

    ani = animation.ArtistAnimation(fig, imgs)
    return HTML(ani.to_jshtml())


def plot_magnetic_line(x, y, field):
    fig, ax = plt.subplots()

    xx, yy = np.meshgrid(x, y)
    plt.streamplot(xx, yy, field[-1, 0], field[-1, 1])


def plot_velocity_line(x, y, field):
    fig, ax = plt.subplots()

    xx, yy = np.meshgrid(x, y)
    plt.streamplot(xx, yy, field[-1, 7], field[-1, 8])


def animate_2x2_fields(x, y, field):
    '''
    plot preassure, density, x-direction of magnetic field
    and hypothetical potential for divB
    '''
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))

    vmins = [np.amin(field[:, i]) for i in [5, 6, 0, 4]]
    vmaxs = [np.amax(field[:, i]) for i in [5, 6, 0, 4]]

    imgs = []
    for f in field:
        im = [
            axes.flat[i]
                .pcolormesh(x, y, f[n_val], vmin=vmins[i], vmax=vmaxs[i])
            for i, n_val in enumerate([5, 6, 0, 4])
        ]

        for ax, title in zip(axes.flat, ['pr', 'ro', 'bx', 'phi']):
            ax.set_title(title)
            ax.label_outer()

        imgs.append(im)

    for qm, ax in zip(im, axes.flat):
        fig.colorbar(qm, ax=ax)

    ani = animation.ArtistAnimation(fig, imgs)
    return HTML(ani.to_jshtml())


def animate_magnetic_line(x, y, field):
    fig, ax = plt.subplots()

    def update(i):
        ax.clear()
        ax.streamplot(x, y, field[i, 0], field[i, 1])

    ani = animation.FuncAnimation(fig, update, frames=len(field))
    return HTML(ani.to_jshtml())


def animate_flow_line(x, y, field):
    fig, ax = plt.subplots()

    def update(i):
        ax.clear()
        ax.streamplot(x, y, field[i, 7], field[i, 8])

    ani = animation.FuncAnimation(fig, update, frames=len(field))
    return HTML(ani.to_jshtml())
