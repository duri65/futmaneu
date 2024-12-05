#!/usr/bin/python
import datetime
import pandas as pd

def export_to_excel(data_list, file_path):
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data_list)
    
    # Write the DataFrame to an Excel file
    df.to_excel(file_path)

def generate_tournament():
    num_teams = 8
    num_courts = 2
    start_time = datetime.datetime(year=2023, month=5, day=1, hour=8, minute=30)
    match_duration = datetime.timedelta(minutes=20)
    break_duration = datetime.timedelta(minutes=5)
    
    teams = [f"Team {i + 1}" for i in range(num_teams)]
    schedule = []
    court = 1
    
    for i in range(num_teams - 1):
        for j in range(i + 1, num_teams):
            team1 = teams[i]
            team2 = teams[j]
            
            match_start = start_time + i * match_duration
            match_end = match_start + match_duration
            
            schedule.append({
                "Court": court,
                "Group": "Group A" if court == 1 else "Group B",
                "Team 1": team1,
                "Team 2": team2,
                "Start Time": match_start,
                "End Time": match_end
            })
            
            court += 1
            if court > num_courts:
                court = 1
            
            start_time += break_duration
    
    return schedule

tournament_schedule = generate_tournament()
export_to_excel(tournament_schedule, 'output.xlsx')


#for match in tournament_schedule:
#    print(match)
