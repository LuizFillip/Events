import core as c
import pandas as pd 

def percent(frac, total):
    
    return len(frac) / len(total) * 100

def geomanetic_by_solar(
        df, 
        percent_like = False,
        level = 86
        ):
    
    total = df.copy()
    
    out = {
        'quiet': [], 
        'disturded': []
        }
    
    solar = ['low', 'high']
    
    solar_dfs = c.solar_levels(
        df, 
        level = level,
        flux_col = 'f107a'
        )
    
    for i, ds in enumerate(solar_dfs):
        
        quiet = ds.loc[ds['kp'] <= 3]
        disturded = ds.loc[ds['kp'] > 3]
        
        if percent_like:
            
            for key in out.keys():
                
                out[key].append(
                    percent(vars()[key], total)
                    )
        else:  
            
            for key in out.keys():
                out[key].append(len(vars()[key]))
        
    ds = pd.DataFrame(out, index = solar)

    ds['total'] = ds.sum(axis = 1)

    ds.loc['total', :] = ds.sum(axis=0)
    
    return ds

df = c.concat_results('saa')

limit = c.limits_on_parts(df['f107a'], parts = 2)

# limit = 86

geomanetic_by_solar(
        df, 
        percent_like = False,
        level = limit
        )

# df['gamma'].plot()

