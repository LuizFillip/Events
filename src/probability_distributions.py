import pandas as pd
import numpy as np
from math import floor, ceil
import PlasmaBubbles as pb 
import base as b 
# from events import concat_results 



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



import matplotlib.pyplot as plt 


    



    
b.config_labels()
    
    




  


def plot_distributions(
        ax, 
        df, 
        name, 
        marker = 's'
        ):


    ds = probability_distribuition(
        df,
        step = 0.2, 
        col_gamma = 'all',
        col_epbs = '-40'
        )
    
  
    args = dict(capsize = 3,
                marker = 's')
    
    ax.errorbar(
        ds['mean'], 
        ds['rate'], 
        xerr = ds['std'],
        yerr = ds['epb_std'],
        **args,
        label = name
        )
    ax.set(
        ylim = [-0.4, 1.4],
        yticks = np.arange(0, 1.25, 0.25),
        xlabel = '$\\gamma_{FT}~\\times 10^{-3}$ ($s^{-1}$)',
        ylabel = 'EPBs probability \noccurrence ($\\%$)'
        )
    
    
    
    for bar in [0, 1]:
        ax.axhline(bar, linestyle = ":", 
                   lw = 2, color = "k")
    
    



def solar_flux_activities(df):
    

    lower = df.loc[df['f107'] <= 100]
    
    medium = df.loc[
        (df['f107'] > 100) &
        (df['f107'] < 150)]
    
    
    high = df.loc[df['f107'] >= 150]
    
    return [lower, medium, high]



def plot_probability_distribution(df):
    
    fig, ax = plt.subplots(
        dpi = 300, 
        sharex = True,
        sharey = True,
        figsize = (12, 6)
        )
        

    names = ['$F_{10.7} < 100$',
             '$100 < F_{10.7} < 150$', 
             '$F_{10.7} > 150$']

    datasets = solar_flux_activities(df)

    for i, ds in enumerate(datasets):

        plot_distributions(
            ax, ds, names[i])
        
        
    ax.legend(ncol = 3, loc = 'lower right')



    fig.suptitle('disturbed days ($kp > 4$)')

    
    return 
    
df = b.load('all_results.txt')

cols = ['all', '-40', 'f107', 'kp_max']

plot_probability_distribution(df)


df.columns