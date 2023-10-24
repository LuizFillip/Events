import numpy as np 
import random
import GEO as gg
import PlasmaBubbles as pb
import GNSS as gs 
import os 
import pandas as pd 
from tqdm import tqdm 


PATH_RANDOM = 'database/epbs/vad_random/'


def get_filters_lists(
        clon, 
        clat, 
        radius, 
        year = 2021,
        num_rem = 2
        ):
    
    names, lon, lat = gg.arr_coords(year)

    in_x, in_y = gg.distance_circle(
        lon, lat, 
        (clon, clat), 
        radius
        )
    
    indices = np.where(np.isin(lon, in_x))[0]
        
    return [names[i] for i in indices]

def fixed_lits(receivers, num_rem = 2):
    list_0 = receivers[num_rem:]
    list_1 = list_0[num_rem:]
    list_2 = list_1[num_rem:]
    list_3 = list_2[num_rem:]
    list_4 = list_3[num_rem:]

    return (list_0, list_1, list_2, list_3, list_4)


def random_lists(receivers):
    
    out = {}
    for i in range(1, 11, 2):
        
        out[i] = random.sample(receivers, i)

    return out


def max_by_receivers(path, receivers):
     
    df = pb.load_filter(
        path.fn_roti, 
        factor = 3
        )
    
    times = pb.time_range(df)
    
    out = []
    
    for num, receiver in receivers.items():
            
        ds1 = df.loc[df['sts'].isin(receiver)]
                
        out.append(
            pb.time_dataset(
                ds1, 
                num, 
                times
                )
            )
        
    return pd.concat(out, axis = 1).round(4)



def run_days(year, root = os.getcwd()):
    
    clon, clat, radius = -45, -5, 6
    
    receivers = get_filters_lists(
            clon, 
            clat, 
            radius, 
            year
            )
    
    out = []
    
    for doy in tqdm(
            range(1, 366), 
                    str(year)):
            
        path = gs.paths(
            year, doy, root 
            )
        
        out.append(
            max_by_receivers(
                path, 
                random_lists(receivers)
                )
            )
        
    df = pd.concat(out)
    
    df.to_csv(f'{PATH_RANDOM}{year}.txt')
    
    return df

def run():
    for year in range(2013, 2023):
        
        if year < 2019:
            root = 'D:\\'
        else:
            root = 'F:\\'
        
        run_days(year, root)
        
clon, clat, radius = -45, -5, 6
year = 2019

receivers = get_filters_lists(
        clon, 
        clat, 
        radius, 
        year
        )

random_lists(receivers)