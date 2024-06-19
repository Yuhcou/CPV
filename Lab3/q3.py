import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('egg.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray2 = gray[35:270, 87:373]

blur = cv2.GaussianBlur(gray, (11,11), 0)

canny = cv2.Canny(blur, 30, 150, 3)

dilated = cv2.dilate(canny, (1,1), iterations = 2)

(cnt, heirarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(gray, cnt, -1, (0,255,0), 2)


fig, axes = plt.subplots(2, 3, figsize=(10, 7))
for a in range(2):
    for b in range(3):
        axes[a,b].axis('off')
axes[0,0].imshow(image)
axes[0,0]
axes[0,1].imshow(gray, cmap='gray')
axes[0,2].imshow(blur, cmap='gray')
axes[1,0].imshow(canny, cmap='gray')
axes[1,1].imshow(dilated, cmap='gray')
plt.show()