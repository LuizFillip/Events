import pandas as pd
import numpy as np
from math import floor, ceil
import base as b 
import events as ev


def probability_distribuition(
        df,
        step = 0.2
        ):
    
    """
    
    Read and concatenate growth rate
    and EPBs occurrence
    """
    
   
    # bins = np.arange(
    #     floor(df['gamma'].min()), 
    #     ceil(df['gamma'].max()), 
    #     step
    #     )
    
    
    bins = np.arange(0, 3.6, step)
 
 
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
            (df['gamma'] > start) & 
            (df['gamma'] <= end)
            ]
        
        if len(ds) == 0:
            pass
        else:
            epbs = len(ds.loc[ds['epb'] == 1.0])
            
            days = len(ds)
            
            rate = epbs / days
            
            mean = ds['gamma'].mean()
            
            std = ds['gamma'].std()
                        
            epb_error = (epbs * 0.05) / days
             
            for key in out.keys():
                
                out[key].append(vars()[key])
    #df = 
    # df = df.loc[~ ((df['days']==1) &
    #                 (df['epbs'] == 1))]
    return pd.DataFrame(out)


# df = ev.concat_results('saa', col_g = 'e_f')

# df = df.loc[df['kp'] <= 3]

# ds = probability_distribuition(
#         df,
#         step = 0.2
#         )


# # plt.plot(ds.mean, ds.rate)


# ds