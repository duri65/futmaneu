#!/usr/bin/python
import datetime
import pandas as pd

def export_to_excel(data_list, file_path):
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data_list)
    
    # Write the DataFrame to an Excel file
    df.to_excel(file_path)

def generate_tournament():
    num_teams = 4
    start_time = datetime.datetime(year=2023, month=5, day=1, hour=8, minute=30)
    match_duration = datetime.timedelta(minutes=20)
    break_duration = datetime.timedelta(minutes=5)
    
    teams = [f"Team {i + 1}" for i in range(num_teams)]
    schedule = []
    
    for i in range(num_teams):
        team1 = teams[i]
        
        # Rotate the teams for each match to ensure no team plays two consecutive matches
        rotated_teams = teams[i+1:] + teams[:i]
        
        for j in range(num_teams - 1):
            team2 = rotated_teams[j]
            
            match_start = start_time + (i * (num_teams - 1) + j) * (match_duration + break_duration)
            match_end = match_start + match_duration
            
            schedule.append({
                "Team 1": team1,
                "Team 2": team2,
                "Start Time": match_start,
                "End Time": match_end
            })
    
    return schedule

tournament_schedule = generate_tournament()

for match in tournament_schedule:
    print(match)


export_to_excel(tournament_schedule, 'A.xlsx')
