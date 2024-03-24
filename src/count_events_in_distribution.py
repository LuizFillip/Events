import core as c 
import base as b 



def test_number_of_days(df, ds, parameter):
    
    days_in_dist = ds['days'].sum() 
    
    days_in_data = df[parameter].count()
    
    assert days_in_data == days_in_dist

def test_number_of_epbs(df, ds):
    
    epbs_in_dist = ds['epbs'].sum()
    
    epbs_in_data = df['epb'].sum()
    
    assert epbs_in_dist == epbs_in_data
    
# test_number_of_epbs(df, ds)
# test_number_of_days(df, ds, parameter)

df = c.load_results('saa')
parameter = 'vp'

ds = c.probability_distribution(
        df, 
        parameter, 
        outliner = None,
        limit = False 
        )


