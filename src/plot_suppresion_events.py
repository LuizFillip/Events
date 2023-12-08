from geophysical_indices import INDEX_PATH
import pandas as pd
import base as b
import PlasmaBubbles as pb 
import numpy as np


path = 'database/epbs/events_types.txt'


# df = pd.concat(
#     [b.load(path), 
#      b.load(INDEX_PATH)], 
#     axis = 1).dropna()


# ds = df.loc[df['kp'] > 3].iloc[:, :5]

ds = b.load(path)


        
        
def remove_middle(arr):
    middle_index = len(arr) // 2

    if len(arr) % 2 == 0:
        
        arr = np.delete(arr, [middle_index - 1, middle_index])
    else:
       
        arr = np.delete(arr, middle_index)

    return arr

    
    
    
#

def find_supressions(ds):
    
    ds['value'] = pb.event_for_all_longs(
        ds, 
        value = 1
        )
    
    out = []
    
    for i, row in enumerate(ds['value']):
    
        if row == 0:
    
            lst = ds.iloc[i - 2: i + 3, -1]
            
            lst_remo = remove_middle(lst.values)
            
            if all(x == 1 for x in lst_remo):
               
                out.append(ds.iloc[i, :-1].to_frame().T)
            else:
                pass
    
    return pd.concat(out)

df = find_supressions(ds)

df_filtered = df[df.apply(
    lambda row: 
    all(x == 0 for x in row), axis=1)
        ]
    
