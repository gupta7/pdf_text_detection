import numpy as np
import argparse
import cv2

image = cv2.imread('test_image.jpg')

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
    cv2.imshow("images", np.hstack([image, output]))
    cv2.imwrite("test.jpg",output)
    #cv2.waitKey(0)