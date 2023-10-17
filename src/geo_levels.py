def solar_flux_cycles(
        df, 
        flux_col = 'f107a',
        lower_level = 90, 
        high_level = 120
        ):
    

    lower = df.loc[
        df[flux_col] <= lower_level
        ]
    
    medium = df.loc[
        (df[flux_col] > lower_level) &
        (df[flux_col] < high_level)
        ]
    
    high = df.loc[
        df[flux_col] >= high_level
        ]
    
    return [lower, medium, high]

def medium_solar_level(
        df, 
        flux_col = 'f107a',
        level = 90, 
     
        ):

    lower = df.loc[
        df[flux_col] <= level
        ]
    
  
    high = df.loc[
        df[flux_col] >= level
        ]
    
    return [lower, high]

def storm_levels(df):
    
    week = df[(df['dst'] > -50)]
    
    moderate = df[(df['dst'] < -50) & 
                  (df['dst'] > -100)]
    
    intense = df[(df['dst'] < -100)]
    
    return [week, moderate, intense]

def kp_levels(df, quiet_level = 4):
    
    
    quiet = df[
        df['kp_max'] <= quiet_level
        ]
    
    disturbed = df[
        df['kp_max'] > quiet_level
        ]
    
    return [quiet, disturbed]