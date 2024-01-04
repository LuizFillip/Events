import PlasmaBubbles as pb 
import os 
import base as b 
import RayleighTaylor as rt
import pandas as pd
import core as c 

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

def concat_longitudes_by_date(
        days, 
        root = 'D:\\'
        ):
    
    out = []    
        
    for dn in days.index[1:]:
        
        path = pb.path_roti(dn, root)
        
        out.append(pb.long_dataset2(path))
        
    return pd.concat(out)
    

def save_temp(ds, path_to_save):
    ds.to_csv(path_to_save)

def fname(dn, folder = 'temp2'):
    b.make_dir(f'{folder}/')
    filename = dn.strftime('%Y%m%d.txt')
    return f'{folder}/{filename}'


def run_and_save():
    
    days = c.range_days(days = 4, kind = 0)
    events = c.concat_and_sel(days)
    folder = 'temp2'
    
    for day, event in zip(days, events):
            
        ds = concat_longitudes_by_date(
                day, 
                root = 'D:\\'
                )
        
        save_temp(ds, fname(event, folder = folder))


