import base as b 
import pandas as pd
import os 
import RayleighTaylor as rt 
import GEO as gg 
import datetime as dt

PATH_GAMMA = 'database/Results/gamma/'
PATH_EPB = 'database/epbs/events_types.txt'
PATH_PRE = 'digisonde/data/PRE/'
PATH_INDEX =  'database/indices/omni_pro.txt'

def gamma(
        site = 'saa', 
        col_g = 'night'
        ):
    
    path = os.path.join(
       PATH_GAMMA,
       f't_{site}.txt'
       )

    df = b.load(path)
    df = df.loc[~(df['night'] > 0.004)]
    df = df * 1e3
    
    return df[col_g]


def epbs(col = -50, class_epb = 'sunset'):

    df = b.load(PATH_EPB)
    df.columns = pd.to_numeric(df.columns)
    
    if class_epb == 'sunset':
        df = df.replace(2, 1)
        df = df.replace((3, 4), (0, 0))
    else:
        df = df.replace((3, 4), (1, 1))
        df = df.replace((2, 1), (0, 0))
    
    cond = (df[col] == 1) | (df[col] == 0)
    ds =  df.loc[cond, [col]]
    
    ds.rename(
        columns = {
            col: 'epb'
            }, 
        inplace = True
        )
    
    return ds




def geo_index():
    
    ds = b.load(PATH_INDEX)
    ds["f107a"] = ds["f107"].rolling(window = 81).mean()
    start = dt.datetime(2013, 1, 1)
    end = dt.datetime(2022, 12, 1)
    ds = b.sel_dates(ds, start, end)
    
    return ds[['f107a', 'f107', 'kp', 'dst']].dropna()

def pre(
        site = 'saa', 
        years = '2013_2021.txt'
        ):
    path = os.path.join(
        PATH_PRE,
        site, 
        years
        )    
    return b.load(path)

def concat_results(
        site = 'saa', 
        col_g = 'night'
        ):
    
    if site == 'saa':
        col_e = -50
    else:
        col_e = -80
    
    g = rt.load_grt(site)

    g = g[['gravity', 'gamma']] * 1e3
    e = epbs(col_e)
    p = pre(site)
    i = geo_index()
    
    ds = pd.concat(
        [g, i, e, p], 
        axis = 1
        ).dropna()
    
    ds.columns.name = gg.sites[site]['name']
    
    ds['doy'] = ds.index.day_of_year.copy()

    
    return ds


