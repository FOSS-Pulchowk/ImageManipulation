# this is a python implementation of Median Filter for the
# removal of Salt and Pepper noise in an image

# to run this script in command line, use the format:
# python [destination folder\medianFilter.py] [photo_file.jpg]

import sys
from PIL import Image

filename = sys.argv[1]
image = Image.open(filename)
width, height = image.size

neighbours = [(0, 0)] * 9

newIm = Image.new('RGB', (width, height), 'white')

print('Processing...')

for i in range(1, width - 1):
    for j in range(1, height - 1):
        neighbours[0] = image.getpixel((i - 1, j - 1))
        neighbours[1] = image.getpixel((i - 1, j))
        neighbours[2] = image.getpixel((i - 1, j + 1))
        neighbours[3] = image.getpixel((i, j - 1))
        neighbours[4] = image.getpixel((i, j))
        neighbours[5] = image.getpixel((i, j + 1))
        neighbours[6] = image.getpixel((i + 1, j - 1))
        neighbours[7] = image.getpixel((i + 1, j))
        neighbours[8] = image.getpixel((i + 1, j + 1))

        neighbours.sort()
        # takes the median value of the neighbour pixels and replaces the (i,j) pixel with the median value
        newIm.putpixel((i, j), (neighbours[4]))

print('Noise removed')

newIm.save('median ' + filename)
