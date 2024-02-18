import datetime as dt 
import core as c 


class SeasonsSplit(object):
    
    def __init__(
            self, 
            df, 
            month, 
            translate = False
            ):
        
        month = month.lower()
        
        if month == 'march':
            dn = dt.date(2013, 3, 21)
            
            if translate:
                name = 'Equinócio de Março'
            else:
                name = 'March equinox'
        
        elif month == 'june':
            dn = dt.date(2013, 6, 21)
            
            if translate:
                name = 'Solstício de Junho'
            else:
                name = 'June solstice'
            
        elif month == 'september':
            dn = dt.date(2013, 9, 21)
            
            if translate:
                name = 'Equinócio de Setembro'
            else:
                name = 'September equinox'
            
        else:
            df['doy'] = df['doy'].where(
                df['doy'] >= 36, 
                df['doy'] + 365
                )
            dn = dt.date(2013, 12, 21)
            
            if translate:
                name = 'Solstício de Dezembro'
            else:
                name = 'December solstice'
       
        self.df = df
        self.dn = dn
        self.name = name
    
    @staticmethod
    def dn2doy(dn):
        return dn.timetuple().tm_yday
    
    @property
    def sel_season(self):
        
        cond = (
        (self.df['doy'] > self.dn2doy(self.dn) - 46) &
        (self.df['doy'] <= self.dn2doy(self.dn) + 46)
            )
        
        return self.df.loc[cond]


def main():
    
    df = c.concat_results('saa')
    
    ss = SeasonsSplit(df, 'june', translate = True)
    
    print(ss.sel_season, ss.name)