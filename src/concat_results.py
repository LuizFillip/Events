import base as b 
import pandas as pd
import PlasmaBubbles as pb
import geophysical_indices as gd


def concat_epbs():
    out = []
    for yr in range(2013, 2023):
        path_epb = f'database/EPBs/events/{yr}.txt'
        
        out.append(pb.events_in_year(path_epb))
        
        
    ds = pd.concat(out)
    
    ds.rename(columns = {'all' : 'epb'}, 
              inplace = True)
    ds = ds[~ds.index.duplicated(keep='first')]
    ds.index = pd.to_datetime(ds.index)
    return ds


def concat_results():
    
    df = b.load('database/Results/gamma/saa.txt')
    
    df['all'] = df['all'] * 1e3
    df = df[~df.index.duplicated(keep='first')]
    epbs = concat_epbs()
    
    idx =  gd.GFZ()
    idx = idx[~idx.index.duplicated(keep='first')]
    idx.index = pd.to_datetime(idx.index)
    return  pd.concat(
        [df, epbs, idx], axis = 1).dropna()

def main():

    df = concat_results()
    
    df.to_csv('all_results.txt')
