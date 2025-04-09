import pandas as pd
import numpy as np

def read_csv(file):
    data = pd.read_csv(file)
    data.set_index('team_name', inplace=True)
    return data

def get_stat(data, acronym, metric):
     try:
         value = data.loc[acronym.upper(), metric]
         return value
     except KeyError:
         return "Team or metric not found, please refer to the list."




sub_data = data[['team_name', 'ballpark', 'left_field', 'center_field', 'right_field']]
