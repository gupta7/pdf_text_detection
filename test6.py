import cv2
import numpy as np
import numpy as np
import argparse
import cv2

image = cv2.imread('page_1.jpg')

height = np.size(image, 0)
width = np.size(image, 1)
print(width,height)

boundaries = [
	([150, 100, 0], [255, 200, 10])
]

i=0
for (lower, upper) in boundaries:
    i=i+1
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)

    # show the images
    #cv2.imshow("images", np.hstack([image, output]))
    cv2.imwrite("test/test.jpg",output)
    #cv2.waitKey(0)
from PIL import Image

img = Image.open("test/test.jpg")
pixels = img.load() # create the pixel map

for i in range(img.size[0]): # for every pixel:
    for j in range(img.size[1]):
        if (pixels[i,j][0]<=50 and pixels[i,j][1]<=50 and pixels[i,j][2]<=50 ):
            # change to black if not red
            pixels[i,j] = (255, 255 ,255)

img.save('test/bar.png')

x='test/bar.png'
y = 'test_image.jpg'

img = cv2.imread(x)

img1 = cv2.imread(y)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('test/gray.jpg', gray)
#--- performing Otsu threshold ---
#ret,thresh1 = cv2.threshold(gray, 0, 255,cv2.THRESH_OTSU|cv2.THRESH_BINARY_INV)
ret,thresh1 = cv2.threshold(gray, 120, 255,cv2.THRESH_BINARY_INV)
cv2.imshow('thresh1', thresh1)
cv2.imwrite('test/thresh5.jpg', thresh1)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 9))
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
cv2.imshow('dilation', dilation)

cv2.imwrite('test/dilate5.jpg', dilation)
_, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

list=[]
im2 = img1.copy()
for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        if(w>((100*width)/1654) and h<((55)*height/2339)):
      #      print(w,h)
            print(x, y)
            list.append((x,y))
            #print(list)
        cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imwrite('test/image7.jpg', im2)

#cv2.waitKey()
