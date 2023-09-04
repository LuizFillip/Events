import pandas as pd
import numpy as np
from math import floor, ceil
import PlasmaBubbles as pb 
import base as b 
from events import concat_results 



def probability_distribuition(
        df,
        step = 0.5, 
        col_gama = 'vz',
        col_epbs = 'same'
        ):
    
    """
    
    Read and concatenate growth rate
    and EPBs occurrence
    """
    
    year = df.index[0].year
      
    nums = np.arange(
        floor(df[col_gama].min()), 
        ceil(df[col_gama].max()), 
        step
        )
    


    out = {'start': [], 
           'end': [], 
           'days': [], 
           'epbs': [], 
           'rate': []}

    for start in nums:
        
        end = start + step
        
        res = df.loc[(df[col_gama] > start) & 
                     (df[col_gama] < end), :]

        epbs = len(res.loc[res[col_epbs] == 1.0])
        
        days = len(res)
        
        try:
            rate = epbs / days
        except:
            rate = 0
            
        for key in out.keys():
            
            out[key].append(vars()[key])
    
    ds = pd.DataFrame(out)
    
    ds = ds.loc[~((ds['epbs'] == 0) & (ds['days'] == 0))] 
    
    ds['year'] = year
    return ds




def run_all():
    
    import matplotlib.pyplot as plt 
    
    for year in range(2013, 2023):
    
        df = concat_results(year = year)
    
        
        ds = probability_distribuition(
                df,
                step = 0.2, 
                col_gama = 'all',
                col_epbs = 'epb'
                )
        
        plt.plot(ds['start'], ds['rate'], label = year)
        
        plt.legend()
        
# df = b.load('database/Results/gamma/saa.txt')

# df['all'] = df['all'] - df['R']

# df['all'].plot()


run_all()