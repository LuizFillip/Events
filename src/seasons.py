import datetime as dt 
import core as c 
import pandas as pd


months = {
      'March equinox': 3,
      'June solstice': 6,
      'September equinox': 9,
      'December solstice': 12
      }

def dn2doy(dn):
    return dn.timetuple().tm_yday

def seasons(df, name):
    
    month = months[name]
        
    dn = dt.date(2013, month, 21)
    
    if month == 12:
    
        df['doy'] = df['doy'].where(
            df['doy'] >= 36, 
            df['doy'] + 365
            )

    cond = (
        (df['doy'] > dn2doy(dn) - 46) &
        (df['doy'] <= dn2doy(dn) + 46)
        )
    
    return df.loc[cond]

def test_difference(df):
    
    out = []
    for name in months.keys():
        out.append(seasons(df, name))

    ds = pd.concat(out)
    
    return df.index.difference(ds.index)


def main():
    
    df = c.concat_results('saa')
    
    for name in months.keys():
        print(len(seasons(df, name)))