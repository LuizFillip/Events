class DisturbedLevels:
    
    
    def __init__(self, df):
        
        self.df = df
        
        
    def F107(self, level = 100):
        
        if isinstance(level, (int, float)):
            level = [level]
            
        if level is None:
            return [self.df]
        
        if len(level) == 1:
            
            lower = self.df.loc[
                self.df['f107a'] <= level[0]
                ]
            
            high = self.df.loc[
                self.df['f107a'] > level[0]
                ]
            
            return [lower, high]
        
        else:
            
            lower = self.df.loc[
                self.df['f107a'] <= level[0]
                ]
            
            medium = self.df.loc[
                (self.df['f107a'] > level[0]) &
                (self.df['f107a'] < level[1])
                ]
            
            high = self.df.loc[
                self.df['f107a'] >= level[1]
                ]
            
            return [lower, medium, high]
        
    def Kp(self, level = 3):
        
        quiet = self.df[self.df['kp'] <= level]
        
        disturbed = self.df[self.df['kp'] > level]
        
        return [quiet, disturbed]
    
    def Dst(self):
        
        week = self.df[(self.df['dst'] > -50)]
        intense = self.df[(self.df['dst'] < -100)]
        
        moderate = self.df[
            (self.df['dst'] < -50) & 
            (self.df['dst'] > -100)
            ]
        
        return [week, moderate, intense]

    @staticmethod
    def solar_labels(level):
        level = round(level, 1)
        return [
        '$F_{10.7} \\leq $' + f' {level}',
        '$F_{10.7} > $' + f' {level}'
        ]        