import PlasmaBubbles as pb 
import os 
import base as b 
import RayleighTaylor as rt
import datetime as dt 
import pandas as pd

def concat_longitudes_by_date(
        start, 
        days = 7, 
        root = 'D:\\'
        ):
    
    out = []    
        
    for day in range(days):
        
        delta = dt.timedelta(days = day)
        dn = start + delta
        
        path = pb.path_roti(dn, root)
        
        out.append(pb.long_dataset2(path))
        
    return pd.concat(out)


def save_temp(ds, fname):
    ds.to_csv('temp/' + fname)

def fname(start):
    
    b.make_dir('temp/')
    filename = start.strftime('%Y%m%d.txt')
    return f'temp/{filename}'

def load_base_roti(ds):
        
    start = ds.index[2]
    end = ds.index[-1]
    
    path = pb.epb_path(
        start.year, 
        root = os.getcwd(), 
        path = 'longs'
        )
    
    return b.sel_dates(b.load(path), start, end)

def load_base_gamma(ds):

    ds1 = rt.gammas_integrated(
        rt.FluxTube_dataset(
            year = 2013, 
            site = "saa"
            ))
    
    start = ds.index[2]
    end = ds.index[-1]
    
    ds1['gamma'] = ds1['gamma'] * 1e3
    
    return b.sel_dates(ds1, start, end)



def load_raw_roti(start):

    path = fname(start)
    
    if not os.path.exists(path):
        ds = concat_longitudes_by_date(start)
        ds.to_csv(fname(start))
    
    return b.load(fname(start))

start = dt.datetime(2013, 4, 3)

ds = load_raw_roti(start)
ds = load_base_roti(ds)

ds['-50'].plot()

