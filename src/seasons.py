import base as b 
import datetime as dt 
import pandas as pd 
from events import probability_distribuition

def sep_seasons(ds, year = 2013):
    
    ds = ds.loc[ds.index.year == year]
    
    summer = ds.loc[
        (ds.index < dt.datetime(year, 3, 21))
        ]
    
    fall = ds.loc[
        (ds.index > dt.datetime(year, 3, 21) ) &
        (ds.index < dt.datetime(year, 6, 21))
        ]
    
    winter = ds.loc[
        (ds.index > dt.datetime(year, 6, 21)) &
        (ds.index < dt.datetime(year, 9, 23))
        ]
    
    spring = ds.loc[
        (ds.index > 
         dt.datetime(year, 9, 23)) &               
        (ds.index < 
         dt.datetime(year, 12, 21)) 
                  ]
    
    return [spring, fall, winter, summer]


def get_doy(dn):

    return dn.timetuple().tm_yday





def summer(df):
    start =  get_doy(dt.date(2013, 12, 21))
    end = get_doy(dt.date(2013, 3, 21))
    
    cond =  (df['doy'] > start) | (df['doy'] <= end)
    return df.loc[cond]


def fall(df):
    start = get_doy(dt.date(2013, 3, 21))
    end = get_doy(dt.date(2013, 6, 21))
    
    cond = (df['doy'] > start) & (df['doy'] <= end)
    return df.loc[cond]


def winter(df):
    start = get_doy(dt.date(2013, 6, 21))
    end = get_doy(dt.date(2013, 9, 23))
    
    cond = (df['doy'] > start) & (df['doy'] <= end)
    return df.loc[cond]


def spring(df):
    start = get_doy(dt.date(2013, 9, 23))
    end = get_doy(dt.date(2013,  12, 21))
    
    cond = (df['doy'] > start) & (df['doy'] <= end)
    return df.loc[cond]


import matplotlib.pyplot as plt 


fig, ax = plt.subplots(
    dpi = 300,
    ncols = 2, 
    nrows = 2,
    sharex = True,
    sharey = True,
    figsize = (10, 10)
    )

plt.subplots_adjust(wspace = 0.1)

df = b.load('all_results.txt')

df = df.loc[df['kp_max'] > 4]



df['doy'] = df.index.day_of_year 
seasons = [summer(df), fall(df), winter(df), spring(df)]
names = ['summer', 'fall', 'winter', 'spring']
for i, ax  in enumerate(ax.flat):

    ds = probability_distribuition(
            seasons[i],
            step = 0.2, 
            col_gama = 'all',
            col_epbs = 'epb'
            )
    
    ax.plot(ds['start'], ds['rate'])
    ax.set(xlim = [0, 3], 
           ylim = [-20, 120],
           title = names[i],
           )
    
    if i >= 2:
        ax.set(xlabel = '$\\gamma_{FT}~\\times 10^{-3}$ ($s^{-1}$)')
        
    if i == 0 or i == 2:
        ax.set(ylabel = 'EPBs probability \noccurrence ($\\%$)')
    
    
fig.suptitle('disturbed days ($kp > 4$)')
