# instead of this
def generate_leaderboard(players):
    leaderboard = []
    for i, player in enumerate(players):
        # Manually adding 1 because leaderboards start at 1, not 0
        leaderboard.append(f"{i+1}. {player['name']}: {player['score']} pts")
    return leaderboard

top_players = [
    {'name': 'MasterBlaster', 'score': 157},
    {'name': 'QuickShot', 'score': 145},
    {'name': 'StealthNinja', 'score': 132}
]
print('\n'.join(generate_leaderboard(top_players)))

# use it like this
def generate_leaderboard(players):
    # The start parameter makes our intention crystal clear
    leaderboard = []
    for rank, player in enumerate(players, start=1):
        leaderboard.append(f"{rank}. {player['name']}: {player['score']} pts")
    return leaderboard

# instead of this

# use it like this

# instead of this
# use it like this

# instead of this

# use it like this
# instead of this
# use it like this
# instead of this
# use it like this
# instead of this
# use it like this
