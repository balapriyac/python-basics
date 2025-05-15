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
def organize_inventory(products):
    # First sort by quantity (least to most)
    by_quantity = sorted(products, key=lambda x: x['quantity'])
    
    # Then sort by category
    by_category = sorted(by_quantity, key=lambda x: x['category'])
    
    # Finally sort by priority
    final_sorted = sorted(by_category, key=lambda x: x['priority'])
    
    return final_sorted

inventory = [
    {'name': 'Laptop', 'category': 'Electronics', 'quantity': 5, 'priority': 1},
    {'name': 'Headphones', 'category': 'Electronics', 'quantity': 8, 'priority': 2},
    {'name': 'Notebook', 'category': 'Office', 'quantity': 15, 'priority': 3},
    {'name': 'Pen', 'category': 'Office', 'quantity': 50, 'priority': 3}
]


# use it like this
def organize_inventory(products):
    return sorted(products, key=lambda x: (
        x['priority'],      # Sort by priority first
        x['category'],      # Then by category
        x['quantity']       # Then by quantity
    ))


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
