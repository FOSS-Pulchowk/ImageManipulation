# this script can make a 1200x1800px photo
# with the required passport size photos
# that can be printed

import os
import sys
from PIL import Image

os.chdir('E:\\KADA\python_learn\project24\ImageManipulator')
filename = sys.argv[1]
bg_im = Image.new('RGB', (1200, 1800), 'white')
width, height = bg_im.size
os.makedirs('ppsize', exist_ok=True)

if not (filename.endswith('.png') or filename.endswith('.jpg')):
    print('Please give a valid im file')

im = Image.open(filename)
im = im.resize((350, 400))
imWidth, imHeight = im.size

print('Creating your photo...')

for left in range(37, width - (imWidth + 37), (imWidth + 37)):
    for top in range(35, height - imHeight, (imHeight + 35)):
        bg_im.paste(im, (left, top))

bg_im.save(os.path.join('ppsize', filename))
print('image succesfully created!')
