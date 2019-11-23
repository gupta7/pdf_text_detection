import cv2
import numpy as np


x = 'test_image.jpg'

img = cv2.imread(x)
print(img.shape)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#--- performing Otsu threshold ---
ret,thresh1 = cv2.threshold(gray, 0, 255,cv2.THRESH_OTSU|cv2.THRESH_BINARY_INV)
cv2.imshow('thresh1', thresh1)
cv2.imwrite('thresh1.jpg', thresh1)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 3))
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
cv2.imshow('dilation', dilation)

cv2.imwrite('dilate1.jpg', dilation)
_, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

im2 = img.copy()
rows, cols, slice = img.shape

for cnt in contours:
    count1=0
    count2=0
    x, y, w, h = cv2.boundingRect(cnt)
    for i in range(x,x+h):
        for j in range(y,y+w):
            if(i<rows and j<cols):
                pixel = img[i,j]
                if(pixel[0]>150 and pixel[0]<=255 and pixel[1]>100 and pixel[1]<=200 and pixel[2]<11 and pixel[2]>=0):
                    #cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    count1 = count1+1
                    #break
                else:
                    count2 = count2+1
    if(count1>count2):
        cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('final', im2)
cv2.imwrite('image3.jpg', im2)
#cv2.waitKey()