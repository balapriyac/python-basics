from itertools import groupby

# Analyze user activity patterns from server logs
user_actions = ['login', 'login', 'browse', 'browse', 'browse', 
                'purchase', 'logout', 'logout']

# Compress into pattern summary
activity_patterns = [(action, len(list(group))) 
                    for action, group in groupby(user_actions)]

print(activity_patterns)

# Calculate total time spent in each activity phase
total_duration = sum(count for action, count in activity_patterns)
print(f"Session lasted {total_duration} actions")

# Quarterly sales data organized by product lines
quarterly_sales = [
    [120, 135, 148, 162],  # Product A by quarter
    [95, 102, 118, 125],   # Product B by quarter
    [87, 94, 101, 115]     # Product C by quarter
]

# Transform to quarterly view across all products
by_quarter = list(zip(*quarterly_sales))
print("Sales by quarter:", by_quarter)

# Calculate quarterly growth rates
quarterly_totals = [sum(quarter) for quarter in by_quarter]
growth_rates = [(quarterly_totals[i] - quarterly_totals[i-1]) / quarterly_totals[i-1] * 100
                for i in range(1, len(quarterly_totals))]
print(f"Growth rates: {[f'{rate:.1f}%' for rate in growth_rates]}")

import bisect

# Maintain a high-score leaderboard that stays sorted
class Leaderboard:
    def __init__(self):
        self.scores = []
        self.players = []

    def add_score(self, player, score):
        # Insert maintaining descending order
        pos = bisect.bisect_left([-s for s in self.scores], -score)
        self.scores.insert(pos, score)
        self.players.insert(pos, player)

    def top_players(self, n=5):
        return list(zip(self.players[:n], self.scores[:n]))

# Demo the leaderboard
board = Leaderboard()
scores = [("Alice", 2850), ("Bob", 3100), ("Carol", 2650),
          ("David", 3350), ("Eva", 2900)]

for player, score in scores:
    board.add_score(player, score)

print("Top 3 players:", board.top_players(3))
