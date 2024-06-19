import cv2
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread('2.png', 1)
image = image[:,:,::-1]
khu_nhieu = cv2.medianBlur(image, 3)
kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
sharpened_image = cv2.filter2D(khu_nhieu, -1, kernel)


plt.subplot(121), plt.imshow(image)
plt.axis('off')
plt.subplot(122), plt.imshow(khu_nhieu)
plt.axis('off')

plt.show()