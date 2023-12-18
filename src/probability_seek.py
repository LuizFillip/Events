import core as c 


df = c.concat_results('saa')

col = 'gamma'


df = c.seasons(df, 'March equinox')


df =  c.solar_levels(
    df, 
    level = 86,
    flux_col = 'f107a'
    )[0]

# print(df.loc[(df[col] > 2) & (df[col] <= 2.2)])

ds = c.probability_distribution(
    df,
    col
    )

ds

