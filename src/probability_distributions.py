import pandas as pd
import numpy as np
import core as c

def limits(col):
    if col == 'gamma':
        vmin, vmax, step = 0, 3.5, 0.2
    elif col == 'vp':
        vmin, vmax, step = 0, 85, 5
    else:
        vmin, vmax, step = 0, 1, 0.05
        
    return (vmin, vmax, step)



def probability_distribuition(
        df,
        col = 'gamma'
        ):
    
    """
    
    Read and concatenate growth rate
    and EPBs occurrence
    """
    vmin, vmax, step = limits(col)
    
    bins = np.arange(vmin, vmax, step)
 
    out = {
           
           'start': [], 
           'end': [], 
           'days': [], 
           'epbs': [], 
           'epb_error': [],
           'rate': [], 
           'mean': [], 
           'std': []
           
           }
 
 
    for i in range(len(bins) - 1):
        
        start, end = bins[i], bins[i + 1]
        
        ds = df.loc[
            (df[col] > start) & 
            (df[col] <= end)
            ]

        if len(ds) == 0:
            pass
        else:
            epbs = len(ds.loc[ds['epb'] == 1.0])
            
            days = len(ds)
            
            rate = epbs / days
            
            mean = ds[col].mean()
            
            std = ds[col].std()
                        
            epb_error = (epbs * 0.05) / days
             
            for key in out.keys():
                
                out[key].append(vars()[key])
   
    ds = pd.DataFrame(out)
    
    ds = ds.loc[~(
        (ds['days'] == 1) & 
        (ds['epbs'] == 1))
        ]
    
    return ds



def test():
    df = c.concat_results(
        'saa', col_g = 'e_f')
    
    ds = probability_distribuition(df)
    
    return ds
