# this script converts a color image to grayscale image

import sys
from PIL import Image

filename = sys.argv[1]
numberOfShades = int(sys.argv[2])
image = Image.open(filename)
width, height = image.size

im1 = Image.new('RGB', (width, height), 'white')
print('Converting image to grayscale')

FACTOR = int(255 / (numberOfShades - 1))

for x in range(0, width):
    for y in range(0, height):
        pixel = image.getpixel((x, y))
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]

        average = ((red + green + blue) / 3)

        gray = int((average / FACTOR) + 0.5) * FACTOR
        im1.putpixel((x, y), (gray, gray, gray))

print('Image succesfully converted')
im1.save('grayscale_' + str(numberOfShades) + '_' + filename)
