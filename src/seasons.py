# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 21:59:01 2023

@author: Luiz
"""


infile = 'all_results_2.txt'
ds = storms_types(infile).df

def sep_seasons(ds, year = 2013):
    
    ds = ds.loc[ds.index.year == 2013]
    
    summer = ds.loc[
        (ds.index < dt.datetime(2013, 3, 21))
        ]
    
    fall = ds.loc[
        (ds.index > dt.datetime(2013, 3, 21) ) &
        (ds.index < dt.datetime(2013, 6, 21))
        ]
    
    winter = ds.loc[
        (ds.index > dt.datetime(2013, 6, 21)) &
        (ds.index < dt.datetime(2013, 9, 23))
        ]
    
    spring = ds.loc[
        (ds.index > dt.datetime(2013, 9, 23)) &               
        (ds.index < dt.datetime(2013, 12, 21)) 
                  ]
    
    return [spring, fall, winter, summer]
