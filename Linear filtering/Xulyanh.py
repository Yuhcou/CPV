import cv2


image = cv2.imread(r'nhieu.png')
khu_nhieu = cv2.medianBlur(image, 3)
khu_nhieu = cv2.medianBlur(khu_nhieu, 3)
# khu_nhieu = cv2.GaussianBlur(khu_nhieu, (5, 5), 1, borderType=cv2.BORDER_REPLICATE)
# dst = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

cv2.imshow('origin', image)
cv2.imshow('convoluted', khu_nhieu)
# cv2.imshow('denoise', dst)
cv2.waitKey(0)
print(image.shape)
