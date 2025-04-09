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

def main():
    file = 'ballparks.csv'
    data = read_csv(file)
    teams_list = ', '.join(data.index)
    metrics_list = ', '.join(data.columns)
    print(f'available teams: {teams_list}')
    print(f'available metrics: {metrics_list}')

    team = input('Enter a team acronym (ex: NYY): ').strip().upper()
    metric = input('Enter a metric name (ex: ballpark): ').strip().lower()

    result = get_stat(data, team, metric)
    print(f"\nResult: {result}")

if __name__ == "__main__":
    main()

