def solar_flux_cycles(df):
    

    lower = df.loc[df['f107'] <= 100]
    
    medium = df.loc[
        (df['f107'] > 100) &
        (df['f107'] < 150)]
    
    
    high = df.loc[df['f107'] >= 150]
    
    return [lower, medium, high]

def storm_levels(df):
    
    week = df[(df['dst'] > -50)]
    
    moderate = df[(df['dst'] < -50) & 
                  (df['dst'] > -100)]
    
    intense = df[(df['dst'] < -100)]
    
    return [week, moderate, intense]

def kp_levels(df):
    quiet = df[df['kp_max'] <= 3]
    
    disturbed = df[df['kp_max'] > 3]
    
    return [quiet, disturbed]