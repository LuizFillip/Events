import pandas as pd
import numpy as np
from math import floor, ceil

def probability_distribuition(
        df,
        step = 0.5, 
        func = 'vz',
        col_epb = 'same'
        ):
    
    """
    
    Read and concatenate growth rate
    and EPBs occurrence
    """
      
    nums = np.arange(
        floor(df[func].min()), 
        ceil(df[func].max()), 
        step
        )
    


    out = {'start': [], 
           'end': [], 
           'days': [], 
           'epbs': [], 
           'rate': []}

    for start in nums:
        
        end = start + step
        
        res = df.loc[(df[func] > start) & 
                     (df[func] < end), :]

        epbs = len(res.loc[res[col_epb] == 1])
        
        days = len(res)
        
        try:
            rate = epbs / days
        except:
            rate = 0
            
        for key in out.keys():
            
            out[key].append(vars()[key])
    
    ds = pd.DataFrame(out)
    
    ds.loc[(ds['epbs'] == 0) & 
           (ds['days'] == 0), 'rate'] = 1
    
    
    return ds