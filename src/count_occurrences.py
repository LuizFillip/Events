import pandas as pd 
import numpy as np 


def month_to_month_occurrence(
        df, 
        col = '-50'
        ):
    
    """
    Agroup the plasma bubbles 
    events by month, and get the 
    occurrence by month
    """
     
    epb = df.loc[
        df[col] == 1, [col]
        ].copy()

    count_epb = epb.groupby(
        epb.index.to_period('M')
        ).agg('count')
     
    ys = df.index[0].year
    ye = df.index[-1].year
    
    new_index = pd.date_range(
        f"{ys}-01-01", 
        f"{ye}-12-31", 
        freq = "1M"
        )

    ds = count_epb.reindex(
        pd.PeriodIndex(
            new_index, 
            freq = "M"
            )
        )
    
    ds.index = ds.index.to_timestamp()

    return ds


def month_occurrence(
        df, 
        value = 1.0
        ):

    cols = df.columns
    
    cols = [c for c in cols if 'f' not in c]
    
    res = []
    for month in range(1, 13, 1):
        
        out = {}
        for col in cols:
            
            df_mon = df.loc[
                df.index.month == month, col
                ]
            out[col] = (df_mon == value).sum()
            
        res.append(
            pd.DataFrame(
                out, index = [month]
                )
            )
    return pd.concat(res)


def year_occurrence(
        df, 
        value = 1.0
        ):
    
    cols = df.columns
    
    cols = [c for c in cols if 'f' not in c]
    
    res = []
    for year in range(2013, 2023):
        out = {}
        for col in cols:
            df_yr = df.loc[
                df.index.year == year, col
                ]
            out[col] = (df_yr == value).sum()
            
        res.append(
            pd.DataFrame(
                out, index = [year]
                )
            )
    return pd.concat(res)



class non_and_occurrences:
    
    
    def __init__(self, df):
        
        self.df = df
        

    def count(self):
        return
    
    def monthly(self):
        
        out = {'epb': [], 'no_epb': []}
        
        months = list(range(1, 13, 1))
        
        for month in months:
            
            df_mon = self.df.loc[
                self.df.index.month == month, 'epb'
                ]
            out['epb'].append((df_mon == 1).sum())
            out['no_epb'].append((df_mon == 0).sum())
        
        return pd.DataFrame(out, index = months)
    
    
    def yearly(self):
        
        years = np.unique(self.df.index.year)
        
        out = {'epb': [], 'no_epb': []}
        
        for year in years:
        
            df_yr = self.df.loc[
                self.df.index.year == year, 'epb'
                ]
            out['epb'].append((df_yr == 1).sum())
            out['no_epb'].append((df_yr == 0).sum())
            
        return pd.DataFrame(out, index = years)

