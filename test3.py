import cv2
import numpy as np

image = cv2.imread('bar1.png')

image1 = cv2.imread('test_image.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7,7), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
dilate = cv2.dilate(thresh, kernel, iterations=4)

cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(image1, (x, y), (x + w, y + h), (36,255,12), 2)

#cv2.imshow('thresh', thresh)
#cv2.imshow('dilate', dilate)
#cv2.imshow('image', image)
cv2.imwrite('image4.jpg', image1)
cv2.imwrite('thresh4.jpg', thresh)
cv2.imwrite('dilate4.jpg', dilate)
#cv2.waitKey()