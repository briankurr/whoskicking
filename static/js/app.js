document.addEventListener('DOMContentLoaded', () => {
    const socket = io();

    socket.on('connect', () => {
        console.log('Connected to server');
    });

    socket.on('update_games', (games) => {
        console.log('Received game updates:', games);  // Add this line to confirm updates
        const gamesContainer = document.getElementById('games-container');
        gamesContainer.innerHTML = '';

        games.forEach(game => {
            const gameCard = document.createElement('div');
            gameCard.className = 'game-card bg-white rounded-lg shadow-md p-4';
            gameCard.innerHTML = `
                <div class="flex justify-between items-center">
                    <span class="text-lg font-semibold">${game.home_team}</span>
                    <span class="text-sm">vs</span>
                    <span class="text-lg font-semibold">${game.away_team}</span>
                </div>
                <div class="mt-2 text-center text-sm">
                    ${game.kickoff_team 
                        ? `<span class="text-green-600">${game.kickoff_team} kicking off in 2nd half</span>`
                        : '<span class="text-yellow-600">Kickoff information not available</span>'
                    }
                </div>
            `;
            gamesContainer.appendChild(gameCard);
        });
    });
});
