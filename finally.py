import cv2
import numpy as np
import numpy as np
import argparse
import cv2

image = cv2.imread('page_2.jpg')

height = np.size(image, 0)
width = np.size(image, 1)
print(width,height)

boundaries = [
	([150, 100, 0], [255, 200, 10])
]

for (lower, upper) in boundaries:
    print(type(lower),upper)
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    print(type(lower), upper)
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

            pixels[i,j] = (255, 255 ,255)

img.save('test/bar.png')

x='test/bar.png'

img = cv2.imread(x)

img1 = image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('test/gray.jpg', gray)
#--- performing Otsu threshold ---
#ret,thresh1 = cv2.threshold(gray, 0, 255,cv2.THRESH_OTSU|cv2.THRESH_BINARY_INV)
ret,thresh1 = cv2.threshold(gray, 120, 255,cv2.THRESH_BINARY_INV)
#cv2.imshow('thresh1', thresh1)
cv2.imwrite('test/thresh5.jpg', thresh1)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (int((60*4135)/width), int((45*5848)/height)))
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
#cv2.imshow('dilation', dilation)

cv2.imwrite('test/dilate5.jpg', dilation)
_, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

list=[]
headings=[]
width_bound=[((100*width)/1500),width]
height_bound=[0,((60)*height/2339)]
im2 = img1.copy()
for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        if(w>((100*width)/1500) and h<((60)*height/2339)):
            print(w,h)
            print(x, y)
         #   list.append((x,y,w,h))
            headings.append((x,y,w,h))
            #print(list)
            cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 6)

headings.sort(key = lambda x: x[0])
col1head=[]
col2head=[]
col1head.append(headings[0])
for i in range(1,len(headings)):
    if(headings[i][0] < (col1head[0][0]+20)):
        col1head.append(headings[i])
    else:
        col2head.append(headings[i])

col1head.sort(key = lambda x: x[1])
col2head.sort(key = lambda x: x[1])

print(col1head)
print(col2head)

x1 = col1head[0][0]
x2 = col2head[0][0]

col1cont = []
col2cont = []

cv2.rectangle(im2, (col1head[0][0]-10, 50), ((x2 - 20), (col1head[0][1] - 70)), (0, 0, 255), 4)

for i in range(0,len(col1head)-1):
    col1cont.append((col1head[i][0],col1head[i][1]+col1head[i][3],(x2-20),(col1head[i+1][1]-20)))
    cv2.rectangle(im2, (col1head[i][0], col1head[i][1]), ((x2-20), (col1head[i+1][1]-20)), (0, 0, 255), 4)
    cv2.rectangle(im2, (col1cont[i][0], col1cont[i][1]), (col1cont[i][2], col1cont[i][3]), (255, 0, 0), 4)
#i=i+1
col1cont.append((col1head[len(col1head)-1][0], col1head[len(col1head)-1][1]+col1head[len(col1head)-1][3], x2-20, height-20))
cv2.rectangle(im2, (col1head[len(col1head)-1][0], col1head[len(col1head)-1][1]), ((x2-20), (height-20)), (0, 0, 255), 4)
cv2.rectangle(im2, (col1cont[len(col1cont)-1][0], col1cont[len(col1cont)-1][1]), (col1cont[len(col1cont)-1][2], col1cont[len(col1cont)-1][3]), (255, 0, 0), 4)

for i in range(0,len(col2head)-1):
    col2cont.append((col2head[i][0],col2head[i][1]+col2head[i][3],(width-20),(col2head[i+1][1]-20)))
    cv2.rectangle(im2, (col2head[i][0], col2head[i][1]), ((width-20), (col2head[i+1][1]-20)), (0, 0, 255), 4)
    cv2.rectangle(im2, (col2cont[i][0], col2cont[i][1]), (col2cont[i][2], col2cont[i][3]), (255, 0, 0), 4)
#i=i+1
#i=0
col2cont.append((col2head[len(col2head)-1][0], col2head[len(col2head)-1][1]+col2head[len(col2head)-1][3], width-20, height-20))

cv2.rectangle(im2, (col2cont[len(col2cont)-1][0], col2cont[len(col2cont)-1][1]), (col2cont[len(col2cont)-1][2], col2cont[len(col2cont)-1][3]), (255, 0, 0), 4)

cv2.rectangle(im2, (col2head[len(col2head)-1][0], col2head[len(col2head)-1][1]), ((width-20),(height-20)), (0, 0, 255), 4)

#cv2.imshow('final', im2)
cv2.imwrite('test/image7.jpg', im2)

#cv2.waitKey()
