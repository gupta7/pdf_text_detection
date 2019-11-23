from PIL import Image

im = Image.open('get_pixel.jpg', 'r')

pix_val = list(im.getdata())

for p in pix_val:
        print(p)