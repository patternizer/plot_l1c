# quick routine to import PNGs and produce a panel plot

from PIL import Image, ImageTk
import numpy as np
import os
import glob
import matplotlib.pyplot as plt

imageFolderPath = os.getcwd()
imagePath = glob.glob(imageFolderPath + '/*.png') 
im_array = np.array( [np.array(Image.open(img).convert('L'), 'f') for img in imagePath] )

maxcol = int(np.floor(len(imagePath)/2))
fig, ax = plt.subplots(2,maxcol, sharex=True, sharey=True)
for idx in range(len(imagePath)-1):

    imageFile = imagePath[idx]
#    im = Image.open(imageFile)
    im = im_array[idx,:,:]
    plt.subplot(2,maxcol,idx+1, frameon=False)
    plt.imshow(im)
    plt.axis('off')
    
plt.tight_layout()
plt.savefig('test.png')

print('** END')
