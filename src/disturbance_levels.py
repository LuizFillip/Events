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

def solar_levels(
        df, 
        level = (100),
        flux_col = 'f107a'
        ):
    
    if len(level) == 1:
        
        lower = df.loc[
            df[flux_col] <= level[0]
            ]
        
        high = df.loc[
            df[flux_col] > level[0]
            ]
        
        return [lower, high]
    
    else:
        
        lower = df.loc[
            df[flux_col] <= level[0]
            ]
        
        medium = df.loc[
            (df[flux_col] > level[0]) &
            (df[flux_col] < level[1])
            ]
        
        high = df.loc[
            df[flux_col] >= level[1]
            ]
        
        return [lower, medium, high]
        

def dst_levels(df):
    
    week = df[(df['dst'] > -50)]
    
    moderate = df[(df['dst'] < -50) & 
                  (df['dst'] > -100)]
    
    intense = df[(df['dst'] < -100)]
    
    return [week, moderate, intense]

def kp_levels(
        df, 
        level = 3, 
        kp_col = 'kp'
        ):
    
    
    quiet = df[
        df[kp_col] <= level
        ]
    
    disturbed = df[
        df[kp_col] > level
        ]
    
    return [quiet, disturbed]