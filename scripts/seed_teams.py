# seed_teams.py
import sys
import os

# Add the project root to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, project_root)

import requests
from app import app, db
from app.models import Team, Logo
import datetime

def seed_teams():
    with app.app_context():
        # Initial API endpoint to fetch all teams
        api_url = 'https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2024/teams'
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            teams_list = data.get('items', [])

            for team_ref in teams_list:
                team_url = team_ref.get('$ref')
                if team_url:
                    team_response = requests.get(team_url)
                    if team_response.status_code == 200:
                        team_data = team_response.json()
                        # Check if the team already exists
                        existing_team = Team.query.filter_by(name=team_data.get('name')).first()
                        if not existing_team:
                            # Create a new Team instance
                            team = Team(
                                name=team_data.get('name'),
                                logo_url=team_data.get('logos', [{}])[0].get('href', ''),
                                slug=team_data.get('slug'),
                                location=team_data.get('location'),
                                nickname=team_data.get('nickname'),
                                abbreviation=team_data.get('abbreviation'),
                                displayName=team_data.get('displayName'),
                                shortDisplayName=team_data.get('shortDisplayName'),
                                color=team_data.get('color'),
                                alternateColor=team_data.get('alternateColor'),
                                isActive=int(team_data.get('isActive', False))
                            )
                            db.session.add(team)
                            db.session.commit()  # Commit to get the team.id

                            # Handle logos
                            logos_data = team_data.get('logos', [])
                            for logo_data in logos_data:
                                try:
                                    last_updated_str = logo_data.get('lastUpdated', '')
                                    if last_updated_str:
                                        last_updated = datetime.datetime.strptime(last_updated_str, '%Y-%m-%dT%H:%MZ')
                                    else:
                                        last_updated = None
                                except ValueError:
                                    last_updated = None

                                logo = Logo(
                                    team_id=team.id,
                                    href=logo_data.get('href'),
                                    width=logo_data.get('width'),
                                    height=logo_data.get('height'),
                                    alt=logo_data.get('alt'),
                                    rel=', '.join(logo_data.get('rel', [])),  # Convert list to string
                                    lastUpdated=last_updated
                                )
                                db.session.add(logo)
                            db.session.commit()
                            print(f"Team {team.name} and its logos have been added.")
                        else:
                            print(f"Team {team_data.get('name')} already exists in the database.")
                    else:
                        print(f"Failed to fetch team data from {team_url}: {team_response.status_code}")
                else:
                    print("No '$ref' found in team reference.")
            print("All teams have been successfully seeded.")
        else:
            print(f"Failed to fetch data from {api_url}: {response.status_code}")

if __name__ == '__main__':
    seed_teams()
