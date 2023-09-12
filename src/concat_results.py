import base as b 
import pandas as pd


def gamma():
    
    path = 'database/Results/gamma/saa.txt'
    df = b.load(path).dropna()
    
    for col in ['all', 
                'gravity', 
                'winds']:
        
        df[col] = df[col] * 1e3
   
    df = df[~df.index.duplicated(keep = 'first')]
    
    df = df.loc[~(df['all'] > 3.5)]
    
    return df

def indices(df):
    path = 'database/indices/indeces.txt'
    ds = b.load(path).dropna()
    
    return b.sel_dates(ds, df.index[0], df.index[-1])


def epbs(col = -40):
    
    path = 'database/epbs/postsunset.txt'
    df = b.load(path)
    
    df.rename(columns = {'all': 'epb'}, 
              inplace = True)
    return df

def dst(df):
    
    infile = 'database/indices/kyoto2000.txt'
    ds = b.load(infile)
    ds = ds.resample('D').min()
    return b.sel_dates(ds, df.index[0], df.index[-1])

def pre():
    path = 'digisonde/data/PRE/saa/2013_2022.txt'
    df = b.load(path)
    
    return df

def concat_results():
    
    g = gamma()
    
    e = epbs()
    
    p = pre()

    i = indices(g)
    
    d = dst(g)
    
    return pd.concat([g, i, p, e, d], axis = 1)

def main():
    df = concat_results()
        
    df.to_csv('all_results.txt')



