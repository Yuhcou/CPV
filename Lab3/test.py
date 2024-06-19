import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('coin.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray2 = gray[35:270, 87:373]

blur = cv2.GaussianBlur(gray2, (11,11), 0)

canny = cv2.Canny(blur, 30, 150, 3)

dilated = cv2.dilate(canny, (1,1), iterations = 2)

(cnt, heirarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(gray2, cnt, -1, (0,255,0), 2)

print('Coins in the image: ', len(cnt))
areas = list(map(cv2.contourArea, cnt))
nickels = 0
for i in areas:
    if i > 2200:
        nickels += 1
print('Nickles: ' + str(nickels) + '   Dime: ' + str(len(cnt)-nickels))

for i, cont in enumerate(cnt):
    x, y, w, h = cv2.boundingRect(cont)

    X = x + int(w/2)-10
    Y = y + int(h/2)

    area = cv2.contourArea(cont)
    coin_type = 'Nickel' if area > 2200 else 'Dime'

    gray2 = cv2.putText(img=gray2, text=coin_type, org=(X, Y), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.3, color=(0,255,0))

plt.imshow(gray2, cmap='grey')
plt.axis('off')
plt.show()