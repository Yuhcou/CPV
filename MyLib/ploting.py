import numpy as np
from matplotlib.gridspec import GridSpec
from matplotlib import pyplot as plt


def plot(imgs, axis=0, nsep=1000, img_dis=20, axis_state='off', figsize=(15, 15)):
    if axis not in [0, 1]:
        raise ValueError('Axis must be 0 or 1.')

    num_of_imgs = len(imgs)
    PoIs = [img.shape[1 - axis] for img in imgs]
    total_pixels = sum(PoIs)
    grid_sizes = [round((img.shape[1 - axis] / total_pixels) * nsep) for img in imgs]
    grid_sizes.insert(0, 0)
    grid_places = grid_sizes.copy()
    for i in range(1, len(grid_sizes)):
        grid_places[i] = grid_places[i - 1] + grid_sizes[i] + img_dis
    # print(grid_places)

    grid = nsep + num_of_imgs * img_dis

    plt.figure(figsize=figsize)
    ax = [''] * num_of_imgs
    if axis == 0:
        gs = GridSpec(1, grid)
        for i in range(num_of_imgs):
            ax[i] = plt.subplot(gs[:, grid_places[i]:grid_places[i + 1] - img_dis])
            ax[i].axis(axis_state)
            ax[i].imshow(imgs[i])
    else:
        gs = GridSpec(grid, 1)
        for i in range(num_of_imgs):
            ax[i] = plt.subplot(gs[grid_places[i]:grid_places[i + 1] - img_dis, :])
            ax[i].axis(axis_state)
            ax[i].imshow(imgs[i])
    plt.show()
