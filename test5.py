import cv2
import numpy as np

x='bar1.png'
y = 'test_image.jpg'

img = cv2.imread(x)

img1 = cv2.imread(y)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#--- performing Otsu threshold ---
ret,thresh1 = cv2.threshold(gray, 0, 255,cv2.THRESH_OTSU|cv2.THRESH_BINARY_INV)
cv2.imshow('thresh1', thresh1)
cv2.imwrite('thresh5.jpg', thresh1)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 3))
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
cv2.imshow('dilation', dilation)

cv2.imwrite('dilate5.jpg', dilation)
_, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

im2 = img1.copy()
for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        if(w>100 and h<55):
            print(x, y)
            cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('final', im2)
cv2.imwrite('image7.jpg', im2)
#cv2.waitKey()