import pandas as pd
import numpy as np
data = pd.read_csv('ballparks.csv')
data.shape

row = data.columns[0]
print(f"available teams ({row}):", data[row].tolist())
print("available stats:", list(data.columns))

user_team_input = input('which teams stadium would you like to see?: ')
user_stat_input = input('which stats would you like to see?: ')

#if user_team_input in data['team_name']:
    #if user_





sub_data = data[['team_name', 'ballpark', 'left_field', 'center_field', 'right_field']]
