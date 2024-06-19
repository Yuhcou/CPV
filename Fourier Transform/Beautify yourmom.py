import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('yourmom.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.abs(fshift))

plt.subplot(221), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# plt.show()

rows, cols = img.shape

crow, ccol = rows // 2, cols // 2
fshift[crow - 13:crow - 5, ccol - 13:ccol - 5] = 800
fshift[crow + 5:crow + 13, ccol + 5:ccol + 13] = 800
fshift[crow - 21:crow - 13, ccol - 21:ccol - 13] = 800
fshift[crow + 13:crow + 21, ccol + 13:ccol + 21] = 800
fshift[crow - 29:crow - 21, ccol - 29:ccol - 21] = 800
fshift[crow + 21:crow + 29, ccol + 21:ccol + 29] = 800
fshift[crow - 37:crow - 29, ccol - 37:ccol - 29] = 800
fshift[crow + 29:crow + 37, ccol + 29:ccol + 37] = 800
magnitude_spectrum = 20 * np.log(np.abs(fshift))
print(fshift.min(), fshift.max())
# print(magnitude_spectrum[])

plt.subplot(223), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum2'), plt.xticks([]), plt.yticks([])

f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.real(img_back)

plt.subplot(224), plt.imshow(img_back, cmap='gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])

# plt.show()

# print(type(img_back))
# print(np.floor(np.abs(img_back)))
# print(img_back.max())
# print(type(img[0][0]))
# print(img)
img_back = np.floor(np.abs(img_back)).astype(np.uint8)
khu_nhieu = cv.GaussianBlur(img_back,(5,5),0)
plt.subplot(221), plt.imshow(khu_nhieu, cmap='gray')

kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharpened_image = cv.filter2D(khu_nhieu, -1, kernel)
plt.subplot(222), plt.imshow(sharpened_image, cmap='gray')
plt.show()
