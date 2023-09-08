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
    
    
    return df#.loc[:, [str(col)]]

def concat_results():
    
    g = gamma()
    
    e = epbs()

    i = indices(g)
    
    return pd.concat([g, i, e], axis = 1)
# def main():

# df = concat_results()
    
# df.to_csv('all_results.txt')
    
    
# df 