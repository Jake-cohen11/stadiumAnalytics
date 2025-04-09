import pandas as pd
import numpy as np

def read_csv(file):
    data = pd.read_csv(file)
    data.set_index('team_name', inplace=True)
    return data


row = data.columns[0]
print(f"available teams ({row}):", data[row].tolist())
print("available stats:", list(data.columns))

row_name = input('which teams stadium would you like to see?: ')
col_name = input('which stats would you like to see?: ')

if row_name not in data:
    print("team not found")
else:
    row_name = data[data[row] == row_name]

    if not row.empty:
        value = row.iloc[0][col_name]
        print(f"The stat you are looking for for '{row_name}' is '{col_name}' : {value}" )
    else:
        print("stat metric not found")

sub_data = data[['team_name', 'ballpark', 'left_field', 'center_field', 'right_field']]
