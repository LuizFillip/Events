import base as b 
import datetime as dt 
import pandas as pd 


def sep_seasons(ds, year = 2013):
    
    ds = ds.loc[ds.index.year == year]
    
    summer = ds.loc[
        (ds.index < dt.datetime(year, 3, 21))
        ]
    
    fall = ds.loc[
        (ds.index > dt.datetime(year, 3, 21) ) &
        (ds.index < dt.datetime(year, 6, 21))
        ]
    
    winter = ds.loc[
        (ds.index > dt.datetime(year, 6, 21)) &
        (ds.index < dt.datetime(year, 9, 23))
        ]
    
    spring = ds.loc[
        (ds.index > dt.datetime(year, 9, 23)) &               
        (ds.index < dt.datetime(year, 12, 21)) 
                  ]
    
    return [spring, fall, winter, summer]


df = b.load('all_results.txt')