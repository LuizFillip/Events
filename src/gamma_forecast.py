import base as b 
import core as c
import pandas as pd 
from sklearn.metrics import confusion_matrix, accuracy_score


def predict(pred, input_value):
    
    pred['Diff1'] = abs(pred['start'] - input_value)
    pred['Diff2'] = abs(pred['end'] - input_value)
    
   
    min_row = pred.loc[(pred['Diff1'] + pred['Diff2']).idxmin()]
    
    if min_row['rate'] <= 0.5:
        return 0
    else:
        return 1



def predict_values(train_data, test_data):
    
    pred = c.probability_distribution(train_data)    
    epb = test_data['epb'].values
    gamma = test_data['gamma'].values
    epb_pred = [predict(pred, g) for g in gamma]
    
    return epb, epb_pred
    
def metrics(y, y_pred):
    cm = confusion_matrix(y, y_pred)
    
    acc_score = accuracy_score(y, y_pred)
    
df = c.load_results('saa')

train_data = df.loc[df.index.year < 2023]

test_data = df.loc[df.index.year == 2023]