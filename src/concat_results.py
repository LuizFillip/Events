import base as b 
import pandas as pd
import os 
import datetime as dt
import RayleighTaylor as rt
import PlasmaBubbles as pb 

PATH_GAMMA = 'database/gamma/'
PATH_EPB = 'database/epbs/sunset_events2'
PATH_EPB = 'database/epbs/sunset_fresh'
PATH_PRE = 'digisonde/data/PRE/'
PATH_INDEX =  'database/indices/omni_pro2.txt'

def gamma(site = 'saa'):
    
    if site == 'saa':
        path = os.path.join(PATH_GAMMA, f'p_{site}.txt')
        
        df = b.load(path)
        time = dt.time(22, 0)
        df = df.loc[df.index.time == time]    
        df.index = pd.to_datetime(df.index.date)
        
        df= df.loc[~df.index.duplicated()]
        df[['gravity','gamma']] = df[['gravity','gamma']] * 1e3
        return df

    else:
        df = b.load('database/jic_local')
        time = dt.time(1, 0)
        return df
    
   

def epbs(col = -50, 
         geo = False, 
         syear = 2013, 
         eyear = 2023
         ):
    
    # PATH_EPB = 'events_class'
    # PATH_EPB = 'core/data/epb_class'
    PATH_EPB = 'events_class2'
    
    
    df = b.load(PATH_EPB)
    try:
        df = pb.bubble_class(df, typing = 'sunset') 
    except:
        pass

    df.columns = pd.to_numeric(df.columns)
    
    df = df.loc[:, [col]]
    
    df.rename(
        columns = {col: 'epb'}, 
        inplace = True
        )
    idx = geo_index(syear = syear, eyear = eyear)
    
    if geo:
        df = pd.concat([df, idx], axis = 1).dropna()
        
    return df


def interpote_hourly(ey = 2023, es = 2013):
    ds = b.load(PATH_INDEX)[['kp', 'dst']]
    
    ds = ds.loc[(ds.index.year >= es) & 
                (ds.index.year <= ey)]
    
    return  ds.resample('60s').asfreq().interpolate()



def geo_index(
        cols = ['f107a', 'f107', 'kp', 'dst'],
        syear = 2013, 
        eyear = 2023
        ):
    
    ds = b.load(PATH_INDEX)
    
    ds["f107a"] = ds["f107"].rolling(window = 81).mean()
    
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

def load_results(
        site = 'saa', 
        gamma_cols = ['vp', 'gamma'],
        syear = 2013, 
        eyear = 2023
        ):
    
    # i = geo_index(
    #     cols = ['f107a', 'f107', 'kp', 'dst'],
    #     syear = syear, 
    #     eyear = eyear
    #     )
    
    g = b.load('gamma_saa')[gamma_cols]
    g['gamma'] = g['gamma'] * 1e3
    g = gamma(site = site)[gamma_cols]
    
    
    if site == 'saa':
        col_epb = -50
    else:
        col_epb = -80
    
    # g = g.loc[~((g['vp'] > 100) | (g['vp'] < 0))]
        
    e = epbs(col = col_epb, geo = True, 
             syear = syear, eyear = eyear)

    ds = pd.concat([g, e], axis = 1).dropna().sort_index()

    ds['doy'] = ds.index.day_of_year.copy()

    return ds


def local_results(
        year, 
        col_grad = 'L1', 
        col_epb = -80):
    
    df = rt.local_results(
        year, 
        col_grad = 'L1', 
        time = dt.time(1, 0)
        )
            
    ep = epbs(col = col_epb, geo = True)
    
    return pd.concat([df, ep], axis  = 1).dropna()
    


def get_same_length():
    ds1 = load_results('saa')
    ds2 = load_results('jic')
    
    sel_2 = ds1.loc[ds1.index.isin(ds2.index)]
    
    return sel_2.dropna(), ds2.dropna()

