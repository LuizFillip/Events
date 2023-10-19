import base as b 
import pandas as pd
import os 
from geophysical_indices import INDEX_PATH
import GEO as gg 


PATH_GAMMA = 'database/Results/gamma/'
PATH_EPB = 'database/epbs/events_types.txt'
PATH_PRE = 'digisonde/data/PRE/'


def gamma(site = 'saa'):
    
    path = os.path.join(
       PATH_GAMMA,
       f't_{site}.txt'
       )

    df = b.load(path)
    df = df.loc[~(df['night'] > 0.004)]
    df = df * 1e3
    return df['night']


def epbs(col = -50):

    df = b.load(PATH_EPB)
    df.columns = pd.to_numeric(df.columns)
    cond = (df[col] == 1) | (df[col] == 0)
    return df.loc[cond, [col]]



def geo_index():
    
    ds = b.load(INDEX_PATH)
    return ds[['f107a', 'kp', 'dst']].dropna()

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
        col = -50
    else:
        col = -80
        
    g = gamma(site)
    
    e = epbs(col)
    p = pre(site)
    i = geo_index()
    
    ds = pd.concat(
        [g, i, e, p], axis = 1
        ).dropna()
    
    ds.columns.name = gg.sites[site]['name']
    
    ds.rename(
        columns = {col: 'epb'}, 
        inplace = True
        )
    return ds


# df = concat_results('saa')



# df['vp'].plot()