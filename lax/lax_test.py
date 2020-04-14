import  _lacosmicx as  lax
from astropy.io import fits
import matplotlib.pyplot as plt
from scipy import misc

data = fits.open('/home/hydway/Git/lacosmicx/data2/twoobjects/N1821824857_2.fits')
im = data[0].data

im_clean = lax.lacosmicx(im, sigclip=4.5, objlim=10)
# misc.imsave('9.tif', im_clean[1])
print(im_clean[1])

# plt.figure(1)
# plt.imshow(im, cmap='gray')
# plt.figure(2)
# plt.imshow(im_clean[1], cmap='gray')
# plt.show()
# print im_clean[1].shape[0]
# print im_clean[1].shape[1]
# print('Done')