from common import load


class storms_types:
    
    def __init__(
            self, 
            infile, 
            col_storm = 'kp', 
            year = None):
        
        df = load(infile)
        
        if year is not None:
            df = df.loc[df.index.year == year]
        
        self.intense = df.loc[df[col_storm] >= 6]
        
        self.modered = df.loc[
            (df[col_storm] > 3) &
            (df[col_storm] < 6)
            ]
        
        self.quiets = df.loc[df[col_storm] <= 3]
        self.df = df

def main():
    infile ='all_results.py'
