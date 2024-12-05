#!/usr/bin/python
from datetime import datetime, timedelta
import pandas as pd

def export_to_excel(data_list, file_path):
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data_list)
    # Write the DataFrame to an Excel file
    df.to_excel(file_path)

def generate_matches(teams, start_time, match_duration, break_duration):
    num_teams = len(teams)
    num_rounds = num_teams - 1

    match_time = start_time
    all_matches = []
    for round in range(num_rounds):
        matches = []
        for i in range(num_teams // 2):
            team1 = teams[i]
            team2 = teams[num_teams - 1 - i]

            match_end_time = match_time + timedelta(minutes=match_duration)
            matches.append((team1, team2, match_time, match_end_time))

            match_time = match_end_time + timedelta(minutes=break_duration)

        teams.insert(1, teams.pop())

        all_matches.append(matches)

    return all_matches

# Zoznam mužstiev
groups = 2
#teams = ['Diviaky U11', 'H.Štubňa', 'L.Ondrášová', 'Bystrička']
teams = ['Diviaky Žltí', 'Diviaky Modrí','Ľubochňa','Rajec','Nitrianske Pravno', 'Zuberec', 'Hliník nad Váhom']
# Časové údaje
start_time = datetime.strptime('9:00', '%H:%M')
match_duration = 20
break_duration = 5

# Vygenerovanie zápasov
matches = generate_matches(teams, start_time, match_duration, break_duration)

# Výpis všetkých zápasov
for round, matches_round in enumerate(matches, start=1):
#    print(f"Round {round}:")
    for match in matches_round:
        match_start_time = match[2].strftime('%H:%M')
        match_end_time = match[3].strftime('%H:%M')
        print(f"{match_start_time} - {match_end_time} {match[0]} vs {match[1]}")

export_to_excel(matches, 'skupinaA.xlsx')