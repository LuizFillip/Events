import pandas as pd
import numpy as np
from math import floor, ceil
import base as b 
import events as ev


def probability_distribuition(
        df,
        step = 0.2, 
        col_gamma = 'all',
        col_epbs = 'same'
        ):
    
    """
    
    Read and concatenate growth rate
    and EPBs occurrence
    """
    
   
    bins = np.arange(
        floor(df[col_gamma].min()), 
        ceil(df[col_gamma].max()), 
        step
        )
 
 
 
    out = {
           
           'start': [], 
           'end': [], 
           'days': [], 
           'epbs': [], 
           'rate': [], 
           'mean': [], 
           'std': [], 
           'epb_mean': [],
           'epb_std': []
           
           }
 
 
    for i in range(len(bins) - 1):
        
        
        start, end = bins[i], bins[i + 1]
        
        ds = df.loc[
            (df[col_gamma] > start) & 
            (df[col_gamma] <= end)
            ]
        
        if len(ds) == 0:
            pass
        else:
            epbs = len(ds.loc[ds[col_epbs] == 1.0])
            
            days = len(ds)
            
            rate = epbs / days
            
            mean = ds[col_gamma].mean()
            
            std = ds[col_gamma].std()
            
            epb_std = ds[col_epbs].std()
            
            epb_mean = ds[col_epbs].mean()
            
            for key in out.keys():
                
                out[key].append(vars()[key])
 
    return pd.DataFrame(out)


