import pandas as pd 
import numpy as np 


def seasonal_yearly_occurrence(
        df, 
        col = '-50'
        ):
    
    """
    Agroup the plasma bubbles 
    events by month, and get the 
    occurrence by month
    """
     
    epb = df.loc[df[col] == 1, [col]].copy()

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


class count_occurences:
    
    
    def __init__(self, df):
        self.s_year = df.index[0].year        
        self.e_year = df.index[-1].year
    
        self.df = df
        
    
    
    @staticmethod
    def count_all_types(df_sel, month):
    
        out = {}
    
        for col in df_sel.columns:
                    
            out[col] =  (df_sel[col] == 1).sum()
            
        return pd.DataFrame(out, index = [month])


    @property
    def month(self):
    
        out = []
        for month in range(1, 13, 1):
       
            df_mon = self.df.loc[self.df.index.month == month]
            
            out.append(self.count_all_types(df_mon, month))
            
        return pd.concat(out)
    
    
    @property
    def year(self):
        
        res = []
        for year in range(self.s_year, self.e_year + 1):
            
            df_yr = self.df.loc[self.df.index.year == year]
            res.append(self.count_all_types(df_yr, year))
                
        return pd.concat(res)


# import core as c 

# ds = c.epbs(col = -80, geo = False)

# ds = ds.loc[ds.index.year == 2018]
