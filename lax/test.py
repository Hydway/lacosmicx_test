import CPF_read as cpf
import seaborn as sns
import matplotlib.pyplot as plt
import  _lacosmicx as  lax
from astropy.io import fits

fits_file = fits.open('/home/hydway/Git/lacosmicx/data2/twoobjects/N1821824857_2.fits')
im = fits_file[0].data
CPF_file = '/home/hydway/Git/lacosmicx/data2/twoobjects/N1821824857_2_gaia2.CPF'
df = cpf.CPF_read(CPF_file)
x = map(eval, df['cen_x'])
y = map(eval, df['cen_y'])

# sns.scatterplot(df['cen_x'],df['cen_y'])
# plt.show()

im_clean = lax.lacosmicx(im)
# misc.imsave('9.tif', im_clean[1])
print(im_clean)

plt.figure(1)
plt.imshow(im, cmap='gray')
plt.scatter(x,y,alpha=0.4)
# plt.imshow(im_clean[1], cmap='gray')
plt.figure(2)
plt.imshow(im, cmap="gray")
plt.figure(3)
plt.scatter(x,y,alpha=0.4)
plt.show()
print('Done')


