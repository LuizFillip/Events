import pandas as pd
import core as c
import numpy as np


def remove_middle(arr):
    middle_index = len(arr) // 2

    if len(arr) % 2 == 0:
        
        arr = np.delete(
            arr, [middle_index - 1, middle_index])
    else:
       
        arr = np.delete(arr, middle_index)

    return arr


def offset(days):
    if days % 2 == 0:
        raise('number the days must be odd')
    else:
        return days // 2


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





import PlasmaBubbles as pb 
import os 
import base as b 
import datetime as dt 

def suppression_days(out, col = 'epb'):
    ds = pd.concat(out)
    return ds.loc[ds[col] == 0]


# def main():
days = 4

df = c.concat_results('saa')

ds = find_supressions(df, days = days)[4]

delta = dt.timedelta(days = 7)

start = ds.index[2]
end = ds.index[-1]

path = pb.epb_path(
    start.year, 
    root = os.getcwd(), 
    path = 'longs'
    )

df = b.sel_dates(
    b.load(path), start, end)
col = '-50'
df[col].plot(ylim = [0, 4])

ds
