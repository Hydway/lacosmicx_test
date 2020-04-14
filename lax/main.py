import DB_read as db
import sys
import matplotlib.pyplot as plt
import  _lacosmicx as  lax
from astropy.io import fits
import bgclean as bc


def echoMsg(level, msg):
    if level == 'Info':
        print '[Info] %s' % msg
    elif level == 'Error':
        print '[Error] %s' % msg

# fits_file = fits.open('/home/hydway/Git/lacosmicx/data2/twoobjects/N1821824893_1.fits')
# CPF_file = '/home/hydway/Git/lacosmicx/data2/twoobjects/N1821824893_1_gaia2.CPF'

def main(fits_file, DB_file, DB_model):
    im = fits_file[0].data
    if DB_model == "CPF":
        df = db.CPF_read(DB_file)
    else:
        df = db.QMPF_read(DB_file)
    x = map(eval, df['cen_x'])
    y = map(eval, df['cen_y'])

    im_clean = lax.lacosmicx(im)
    print(im_clean)
    bg_clean = bc.bgclean(7, im, x, y)

    plt.figure(1)
    plt.imshow(im, cmap='gray')
    plt.scatter(y,x,alpha=0.4)
    # plt.scatter(400,0)
    # plt.imshow(im_clean[1], cmap='gray')
    plt.figure(2)
    plt.imshow(im, cmap="gray")
    plt.figure(3)
    plt.scatter(x,y,alpha=0.4)
    plt.figure(4)
    # plt.imshow(bg_clean)
    plt.show()
    print('Done')

if __name__ == '__main__':
    try:
        fits_file = fits.open(raw_input('Please input fits_image file path : '))
    except Exception as e:
        echoMsg('Error', e)
        sys.exit()
    try:
        DB_model = raw_input('Please input DB file type (CPF or QMPF) : ')
        if DB_model == 'CPF':
            CPF_file = raw_input('Please input CPF file path : ')
            DB_file = CPF_file
        elif DB_model == 'QMPF':
            QMPF_file = raw_input('Please input QMPF file path : ')
            DB_file = QMPF_file
        else:
            echoMsg("Error", "type error")
    except Exception as e:
        echoMsg('Error', e)
        sys.exit()
    main(fits_file, DB_file, DB_model)