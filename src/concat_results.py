import base as b 
import pandas as pd


def gamma():
    df = b.load('database/Results/gamma/saa.txt').dropna()
    
    df['all'] = df['all'] * 1e3
    
    df = df[~df.index.duplicated(keep = 'first')]
    
    return df

def indices(df):

    ds = b.load('database/indices/indeces.txt').dropna()
    
    return b.sel_dates(ds, df.index[0], df.index[-1])


def epbs(col = -40):
    
    df = b.load('database/epbs/postsunset.txt')
    
    df.rename(columns = {'all': 'epb'}, 
              inplace = True)
    return df

def dst(df):
    
    infile = 'database/indices/kyoto2000.txt'
    ds = b.load(infile)
    ds = ds.resample('D').min()
    return b.sel_dates(ds, df.index[0], df.index[-1])

def pre():
    df = b.load('digisonde/data/PRE/saa/2013_2022.txt')
    
    return df

def concat_results():
    
    g = gamma()
    
    e = epbs()
    
    p = pre()

    i = indices(g)
    
    d = dst(g)
    
    return pd.concat([g, i, p, e, d], axis = 1)


# df = concat_results()
    
# df.to_csv('all_results.txt')


