import json
import pandas as pd
from datetime import datetime
import os
import warnings
warnings.filterwarnings('ignore')
def match_reader (json_file_path):
    df = pd.DataFrame(columns=['Event', 'Match', 'Date', 'Venue', 'City', 'Team1', 'Players1', 'Team2', 'Players2', 'Winner', 'Batting', 'Innings', 'Over', 'Batsman', 'Bowler', 'Non-Striker', 'Bat-Score', 'Extras-Score', 'Extras-Bool', 'Extras', 'Wicket-Type', 'Wicket-Bool', 'Player Out', 'Run-Total', 'Wicket-Count'])
    with open(json_file_path, 'r') as file:
        # Parse the JSON data
        parsed_data = json.load(file)
        event = parsed_data['info']['event']['name']
        mdate = datetime.strptime(parsed_data["info"]["dates"][0], "%Y-%m-%d").date()
        try:
            match = parsed_data['info']['event']['match_number']
        except Exception as e:
            match = parsed_data['info']['event']['stage']
        venue = parsed_data['info']['venue']
        city = parsed_data['info']['city']
        Team_1 = parsed_data['info']['teams'][0]
        Team_2 = parsed_data['info']['teams'][1]
        Winner = parsed_data['info']['outcome']['winner']
        T1_ply = parsed_data['info']['players'][parsed_data['info']['teams'][0]]
        T2_ply = parsed_data['info']['players'][parsed_data['info']['teams'][1]]
        runs1 = 0
        runs2 = 0
        wkct1 = 0
        wkct2 = 0
        for i in range(len(parsed_data['innings'][0]['overs'])):
            over = parsed_data['innings'][0]['overs'][i : i + 1]
            dely = 1
            for ball in over[0]['deliveries']:
                bowl = i + (dely/10)
                bowler = ball['bowler']
                inc = 1
                batsman = ball['batter']
                n_strike = ball['non_striker']

                if batsman in T1_ply and n_strike in T1_ply:
                    Batting = Team_1
                else:
                    Batting = Team_2
                
                bat_sc = ball['runs']['batter']
                ext_sc = ball['runs']['extras']
                runs1 = runs1 + bat_sc + ext_sc
                ext = ''
                wicket = False
                extras = False
                play_out = ''
                fielder = ''
                wkt_type = ''
                if 'wickets' in ball:
                    wicket = True
                    wkct1 = wkct1 + 1
                    play_out = ball['wickets'][0]['player_out']
                    
                    if 'fielders' in ball['wickets'][0]:
                        fielder = ball['wickets'][0]['fielders'][0]['name']
                        
                    wkt_type = ball['wickets'][0]['kind']
                    
                else:
                    wicket = False
                if 'extras' in ball:
                    extras = True
                    ext = list(ball['extras'].keys())
                    for element in ext:    
                        if 'wide' in element or 'no' in element:
                            inc = 0
                else:
                    extras = False

                dely = dely + inc
                nrow = {'Event' : event, 'Match' : match, 'Date' : mdate, 'Venue' : venue, 'City' : city, 
                        'Team1' : Team_1, 'Players1' : T1_ply, 'Team2' : Team_2, 'Players2' : T2_ply, 
                        'Winner' : Winner, 'Batting' : Batting, 'Innings' : 1, 'Over' : bowl, 
                        'Batsman' : batsman, 'Bowler' : bowler, 'Non-Striker' : n_strike,
                        'Bat-Score' : bat_sc, 'Extras-Score' : ext_sc, 'Extras-Bool' : extras,
                        'Extras' : ext, 'Wicket-Type' : wkt_type, 'Player Out' : play_out,
                        'Wicket-Bool' : wicket, 'Run-Total' : runs1, 'Wicket-Count' : wkct1}
                df = pd.concat([df, pd.DataFrame([nrow])], ignore_index=True)
                
        for i in range(len(parsed_data['innings'][1]['overs'])):
            over = parsed_data['innings'][1]['overs'][i : i + 1]
            dely = 1
            for ball in over[0]['deliveries']:
                bowl = i + (dely/10)
                bowler = ball['bowler']
                inc = 1
                batsman = ball['batter']
                n_strike = ball['non_striker']

                if batsman in T1_ply and n_strike in T1_ply:
                    Batting = Team_1
                else:
                    Batting = Team_2
                
                bat_sc = ball['runs']['batter']
                ext_sc = ball['runs']['extras']
                runs2 = runs2 + bat_sc + ext_sc
                ext = ''
                wicket = False
                extras = False
                play_out = ''
                fielder = ''
                wkt_type = ''
                if 'wickets' in ball:
                    wkct2 = wkct2 + 1
                    wicket = True
                    play_out = ball['wickets'][0]['player_out']
                    
                    if 'fielders' in ball['wickets'][0]:
                        fielder = ball['wickets'][0]['fielders'][0]['name']
                        
                    wkt_type = ball['wickets'][0]['kind']
                    
                else:
                    wicket = False
                if 'extras' in ball:
                    extras = True
                    ext = list(ball['extras'].keys())
                    for element in ext:    
                        if 'wide' in element or 'no' in element:
                            inc = 0
                else:
                    extras = False

                dely = dely + inc
                nrow = {'Event' : event, 'Match' : match, 'Date' : mdate, 'Venue' : venue, 'City' : city, 
                        'Team1' : Team_1, 'Players1' : T1_ply, 'Team2' : Team_2, 'Players2' : T2_ply, 
                        'Winner' : Winner, 'Batting' : Batting, 'Innings' : 2, 'Over' : bowl, 
                        'Batsman' : batsman, 'Bowler' : bowler, 'Non-Striker' : n_strike,
                        'Bat-Score' : bat_sc, 'Extras-Score' : ext_sc, 'Extras-Bool' : extras,
                        'Extras' : ext, 'Wicket-Type' : wkt_type, 'Player Out' : play_out,
                        'Wicket-Bool' : wicket, 'Run-Total' : runs2, 'Wicket-Count' : wkct2}
                df = pd.concat([df, pd.DataFrame([nrow])], ignore_index=True)
    return df
    
