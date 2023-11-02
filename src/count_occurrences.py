import pandas as pd 
import numpy as np 
from events import concat_results, solar_levels, epbs



def monthly_occurrences(df, col = 'epb'):
    
    out = {'epb': [], 'no_epb': []}
    months = list(range(1, 13, 1))
    
    for month in months:
        
        df_mon = df.loc[
            df.index.month == month, 
            col
            ]
        out['epb'].append((df_mon == 1).sum())
        out['no_epb'].append((df_mon == 0).sum())
    
    return pd.DataFrame(out, index = months)


def yearly_occurrences(df):
    
    years = np.unique(df.index.year)
    
    out = {'epb': [], 'no_epb': []}
    
    for year in years:
    
        df_yr = df.loc[
            df.index.year == year, 'epb'
            ]
        
        out['epb'].append((df_yr == 1).sum())
        out['no_epb'].append((df_yr == 0).sum())
        
    return pd.DataFrame(out, index = years)

df = concat_results('saa')

df  = epbs(class_epb = 'sunset')

ds = yearly_occurrences(df, col = 'epb')

