import matplotlib.pyplot as plt
import settings as s
from common import load
import pandas as pd

def PRE():
    infile = 'database/Drift/PRE/SAA/2013_2.txt'
    
    df1 = load(infile)
    
    infile = 'database/Digisonde/vzp/saa/2014_2015_2.txt'
    
    df = load(infile)
    
    return pd.concat([df1, df])    

def plot_pre_and_terminators():
    
    fig, ax = plt.subplots(
        figsize = (10, 4)
        )
    
    df = PRE()
    
    ax.scatter(df.index, df['time'])
    for dusk in [0, 12, 18]:
        infile = f'database/GEO/twilights/{dusk}.txt'
        ds = load(infile)
        ax.plot(ds['dusk'])
        
    ax.set(xlim = [df.index[0], 
                   df.index[-1]], 
           ylim = [20, 23])
    
    s.axes_month_format(
            ax, 
            month_locator = 4, pad = 60) 
    
    
plot_pre_and_terminators()


