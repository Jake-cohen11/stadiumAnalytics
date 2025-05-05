import pandas as pd
from pathlib import Path

def read_csv(file):
    data = pd.read_csv(file)
    data.set_index('team_name', inplace=True)
    return data

def get_stat(data, acronym, metric):
     try:
         value = data.loc[acronym.upper(), metric.lower()]
         return value
     except KeyError:
         return "Team or metric not found, please refer to the list."
     
example_teams = ('NYY', 'LAD', 'NYM', 'BOS') #tuple of example teams

def main(): #this function asks the user as well as finds the data the user is looking for
    file = 'ballparks.csv'
    data = read_csv(file)
    teams_list = ', '.join(data.index)
    metrics_list = ', '.join(data.columns)

    print('You can select any MLB team and specific stats about that teams stadium. Your choices are listed below.')
    print(f'available teams: {teams_list}')
    print(f'available metrics: {metrics_list}')
    print(f'\nteam name examples: {", ".join(example_teams)}\n')

    while True:
        team = input('Enter a team acronym, type STOP to exit: ').strip().upper()
        if team.upper() == 'STOP':
            break
        metric = input('Enter a metric name, type STOP (ex: ballpark): ').strip().lower()
        if metric.upper() == 'STOP':
            break
        result = get_stat(data, team, metric)
        if result is None:
            print("Team or metric not found, please look at the list again and try again.")
        new_file = Path.cwd() / 'stadium_analytics.txt'
        new_file.touch()
        with new_file.open(mode="w", encoding = "utf-8"):
            new_file.write_text(f"You chose to look at the {metric} of the {team}. The result is {result}")

if __name__ == "__main__": #calls the main function
    main()

