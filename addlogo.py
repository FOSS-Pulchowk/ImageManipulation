# adds logos to all the photos in the working directory and save them in a new folder

import os
from PIL import Image

LOGO_FILENAME = 'logo.png'
MINIMUM_SIZE = 500

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)

# loop over all the files in the working directory
for filename in os.listdir('.'):
    if not (filename.endswith('.jpg') or filename.endswith('JPG') or filename.endswith('.png') or filename.endswith('PNG') or filename == LOGO_FILENAME):
        continue  # skips the logo file

    image = Image.open(filename)
    width, height = image.size

    if width < MINIMUM_SIZE and height < MINIMUM_SIZE:
        continue

    # add logo
    print('adding logo to %s...' % (filename))
    image.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    image.save(os.path.join('withLogo', 'withlogo' + filename))
    print('Logo added to %s' % (filename))
