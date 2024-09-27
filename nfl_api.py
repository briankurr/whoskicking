import random
import time

call_count = 0

def fetch_nfl_data():
    global call_count
    call_count += 1
    
    # Mock API call
    time.sleep(1)  # Simulate API delay
    teams = ['Patriots', 'Bills', 'Jets', 'Dolphins', 'Ravens', 'Steelers', 'Browns', 'Bengals']
    games = []
    
    for i in range(4):
        home = random.choice(teams)
        teams.remove(home)
        away = random.choice(teams)
        teams.remove(away)
        
        # Randomly change kickoff_team based on call_count
        if call_count % 3 == 0:
            kickoff_team = random.choice([home, away])
        else:
            kickoff_team = None
        
        games.append({
            'game_id': f'2023_W1_G{i+1}',
            'home_team': home,
            'away_team': away,
            'kickoff_team': kickoff_team
        })
    
    return games

def process_game_data(nfl_data):
    # In a real scenario, we would process the API data here
    # For this example, we'll just return the mock data as-is
    return nfl_data
