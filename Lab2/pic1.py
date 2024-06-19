import cv2
from matplotlib import pyplot as plt

image = cv2.imread('1.png', 1)
imageb = image[:,:,0]
imageg = image[:,:,1]
imager = image[:,:,2]
# image = image[:,:,::-1]

image2 = image.copy()
imageb = cv2.equalizeHist(imageb)
imageg = cv2.equalizeHist(imageg)
imager = cv2.equalizeHist(imager)

image2[:,:,0] = imager
image2[:,:,1] = imageg
image2[:,:,2] = imageb


plt.subplot(121), plt.imshow(image[:,:,::-1])
plt.axis('off')
plt.subplot(122), plt.imshow(image2)
plt.axis('off')

plt.show()