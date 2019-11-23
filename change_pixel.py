from PIL import Image

img = Image.open("test.jpg")
pixels = img.load() # create the pixel map

for i in range(img.size[0]): # for every pixel:
    for j in range(img.size[1]):
        if (pixels[i,j][0]<=50 and pixels[i,j][1]<=50 and pixels[i,j][2]<=50 ):
            # change to black if not red
            pixels[i,j] = (255, 255 ,255)

img.save('bar1.png')