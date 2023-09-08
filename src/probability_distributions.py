import pandas as pd
import numpy as np
from math import floor, ceil
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




def plot_distribution(
        ax, 
        df, 
        name, 
        step = 0.2, 
        col_gamma = 'all',
        col_epbs = '-40'
        ):
    
    b.config_labels()


    ds = probability_distribuition(
        df,
        step = step, 
        col_gamma = col_gamma,
        col_epbs = col_epbs
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
    

    for bar in [0, 1]:
        ax.axhline(
            bar, 
            linestyle = ":", 
            lw = 2, 
            color = "k"
            )
        
    return ds['epbs'].sum()
    


def solar_flux_activities(df):
    

    lower = df.loc[df['f107'] <= 100]
    
    medium = df.loc[
        (df['f107'] > 100) &
        (df['f107'] < 150)]
    
    
    high = df.loc[df['f107'] >= 150]
    
    return [lower, medium, high]

def storm_activities(df):
    
    week = df[(df['dst'] > -50)]
    
    moderate = df[(df['dst'] < -50) & 
                  (df['dst'] > -100)]
    
    intense = df[(df['dst'] < -100)]
    
    return [week, moderate, intense]

def plot_distributions_solar_flux(
        df, 
        geomag = 'quiet', 
        step = 0.2, 
        col_gamma = 'all',
        col_epbs = '-40'
        ):
    
    fig, ax = plt.subplots(
        dpi = 300, 
        sharex = True,
        sharey = True,
        figsize = (12, 6)
        )
    
    vmin, vmax = df[col_gamma].min(), df[col_gamma].max()
    
    vmin, vmax = floor(vmin), ceil(vmax)
    
    
    if geomag == 'quiet':
        
        df = df[df['kp_max'] <= 3]
        
        title = 'Quiet days ($Kp \\leq 3$)'
    else:

        df = df[df['kp_max'] > 3]

        title = 'Disturbed days ($Kp > 3$)'

    names = ['$F_{10.7} < 100$',
             '$100 < F_{10.7} < 150$', 
             '$F_{10.7} > 150$']

    datasets = solar_flux_activities(df)
    
    count = []

    for i, ds in enumerate(datasets):
        
        index = i + 1

        c = plot_distribution(
            ax, 
            ds, 
            f'({index}) {names[i]}', 
            step = step, 
            col_gamma = col_gamma,
            col_epbs = col_epbs
            )
        
        count.append(f'({index}) {c} events')
        
    ax.set(
        xlim = [vmin - step, vmax + step],
        xticks = np.arange(vmin, vmax, step * 2),
        ylim = [-0.2, 1.2],
        yticks = np.arange(0, 1.25, 0.25),
        xlabel = '$\\gamma_{FT}~\\times 10^{-3}$ ($s^{-1}$)',
        ylabel = 'EPB occurrence probability'
        )
    
    infos = 'EPB occurrence\n' + '\n'.join(count)
        
    ax.text(0.77, 0.3, infos, transform = ax.transAxes)
        
    ax.legend(ncol = 3, 
              bbox_to_anchor = (.5, 1.15),
              loc = "upper center"
              )

    fig.suptitle(title, y = 1.05)

    return fig
    
df = b.load('all_results.txt')

cols = ['all', '-40', 'f107', 'kp_max']



f = plot_distributions_solar_flux(
    df, geomag = 'quiet'
    )