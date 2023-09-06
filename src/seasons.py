import base as b 
import datetime as dt 



def get_doy(dn):

    return dn.timetuple().tm_yday





def summer(df):
    start =  get_doy(dt.date(2013, 12, 21))
    end = get_doy(dt.date(2013, 3, 21))
    
    cond =  (df['doy'] > start) | (df['doy'] <= end)
    return df.loc[cond]


def fall(df):
    start = get_doy(dt.date(2013, 3, 21))
    end = get_doy(dt.date(2013, 6, 21))
    
    cond = (df['doy'] > start) & (df['doy'] <= end)
    return df.loc[cond]


def winter(df):
    start = get_doy(dt.date(2013, 6, 21))
    end = get_doy(dt.date(2013, 9, 23))
    
    cond = (df['doy'] > start) & (df['doy'] <= end)
    return df.loc[cond]


def spring(df):
    start = get_doy(dt.date(2013, 9, 23))
    end = get_doy(dt.date(2013,  12, 21))
    
    cond = (df['doy'] > start) & (df['doy'] <= end)
    return df.loc[cond]







def season(df, month = 6):
        
    dn =  dt.date(2013, month, 21)
    
    if month == 12:
    
        df['doy'] = df['doy'].where(
            df['doy'] >= 36, df['doy'] + 365)
    
        
    cond = ((df['doy'] > get_doy(dn) - 45) &
            (df['doy'] <= get_doy(dn) + 45))
    
    return df.loc[cond]


df = b.load('all_results.txt')

df['doy'] =  df.index.day_of_year




