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


def split_array_into_three_equal_parts(arr):
    length = len(arr)
    
    if length % 3 != 0:
        raise ValueError("Array cannot be divided into three equal parts.")
    
    part_size = length // 3
    
    part1 = arr[:part_size]
    part2 = arr[part_size:2*part_size]
    part3 = arr[2*part_size:]
    
    return part1, part2, part3

