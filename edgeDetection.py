# this is a python implementetion of the sobel algorithm
# for edge detection in digital image processing

import sys
from PIL import Image
import math

filename = sys.argv[1]
image = Image.open(filename)
width, height = image.size

im1 = Image.new('RGB', (width, height), 'white')

print('Detecting edges...')

for i in range(1, width - 1):
    for j in range(1, height - 1):

        # Gx and Gy are inatilized to zero for every pixel
        Gx = 0
        Gy = 0

        # for the top-left pixel
        pixel = image.getpixel((i - 1, j - 1))
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]

        Gx += -(red + green + blue)
        Gy += (red + green + blue)

        # for the mid-left pixel
        pixel = image.getpixel((i, j - 1))
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]

        Gx += -2 * (red + green + blue)

        # for the low-left pixel
        pixel = image.getpixel((i + 1, j - 1))
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]

        Gx += -(red + green + blue)
        Gy += -(red + green + blue)

        # for the top-mid pixel
        pixel = image.getpixel((i - 1, j))
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]

        Gy += 2 * (red + green + blue)

        # for the mid-mid pixel
        pixel = image.getpixel((i, j))
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]

        # for the mid-low pixel
        pixel = image.getpixel((i + 1, j))
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]

        Gy += -2 * (red + green + blue)

        # for the top-right pixel
        pixel = image.getpixel((i - 1, j + 1))
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]

        Gx += (red + green + blue)
        Gy += (red + green + blue)

        # for the mid-right pixel
        pixel = image.getpixel((i, j + 1))
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]

        Gx += 2 * (red + green + blue)

        # for the low-right pixel
        pixel = image.getpixel((i + 1, j + 1))
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]

        Gx += (red + green + blue)
        Gy += -(red + green + blue)

        # total gradient
        G = math.sqrt((Gx * Gx) + (Gy * Gy))

        # normalise the total gradient to range 0 to 255
        G = G / 4328 * 255
        G = int(G)

        # Draw gradient i edge image
        im1.putpixel((i, j), (G, G, G))

print('Edge detection completed')
im1.save('edge ' + filename)
