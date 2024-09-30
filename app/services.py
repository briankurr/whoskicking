# app/services.py
from app.models import Team
import random
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_teams() -> list[Team]:
    return Team.query.filter_by(isActive=1).all()

def create_game_matchups(teams: list[Team]) -> list[dict]:
    games = []
    if len(teams) < 2:
        logger.warning("Not enough teams to create game matchups")
        return games

    for i in range(12):
        home = random.choice(teams)
        teams.remove(home)
        away = random.choice(teams)
        teams.remove(away)
        kickoff_team = random.choice([home, away])
        
        games.append({
            'game_id': f'2023_W1_G{i+1}',
            'home_team': {
                'name': home.name,
                'code': home.abbreviation,
                'color': home.color,
                'alternate_color': home.alternateColor
            },
            'away_team': {
                'name': away.name,
                'code': away.abbreviation,
                'color': away.color,
                'alternate_color': away.alternateColor
            },
            'kickoff_team': {
                'name': kickoff_team.name,
                'code': kickoff_team.abbreviation,
                'color': kickoff_team.color,
                'alternate_color': kickoff_team.alternateColor
            }
        })
    
    return games
