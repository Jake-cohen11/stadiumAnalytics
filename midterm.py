import pandas as pd
import numpy as np
data = pd.read_csv('ballparks.csv')
data.shape

user_team_input = input('which teams stadium would you like to see?: ')
user_stat_input = input('which stats would you like to see? enter "stop" to stop: ')
while True:
    if user_stat_input == 'stop':
        break
    



sub_data = data[['team_name', 'ballpark', 'left_field', 'center_field', 'right_field']]
