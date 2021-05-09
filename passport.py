# this script can make a 4x6 inches photo
# with the required passport size photos
# that can be printed in .jpg file format

# to run this script in command line, use the format:
# python [destination folder\passport.py] [photo_file.jpg]

import os
import sys
from PIL import Image, ImageDraw

filename = sys.argv[1]
bg_im = Image.new('RGB', (1200, 1800), 'white')
width, height = bg_im.size
os.makedirs('ppsize', exist_ok=True)

# check for a image file
if not (filename.endswith('.png') or filename.endswith('.jpg')):
    print('Please give a valid im file')

im = Image.open(filename)
im = im.resize((350, 400))
imWidth, imHeight = im.size
draw = ImageDraw.Draw(im)
draw.line([(0, 0), (imWidth - 1, 0), (imWidth - 1, imHeight - 1), (0, imHeight - 1), (0, 0)], fill='black')

print('Creating your photo...')

for left in range(37, width - (imWidth + 37), (imWidth + 37)):
    for top in range(35, height - imHeight, (imHeight + 35)):
        bg_im.paste(im, (left, top))

bg_im.save(os.path.join('ppsize', 'ppsize' + filename), dpi=(300, 300))
print('image succesfully created!')
