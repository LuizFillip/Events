import pandas as pd
import core as c
import numpy as np



def remove_middle(arr):
    middle = len(arr) // 2
    if len(arr) % 2 == 0:
        arr = np.concatenate((arr[:middle - 1], arr[middle + 1:]))
    else:
        arr = np.concatenate((arr[:middle], arr[middle + 1:]))
    return arr

def atypical_occurrences(df, days=4, col='epb', kind=0):
    """
    Kind = 0 for suppresion events amd 1 for seeding events
    """
    out = []
    for i, row in enumerate(df[col]):
        
        if row == kind:
          
            cond = slice(i - days, i + days + 1)
            lst = df.iloc[cond][col]
            
            if len(lst) == (days * 2 + 1):
                lst_remo = remove_middle(lst.values)
                
                if all(x == (1 - kind) for x in lst_remo):
                    out.append(lst.to_frame(col))
     
    return out

def concat_and_sel(
        out, 
        col = 'epb', 
        kind = 0
        ):
    ds = pd.concat(out)
    return ds.loc[ds[col] == kind]

def get_days(days = 4, kind = 0):

    df = c.concat_results('saa')
    
    lst_days = atypical_occurrences(
        df, days = days, kind = kind)
    
    return concat_and_sel(lst_days, kind = kind)


get_days(kind = 0)

