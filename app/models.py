import enum
from app import db
from sqlalchemy import Enum

class SeasonType(enum.Enum):
    PRE_SEASON = 1
    REGULAR_SEASON = 2
    POST_SEASON = 3
    OFF_SEASON = 4

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    season_id = db.Column(db.Integer, db.ForeignKey('season.id'), nullable=False)
    home_team = db.Column(db.String(64), nullable=False)
    away_team = db.Column(db.String(64), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'season_id': self.season_id,
            'home_team': self.home_team,
            'away_team': self.away_team,
            'start_time': self.start_time
        }


class Season(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    type = db.Column(Enum(SeasonType), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'year': self.year,
            'type': self.type.value
        }


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    logo_url = db.Column(db.String(256))
    slug = db.Column(db.String(256))
    location = db.Column(db.String(256))
    nickname = db.Column(db.String(256))
    abbreviation = db.Column(db.String(256))
    displayName = db.Column(db.String(256))
    shortDisplayName = db.Column(db.String(256))
    color = db.Column(db.String(256))
    alternateColor = db.Column(db.String(256))
    isActive = db.Column(db.Integer)


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'logo_url': self.logo_url,
            'slug': self.slug,
            'location': self.location,
            'nickname': self.nickname,
            'abbreviation': self.abbreviation,
            'displayName': self.displayName,
            'shortDisplayName': self.shortDisplayName,
            'color': self.color,
            'alternateColor': self.alternateColor,
            'isActive': self.isActive,
        }

class Logo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    href = db.Column(db.String(256))
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    alt = db.Column(db.String(256))
    rel = db.Column(db.String(256))
    lastUpdated = db.Column(db.DateTime)

    def to_dict(self):
        return {
            'id': self.id,
            'team_id': self.team_id,
            'href': self.href,
            'width': self.width,
            'height': self.height,
            'alt': self.alt,
            'rel': self.rel,
            'lastUpdated': self.lastUpdated
        }
        