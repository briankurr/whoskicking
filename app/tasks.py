# app/tasks.py
from app import socketio, app, db
from app.services import fetch_teams, create_game_matchups
from app.models import Game

def update_games():
    while True:
        with app.app_context():
            # Fetch teams from the database
            teams = fetch_teams()

            # Create game matchups
            games = create_game_matchups(teams)

            # Update the games in the database
            for game_data in games:
                # Check if the game already exists
                game = Game.query.filter_by(game_id=game_data['game_id']).first()
                if game:
                    # Update existing game
                    game.home_team = game_data['home_team']['name']
                    game.away_team = game_data['away_team']['name']
                    game.kickoff_team = game_data['kickoff_team']['name'] if game_data['kickoff_team'] else None
                else:
                    # Create new game
                    new_game = Game(
                        game_id=game_data['game_id'],
                        home_team=game_data['home_team']['name'],
                        away_team=game_data['away_team']['name'],
                        kickoff_team=game_data['kickoff_team']['name'] if game_data['kickoff_team'] else None
                    )
                    db.session.add(new_game)
            db.session.commit()

            # Emit the updated games to connected clients via Socket.IO
            socketio.emit('update_games', games)

        # Sleep for 10 seconds before the next update
        socketio.sleep(10)

# Start the background task
socketio.start_background_task(update_games)
