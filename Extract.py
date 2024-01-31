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


                                            #FULL CODE IS NOT ATTACHED
