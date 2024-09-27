import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
db.init_app(app)
socketio = SocketIO(app)

from models import Game
from nfl_api import fetch_nfl_data, process_game_data

@app.route('/')
def index():
    games = Game.query.all()
    return render_template('index.html', games=games)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

def update_games():
    while True:
        with app.app_context():
            nfl_data = fetch_nfl_data()
            processed_data = process_game_data(nfl_data)
            
            for game_data in processed_data:
                game = Game.query.filter_by(game_id=game_data['game_id']).first()
                if game:
                    game.home_team = game_data['home_team']
                    game.away_team = game_data['away_team']
                    game.kickoff_team = game_data['kickoff_team']
                    db.session.commit()
                else:
                    new_game = Game(**game_data)
                    db.session.add(new_game)
                    db.session.commit()
            
            games = Game.query.all()
            socketio.emit('update_games', [game.to_dict() for game in games])
        
        socketio.sleep(10)  # Update every 10 seconds

socketio.start_background_task(update_games)

with app.app_context():
    db.create_all()
