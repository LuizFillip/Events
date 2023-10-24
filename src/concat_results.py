import base as b 
import pandas as pd
import os 
import RayleighTaylor as rt 
import GEO as gg 


PATH_GAMMA = 'database/Results/gamma/'
PATH_EPB = 'database/epbs/events_types.txt'
PATH_PRE = 'digisonde/data/PRE/'
PATH_INDEX=  'database/indices/omni_pro.txt'

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


# df = concat_results('saa', col_g = 'e_f')





def epbs(col = -50):

    df = b.load(PATH_EPB)
    df.columns = pd.to_numeric(df.columns)
    cond = (df[col] == 1) | (df[col] == 0)
    return df.loc[cond, [col]]



def geo_index():
    
    ds = b.load(PATH_INDEX)
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
    
    g = rt.parameters2()

    g = g[['gravity', 'gamma']] *1e3
    e = epbs(col_e)
    p = pre(site)
    i = geo_index()
    
    ds = pd.concat(
        [g, i, e, p], axis = 1
        ).dropna()
    
    ds.columns.name = gg.sites[site]['name']
    
    ds.rename(
        columns = {
            col_e: 'epb', 
            # col_g: 'gamma'
            }, 
        inplace = True
        )
    return ds


# g = rt.parameters2()

 

# g = g[['gravity', 'gamma']]

# g.plot()

# concat_results(
#         site = 'saa', 
#         col_g = 'night'
#         )