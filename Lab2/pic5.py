import cv2
from matplotlib import pyplot as plt
import numpy as np


image = cv2.imread(r'5.jfif')
image = image[:,:,::-1]
khu_nhieu = cv2.medianBlur(image, 3)
# khu_nhieu = cv2.medianBlur(khu_nhieu, 3)

plt.subplot(121), plt.imshow(image, cmap='grey')
plt.axis('off')
plt.subplot(122), plt.imshow(khu_nhieu, cmap='grey')
plt.axis('off')
plt.show()