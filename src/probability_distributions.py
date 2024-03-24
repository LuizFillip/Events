import pandas as pd
import numpy as np
import core as c

def input_limits(parameter):
    if 'gamma' in parameter:
        # vmin, vmax, step = 0, 3.8, 0.2
        vmin, vmax, step = 0, 2.8, 0.2
    elif parameter == 'vp':
        # vmin, vmax, step = -1, 90, 5
        vmin, vmax, step = 0, 70, 5
    else:
        vmin, vmax, step = 0, 0.8, 0.05
        
    return (vmin, vmax, step)


def compute_limits(df, parameter = 'gamma'):
    vls = df[parameter].values 
    
    vmin, vmax = np.floor(vls.min()), np.ceil(vls.max())
    
    if parameter == 'gamma':
        step = 0.5
    else:
        step = 5
        
    return (vmin, vmax, step)



def probability_distribution(
        df, 
        parameter = 'gamma', 
        outliner = 10,
        limit = None
        ):
    
    """
    Read and concatenate growth rate
    and EPBs occurrence
    """
    if limit is None:
        vmin, vmax, step = input_limits(parameter)
    else:
        vmin, vmax, step = compute_limits(df, parameter)

    bins = np.arange(vmin, vmax + step, step)
    
    
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
            (df[parameter] > start) & 
            (df[parameter] <= end)
            ]

        epbs = len(ds.loc[ds['epb'] == 1.0])
        
        days = len(ds)
        
        try:
            rate = epbs / days
            epb_error = (epbs * 0.05) / days
        except:
            
            if (epbs == 0) and (end > 50):
                rate = 0
                epb_error = 0
                
            elif (epbs == 0) and (days == 0):
                rate = np.nan
                epb_error = np.nan
            else:
                rate = 0
                epb_error = 0
            
        mean = ds[parameter].mean()
        std = ds[parameter].std()
                    
        for key in out.keys():
            
            out[key].append(vars()[key])
    
    df = pd.DataFrame(out)
    
    if outliner is not None:
        df = df.loc[~(df['days'] < outliner)].dropna()

    return df




    
    