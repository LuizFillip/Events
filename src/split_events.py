import events as ev 
import pandas as pd 
import numpy as np 




def monthly_occurences(df, col = 'epb'):
    
    out = {'epb': [], 'no_epb': []}
    months = list(range(1, 13, 1))
    
    for month in months:
        
        df_mon = df.loc[
            df.index.month == month, 
            col
            ]
        out['epb'].append((df_mon == 1).sum())
        out['no_epb'].append((df_mon == 0).sum())
    
    return pd.DataFrame(out, index = months)




def yearly_occurrences(df):
    
    years = np.unique(df.index.year)
    
    out = {'epb': [], 'no_epb': []}
    
    for year in years:
    
        df_yr = df.loc[
            df.index.year == year, 'epb'
            ]
        
        out['epb'].append((df_yr == 1).sum())
        out['no_epb'].append((df_yr == 0).sum())
        
    return pd.DataFrame(out, index = years)
        


def split_in_equal_parts(
        arr, 
        parts = 3
        ):
    
    length = len(arr)
    part_size = length // parts
    
                
    part1 = arr[:part_size]
    part2 = arr[part_size:2*part_size]
    part3 = arr[2*part_size:]
    
    return part1, part2, part3
        
        

def limits_on_parts(df, parts = 2):
    
    arr = sorted(df.values)
    
    parts = split_in_equal_parts(
            arr, 
            parts = 2
            )
        
    return [p[-1] for p in parts if len(p) != 0]
    
df = ev.concat_results('saa')

limits_on_parts(df['f107'], parts = 2)