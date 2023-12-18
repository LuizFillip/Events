import pandas as pd
import numpy as np
import core as c

def limits(col):
    if col == 'gamma':
        vmin, vmax, step = 0, 3.8, 0.2
    elif col == 'vp':
        vmin, vmax, step = 0, 80, 5
    else:
        vmin, vmax, step = 0, 0.8, 0.05
        
    return (vmin, vmax, step)



def probability_distribution(df, col = 'gamma'):
    
    """
    Read and concatenate growth rate
    and EPBs occurrence
    """
    vmin, vmax, step = limits(col)
    
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
            (df[col] > start) & 
            (df[col] <= end)
            ]

        epbs = len(ds.loc[ds['epb'] == 1.0])
        
        days = len(ds)
        
        try:
            rate = epbs / days
            epb_error = (epbs * 0.05) / days
        except:
            
            if (epbs == 0) and (end > 50):
                rate = np.nan
                epb_error = np.nan
                
            elif (epbs == 0) and (days == 0):
                rate = np.nan
                epb_error = np.nan
            else:
                rate = 0
                epb_error = 0
            
        mean = ds[col].mean()
        std = ds[col].std()
                    
        for key in out.keys():
            
            out[key].append(vars()[key])
    
    return  pd.DataFrame(out)





def splited_dataset(df, col):

    vmin, vmax, step = limits(col)
    
    bins = np.arange(vmin, vmax + step, step)
    
    
    out = []
    
    for i in range(len(bins) - 1):
        
        start, end = bins[i], bins[i + 1]
        
        out.append( df.loc[
            (df[col] > start) & 
            (df[col] <= end)
            ]
        )
        
    return pd.concat(out).sort_index()

def test_difference(df):
        
    ds1 = splited_dataset(df, 'gamma')
    ds = splited_dataset(df, 'gravity')
    
    return ds.index.difference(ds1.index)
    
    
    
def main():
    df = c.concat_results('saa')


    col = 'gamma'

    ds = probability_distribution(df)
    
    return ds
