import cv2
import numpy as np

# Reading the input image
img = cv2.imread('page_3.jpg')
image = cv2.imread('page_3.jpg')
height = np.size(image, 0)
width = np.size(image, 1)
print(height,width)
# Taking a matrix of size 5 as the kernel
kernel = np.ones((8, 8), np.uint8)

# The first parameter is the original image,
# kernel is the matrix with which image is
# convolved and third parameter is the number
# of iterations, which will determine how much
# you want to erode/dilate a given image.

img_dilation = cv2.dilate(img, kernel, iterations=1)
img_erosion = cv2.erode(img_dilation, kernel, iterations=1)

#cv2.imshow('Input', img)
#cv2.imshow('Erosion', img_erosion)
#cv2.imshow('Dilation', img_dilation)

cv2.imwrite('test4/Input.jpg', img)
cv2.imwrite('test4/Erosion.jpg', img_erosion)
cv2.imwrite('test4/Dilation.jpg', img_dilation)

gray = cv2.cvtColor(img_erosion, cv2.COLOR_BGR2GRAY)
cv2.imwrite('test4/gray.jpg', gray)
#--- performing Otsu threshold ---
#ret,thresh1 = cv2.threshold(gray, 0, 255,cv2.THRESH_OTSU|cv2.THRESH_BINARY_INV)
ret,thresh1 = cv2.threshold(gray, 120, 255,cv2.THRESH_BINARY_INV)
#cv2.imshow('thresh1', thresh1)
cv2.imwrite('test4/thresh5.jpg', thresh1)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (int((90*4135)/width), int((45*5848)/height)))
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
#cv2.imshow('dilation', dilation)

cv2.imwrite('test4/dilate5.jpg', dilation)
_, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)


        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 6)

cv2.imwrite('test4/final.jpg', img)
#cv2.waitKey(0)