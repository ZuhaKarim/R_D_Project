import pandas as pd
import pickle

# Creatin input file for the models
original_obj = pd.read_pickle(r'data/qm9/test_QM9.pkl')

# selecting molecules
mol_15 = [original_obj[0],
          original_obj[1000],
          original_obj[2000], 
          original_obj[3500],
          original_obj[9010],
          original_obj[1500],
          original_obj[1610],
          original_obj[2200],
          original_obj[9600],
          original_obj[8000],
          original_obj[17000],
          original_obj[740],
          original_obj[8510],
          original_obj[4010],
          original_obj[1900]]

# Saving the input file
file_obj = open('data/qm9/data_15.pkl', 'wb')
pickle.dump(mol_15, file_obj)
file_obj.close()