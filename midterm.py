import pandas as pd
import numpy as np
data = pd.read_csv('ballparks.csv')
data.shape

row = data.columns[0]
print(f"available teams ({row}):", data[row].tolist())
print("available stats:", list(data.columns))

row_name = input('which teams stadium would you like to see?: ')
col_name = input('which stats would you like to see?: ')

if user_team_input not in data['team_name']:
    print("team not found")
else:
    row_name = data[data[row] == user_team_input]

    if not row.empty:
        value = row.iloc[0][user_stat_input]
        print(f"The stat you are looking for for '{user_team_input}' is '{user_stat_input}' : {value}" )
    else:
        print("stat metric not found")





sub_data = data[['team_name', 'ballpark', 'left_field', 'center_field', 'right_field']]
