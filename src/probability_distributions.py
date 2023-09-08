import pandas as pd
import numpy as np
from math import floor, ceil
import PlasmaBubbles as pb 
import base as b 
# from events import concat_results 



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
                     (df[col_gama] <= end), :]

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
    
    ds['rate'] =  ds['rate'] *100
    
    ds['year'] = year
    return ds


def set_plots(ax):
    
    for ax in ax.flat:
        for bar in [0, 100]:
            ax.axhline(bar, linestyle = ":", 
                       lw = 2, color = "k")
            


import matplotlib.pyplot as plt 


def plot_distributions(ax, df, s = 2013, e = 2016):
    
    years = list(range(s, e))

    for yr in years:
        
        ds1 = df.loc[df.index.year == yr]
    
        ds = probability_distribuition(
                ds1,
                step = 0.2, 
                col_gama = 'all',
                col_epbs = 'epb'
                )
        
        ax.plot(ds['start'], ds['rate'], label = yr)
        ax.set(xlim = [0, 3], 
               ylim = [-20, 120],
               xlabel = '$\\gamma_{FT}~\\times 10^{-3}$ ($s^{-1}$)')
        
        
        
    ds2 = df.loc[df.index.year <= years[-1]]
    
    ds = probability_distribuition(
            ds2,
            step = 0.2, 
            col_gama = 'all',
            col_epbs = 'epb'
            )
    
    ax.plot(ds['start'], ds['rate'], lw = 2,
            label = 'all', color = 'r')
    
    
    ax.legend(ncol = 1, 
              loc = 'lower right')


def plot_probability_distribution():
    
    fig, ax = plt.subplots(
        dpi = 300,
        ncols = 2, 
        sharex = True,
        sharey = True,
        figsize = (12, 4)
        )

    plt.subplots_adjust(wspace = 0.1)
    
    plot_distributions(ax[0], df, s = 2013, e = 2016)
    plot_distributions(ax[1], df, s = 2018, e = 2021)


    ax[0].set(ylabel = 'EPBs probability \noccurrence ($\\%$)')


    set_plots(ax)


    fig.suptitle('disturbed days ($kp > 4$)')

    
    return 
    
b.config_labels()
    
    


df = b.load('all_results.txt')

# df = df.loc[df['kp_max'] > 4]



# df.loc[df.index.year == 2021, 'all'].plot()
   


