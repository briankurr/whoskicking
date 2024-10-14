# app/services.py
from app.models import Team
import random
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_teams() -> list[Team]:
    return Team.query.filter_by(isActive=1).all()

def create_game_matchups(teams: list[Team]) -> list[dict]:
    pass
