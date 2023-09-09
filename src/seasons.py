import base as b 
import datetime as dt 



def dn2doy(dn):

    return dn.timetuple().tm_yday


def seasons(df, month = 6):
        
    dn =  dt.date(2013, month, 21)
    
    if month == 12:
    
        df['doy'] = df['doy'].where(
            df['doy'] >= 36, df['doy'] + 365)
    
        
    cond = ((df['doy'] > dn2doy(dn) - 45) &
            (df['doy'] <= dn2doy(dn) + 45))
    
    return df.loc[cond]


