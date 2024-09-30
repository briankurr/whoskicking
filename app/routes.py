# app/routes.py
from flask import render_template
from app import app, db, socketio
from app.services import fetch_teams, create_game_matchups

@app.route('/')
def index():
    teams = fetch_teams()
    games = create_game_matchups(teams)
    return render_template('index.html', games=games)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

# Ensure database tables are created
with app.app_context():
    db.create_all()
