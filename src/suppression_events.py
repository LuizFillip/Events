import pandas as pd
import core as c
import numpy as np
import PlasmaBubbles as pb 
import os 
import base as b 
import RayleighTaylor as rt


def remove_middle(arr):
    middle = len(arr) // 2

    if len(arr) % 2 == 0:
        
        arr = np.delete(
            arr, [middle - 1, middle])
    else:
       
        arr = np.delete(arr, middle)

    return arr


def find_supressions(df, days = 5, col = 'epb'):
   
   out = []
   for i, row in enumerate(df[col]):
       
       if row == 0:
         
           cond = slice(i - days, i + days + 1)
           lst = df.iloc[cond][col]
       
           lst_remo = remove_middle(lst.values)
           
           if all(x == 1 for x in lst_remo):
               out.append(lst.to_frame(col))
    
   return out

def suppression_days(out, col = 'epb'):
    ds = pd.concat(out)
    return ds.loc[ds[col] == 0]

def load_base_roti(ds):
        
    start = ds.index[2]
    end = ds.index[-1]
    
    path = pb.epb_path(
        start.year, 
        root = os.getcwd(), 
        path = 'longs'
        )
    
    return b.sel_dates(b.load(path), start, end)

def load_base_gamma(ds):

    ds1 = rt.gammas_integrated(
        rt.FluxTube_dataset(
            year = 2013, 
            site = "saa"
            ))
    
    start = ds.index[2]
    end = ds.index[-1]
    
    ds1['gamma'] = ds1['gamma'] * 1e3
    return b.sel_dates(ds1, start, end)


df = c.concat_results('saa')

ds = find_supressions(df, days = 4)[0]
import matplotlib.pyplot as plt

fig, ax = plt.subplots(
    dpi = 300, sharey = True)

b.config_labels()

df = load_base_roti(ds)

df['-50'].plot(ax = ax)

df2 = load_base_gamma(ds)

ax1 = ax.twinx()

df2['gamma'].plot(ax = ax1, color = 'b', lw = 2, ylim = [0, 3])

ax.set(ylabel = 'ROTI (TECU/min)')
ax1.set(ylabel = '$\\gamma_{RT} ~(s^{-1})$')

# ds