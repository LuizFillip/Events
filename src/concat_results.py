import base as b 
import pandas as pd
import os 
import datetime as dt


PATH_GAMMA = 'database/gamma/'
PATH_EPB = 'database/epbs/events_types.txt'
PATH_EPB = 'database/epbs/events_class.txt'
PATH_EPB = 'database/epbs/sunset_events.txt'

PATH_PRE = 'digisonde/data/PRE/'
PATH_INDEX =  'database/indices/omni_pro.txt'

def gamma(site = 'saa'):
    
    path = os.path.join(
       PATH_GAMMA,
       f'p_{site}.txt'
       )
    
    df = b.load(path)
    df = df.loc[df.index.time == dt.time(22, 0)]    
    df.index = pd.to_datetime(df.index.date)

    return df


def epbs2(
        col = -50, 
        class_epb = 'sunset',
        geo = False
        ):

    df = b.load(PATH_EPB)
    df.columns = pd.to_numeric(df.columns)
    
    
    if geo:
        df = pd.concat(
            [df, geo_index()], 
            axis = 1
            ).dropna()
        
    if class_epb  == 'sunset':
        
        # df = df.replace((2, 3, 4), (0, 0, 0))
        df = df.replace(
            ( class_epb , 
              'no_epb', 'midnight'), (1, 0, 0)
            )
    elif class_epb == 'midnight':
        df = df.replace(
            ( class_epb ,
              'no_epb', 'sunset'), (1, 0, 0)
            )
        
    else:
        return df
     
    if col is not None:
        df = df.loc[:, [col]]
        df.rename(
            columns = {
                col: 'epb'
                }, 
            inplace = True
            )

    return df
    

def epbs(col = -50, geo = False):
    
    df = b.load(PATH_EPB)
    df.columns = pd.to_numeric(df.columns)
    
    df = df.loc[:, [col]]
    df.rename(
        columns = {
            col: 'epb'
            }, 
        inplace = True
        )
    if geo:
        df = pd.concat([df, geo_index()], 
            axis = 1
            ).dropna()
    return df


def geo_index(
        cols = ['f107a', 'f107', 'kp', 'dst'],
        syear = 2013, 
        eyear = 2022
        ):
    
    ds = b.load(PATH_INDEX)
    
    ds["f107a"] = ds["f107"].rolling(
        window = 81
        ).mean()
    
    start = dt.datetime(syear, 1, 1)
    end = dt.datetime(eyear, 12, 31)
    
    ds = b.sel_dates(ds, start, end)
    
    return ds[cols].dropna()

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

def concat_results(site = 'saa'):
    
    if site == 'saa':
        col_epb = -50
    else:
        col_epb = -80
    
    i = geo_index()
    g = gamma(site)[['gravity', 'vp', 'gamma']]
    e = epbs(col = col_epb)


    ds = pd.concat(
        [g, i, e], 
        axis = 1).dropna().sort_index()

    ds[['gravity', 'gamma']] = ds[
        ['gravity', 'gamma']] * 1e3

    ds['doy'] = ds.index.day_of_year.copy()

    return ds



# site = 'saa'


# df = concat_results()

# df
