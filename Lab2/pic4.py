import cv2
import numpy as np
import matplotlib.pyplot as plt

org = cv2.imread('4.jfif', 0)

tranformed = np.fft.fft2(org)
shifted = np.fft.fftshift(tranformed)
magnitude_spectrum = 20*np.log(np.abs(shifted))

plt.subplot(121)
plt.imshow(org, cmap = 'gray')

fixed = shifted.copy()
r = 7
fixed[250 - r:250 + r, 97- r: 97 +r] = np.median(fixed[245:255, 92: 102])
fixed[190 - r:190 + r, 97- r: 97 +r] = np.median(fixed[185:195, 92: 102])
fixed[70 - r:70 + r, 97- r: 97 +r] = np.median(fixed[63:73, 92: 102])
fixed[9 - r: 9 + r, 97- r: 97 +r] = np.median(fixed[4:14, 92: 102])

magnitude_spectrum_fixed = 20*np.log(np.abs(fixed))

f_ishift = np.fft.ifftshift(fixed)
img_back = np.fft.ifft2(f_ishift)
img_back = np.real(img_back).astype('uint8')

plt.subplot(122)
plt.imshow(img_back, cmap = 'gray')
plt.show()