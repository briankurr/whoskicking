import re
from typing import List
import requests

class ESPNClient:
    def __init__(self):
        self.core_api_url = "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl"
        self.site_api_url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl"
        self.cdn_url = "https://cdn.espn.com/core/nfl"

    def get_season_schedule(self, season_id: int) -> dict:
        raise NotImplementedError("This method is not implemented yet")

    def get_season_weeks(self, season_year: int, season_type: int) -> List[str]:
        url = f"{self.core_api_url}/seasons/{season_year}/types/{season_type}/weeks"
        response = requests.get(url)
        payload = response.json()
        weeks = payload.get('items', [])
        return sorted([week['$ref'] for week in weeks if '$ref' in week], key=self._get_week_number)

    def get_week_schedule(self, season_year: int, season_type: int, week: int) -> dict:
        raise NotImplementedError("This method is not implemented yet")

    def _get_week_number(self, url: str) -> int:
        match = re.search(r'weeks/(\d+)', url)
        return int(match.group(1)) if match else None