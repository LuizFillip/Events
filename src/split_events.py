import events as ev 

df = ev.concat_results('saa')

col = 'gamma'
 

solar_level = 86


solar_dfs =  ev.solar_levels(
    df, 
    level = 86,
    flux_col = 'f107a'
    )


for df in solar_dfs:
    epb = len(df.loc[df['epb'] == 1])
    no_epb = len(df.loc[df['epb'] == 0])
    
    print(epb, no_epb, len(df))
    
    
solar = ['low', 'high']
for i, ds in enumerate(solar_dfs):
    
    quiet = ds.loc[ds['kp'] <= 3]
    distu = ds.loc[ds['kp'] > 3]
    print(solar[i], 'quiet', len(quiet) / len(df) *100)
    print(solar[i], 'disturded', len(distu) / len(df) *100)
    