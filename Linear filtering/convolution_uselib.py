import cv2
import numpy as np

# Load an image
image = cv2.imread(r'C:\Users\Huy\PycharmProjects\CPV\canhchua1.jpg')

# Define a kernel (you can define any kernel as per your requirement)
kernel_sharpen = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
kernel_blur = np.ones((3, 3))/9
kernel_edge = np.array([[-1, -1, -1],
                   [-1, 8,-1],
                   [-1, -1, -1]])

# Convolve image with kernel
convolved_image = cv2.filter2D(image, -1, kernel_edge)

# Save the convolved image
cv2.imshow('original', image)
cv2.imshow('convoluted', convolved_image)
cv2.waitKey(0)