import base as b 
import core as c
import pandas as pd

df = b.load('core/data/all_maximus')
df['mean'] = df.mean(axis = 1)

df = df.resample('1D').asfreq()
idx = c.geo_index(
        cols = ['f107a', 'f107', 'kp', 'dst'],
        syear = 2013, 
        eyear = 2023
        )

ds = pd.concat([df['mean'], idx], axis = 1)

ds

