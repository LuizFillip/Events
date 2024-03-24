import core as c 
import base as b 
import numpy as np 
import pandas as pd 

def splited_dataset(df, col):

    vmin, vmax, step = c.limits(col)
    
    bins = np.arange(vmin, vmax + step, step)

    out = []
    
    for i in range(len(bins) - 1):
        
        start, end = bins[i], bins[i + 1]
        
        out.append( 
            df.loc[(df[col] > start) & (df[col] <= end)]
        )
        
    return pd.concat(out).sort_index()

def test_difference(df):
        
    ds1 = splited_dataset(df, 'gamma')
    ds = splited_dataset(df, 'gravity')
    
    return ds.index.difference(ds1.index)
    

def test_number_of_days(df, ds, parameter):
    
    days_in_dist = ds['days'].sum() 
    
    days_in_data = df[parameter].count()
    
    assert days_in_data == days_in_dist

def test_number_of_epbs(df, ds):
    
    epbs_in_dist = ds['epbs'].sum()
    
    epbs_in_data = df['epb'].sum()
    
    assert epbs_in_dist == epbs_in_data
    
# test_number_of_epbs(df, ds)
# test_number_of_days(df, ds, parameter)

df = c.load_results('saa')
parameter = 'vp'

ds = c.probability_distribution(
        df, 
        parameter, 
        outliner = None,
        limit = False 
        )


