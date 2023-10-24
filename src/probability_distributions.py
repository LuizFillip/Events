import pandas as pd
import numpy as np
import events as ev 


def probability_distribuition(
        df,
        limits = (0, 3.2, 0.2),
        col = 'gamma'
        ):
    
    """
    
    Read and concatenate growth rate
    and EPBs occurrence
    """
    vmin, vmax, step = limits 
    
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
   
    return pd.DataFrame(out)



def test():
    df = ev.concat_results(
        'saa', col_g = 'e_f')
    
    ds = probability_distribuition(df)
