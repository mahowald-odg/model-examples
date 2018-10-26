# fastscore.schema.0: sch_in
# fastscore.schema.1: sch_out
# fastscore.recordsets.$all: yes
 
 
import numpy as np
import pandas as pd
import pickle
 
def begin():
    global model_params
    model_params = pickle.load(open('model_params.pkl', 'rb'))

def action(datum):
    mydf = datum
    mydf['z'] = model_params['a']*mydf['x'] + model_params['b']*mydf['y']
    # yield dict(mydf.sum()) # recordset input, regular output
    yield mydf # recordsets input and output