import events as ev 
import pandas as pd 





  

def percent(frac, total):
    
    return len(frac) / len(total) * 100

def geomanetic_by_solar(
        df, 
        percent_like = False
        ):
    
    total = df.copy()
    
    out = {
        'quiet': [], 
        'disturded': []
        }
    
    solar = ['low', 'high']
    
    solar_dfs =  ev.solar_levels(
        df, 
        level = 86,
        flux_col = 'f107a'
        )
    
    for i, ds in enumerate(solar_dfs):
        
        quiet = ds.loc[ds['kp'] <= 3]
        disturded = ds.loc[ds['kp'] > 3]
        
        if percent_like:
            
            for r in out.keys():
                
                out[r].append(
                    percent(vars()[r], total)
                )
        else:  
            
            for r in out.keys():
                out[r].append(len(vars()[r]))
        
    ds = pd.DataFrame(out, index = solar)

    ds['total'] = ds.sum(axis = 1)

    ds.loc['total',:] = ds.sum(axis=0)
    
    return ds

# ds = geomanetic_by_solar(
#         df, 
#         percent_like = False
#         )






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


df = ev.concat_results('saa')

 
level = 86




