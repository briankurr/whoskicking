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
