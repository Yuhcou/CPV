"""
Multiplication and addition with a constant
Multiplicative gain -Superposition principle:
Dyadic (two-input) operator is the linear blend operator
Invert the gamma mapping applied by the sensor"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


def mul_add(image, a, b):
    img = image.copy()
    img = cv2.multiply(img, a)
    img = cv2.add(img, b)
    return img


def dyadic(image1, image2, alpha=0.5):
    img1 = image1.copy()
    img2 = image2.copy()
    alpha = 0.5
    blended = cv2.addWeighted(img1, 1-alpha, img2, alpha, 0)
    return blended


def adjust_gamma(image, gamma=1.0):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)


image1 = cv2.imread('pig.jpg', 1)
image1 = cv2.resize(image1, (1200, image1.shape[0]*1200//image1.shape[1]))[:700, :]
# cv2.imshow('before1', image1)

image2 = cv2.imread('nunu.jpg', 1)
image2 = cv2.resize(image2, (1200, image2.shape[0]*1200//image2.shape[1]))[:700, :]
# cv2.imshow('before2', image2)

# print(image2.shape)
# grey_img = image2.copy()
# params = [0.0722, 0.7152, 0.216]
# greyify = np.sum(np.array(grey_img[:,:,])*params, axis=2)
# grey_img[:,:,] = greyify.reshape(greyify.shape + (1,))
# cv2.imshow('test', grey_img)
#
# grey_img = image2.copy()
# params = [0.333, 0.333, 0.333]
# greyify = np.sum(np.array(grey_img[:,:,])*params, axis=2)
# grey_img[:,:,] = greyify.reshape(greyify.shape + (1,))
# cv2.imshow('test2', grey_img)



# out_image = mul_add(image2, 1, 50)
cv2.imwrite('mul_add.jpg', mul_add(image1, 1, 50))
# out_image = dyadic(image1, image2, alpha=0.5)
cv2.imwrite('dyadic.jpg', dyadic(image1, image2, alpha=0.5))
out_image = adjust_gamma(image1, gamma=2)
# cv2.imshow('after', out_image)
cv2.imwrite('adjust_gamma.jpg', adjust_gamma(image1, gamma=2))

cv2.waitKey(0)
