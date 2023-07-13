from common import load


class storms_class:
    
    def __init__(self, infile):
        
        df = load(infile)
        
        self.intense = df.loc[df['kp'] >= 6]
        
        self.modered = df.loc[
            (df['kp'] > 3) &
            (df['kp'] < 6)
            ]
        
        self.quiets = df.loc[df['kp'] <= 3]
        

infile ='all_results.py'
