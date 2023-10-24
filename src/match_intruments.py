import os
import imager as im 
import datetime as dt 
import digisonde as dg

sky_dir = 'imager/img/CA_2013_0114/'


fn_sky = 'O6_CA_20130114_224619.png'


def get_closest_iono(fn_sky):
    
    iono_dir = 'database/iono/20130114/'

        
    sky_dt = im.imager_fname(fn_sky).datetime
    
    iono_files = sorted(
        [dg.ionosonde_fname(fn) 
         for fn in os.listdir(iono_dir)]
        )
    
    dn = min(
        iono_files, 
        key = lambda x: abs(x - sky_dt)
        )
        
    return dn.strftime("FZA0M_%Y%m%d(%j)%H%M%S.PNG")


