import events as ev 

df = ev.concat_results('saa')

col = 'gamma'
 
# fig = plot_distributions_solar_flux(
#     df, 
#     col
#     )



FigureName = f'PD_{col}_effects'

# fig.savefig(b.LATEX(FigureName), dpi = 400)


# print(df)
solar_dfs =  ev.solar_levels(
    df, 
    level = 86,
    flux_col = 'f107a'
    )


for df in solar_dfs:
    epb = len(df.loc[df['epb'] == 1])
    no_epb = len(df.loc[df['epb'] == 0])
    
    print(epb, no_epb, len(df))