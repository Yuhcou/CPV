######################### SNAKES MODEL
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.filters import gaussian
from skimage.segmentation import active_contour
import cv2

# Load the image
img = cv2.imread('canhchua1.jpg')
# Convert the image from BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Convert the image to grayscale
img_gray = rgb2gray(img_rgb)

# Define initial contour as a circle
s = np.linspace(0, 2 * np.pi, 400)
r = img_gray.shape[0] / 2 + 300 * np.sin(s)  # 100 * 3 for scaling
c = img_gray.shape[1] / 2 + 300 * np.cos(s)  # 100 * 3 for scaling
init = np.array([r, c]).T

# Display the initial contour
# plt.figure(figsize=(8, 8))
# plt.imshow(img_gray, cmap='gray')
# plt.plot(init[:, 1], init[:, 0], '--r', lw=3)
# plt.title('Initial Contour')
# plt.axis('off')
# plt.show()

# Number of iterations for the active contour model
max_num_iter_values = [5, 20, 40, 60, 80, 100, 150, 500]

# Create subplots
fig, axs = plt.subplots(4, 2, figsize=(14, 28))  # 4 rows and 2 columns

for i, max_num_iter in enumerate(max_num_iter_values):
    # Apply the active contour model
    snake = active_contour(gaussian(img_gray, 3, preserve_range=False), init, alpha=0.015, beta=10, gamma=0.001,
                           max_num_iter=max_num_iter)

    # Plot the results
    ax = axs[i // 2, i % 2]
    ax.imshow(img_rgb)
    ax.plot(init[:, 1], init[:, 0], '--r', lw=3, label='Initial Contour')
    ax.plot(snake[:, 1], snake[:, 0], '-b', lw=3, label='Active Contour')
    ax.set_title('Number of Iterations = {}'.format(max_num_iter))
    ax.set_xticks([]), ax.set_yticks([])
    ax.axis([0, img.shape[1], img.shape[0], 0])

# Hide the empty subplot if there are any
if len(max_num_iter_values) % 2 != 0:
    fig.delaxes(axs[-1, -1])

plt.tight_layout()
plt.show()
