from app import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.String(64), unique=True, nullable=False)
    home_team = db.Column(db.String(64), nullable=False)
    away_team = db.Column(db.String(64), nullable=False)
    kickoff_team = db.Column(db.String(64))

    def to_dict(self):
        return {
            'id': self.id,
            'game_id': self.game_id,
            'home_team': self.home_team,
            'away_team': self.away_team,
            'kickoff_team': self.kickoff_team
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
        