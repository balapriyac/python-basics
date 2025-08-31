# GROUPBY
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

# MATRIX TRANSPOSE WITH zip()
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

# BISECT
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

# HEAPQ
import heapq

# Analyze customer satisfaction survey results
survey_responses = [
    ("Restaurant A", 4.8), ("Restaurant B", 3.2), ("Restaurant C", 4.9),
    ("Restaurant D", 2.1), ("Restaurant E", 4.7), ("Restaurant F", 1.8),
    ("Restaurant G", 4.6), ("Restaurant H", 3.8), ("Restaurant I", 4.4),
    ("Restaurant J", 2.9), ("Restaurant K", 4.2), ("Restaurant L", 3.5)
]

# Find top performers and underperformers without full sorting
top_rated = heapq.nlargest(3, survey_responses, key=lambda x: x[1])
worst_rated = heapq.nsmallest(3, survey_responses, key=lambda x: x[1])

print("Excellence awards:", [name for name, rating in top_rated])
print("Needs improvement:", [name for name, rating in worst_rated])

# Calculate performance spread
best_score = top_rated[0][1]
worst_score = worst_rated[0][1]
print(f"Performance range: {worst_score} to {best_score} ({best_score - worst_score:.1f} point spread)")

# ITEMGETTER FOR MULTI-LEVEL SORT
from operator import itemgetter

# Employee performance data: (name, department, performance_score, hire_date)
employees = [
    ("Sarah", "Engineering", 94, "2022-03-15"),
    ("Mike", "Sales", 87, "2021-07-22"),
    ("Jennifer", "Engineering", 91, "2020-11-08"),
    ("Carlos", "Marketing", 89, "2023-01-10"),
    ("Lisa", "Sales", 92, "2022-09-03"),
    ("David", "Engineering", 88, "2021-12-14"),
    ("Amanda", "Marketing", 95, "2020-05-18")
]

sorted_employees = sorted(employees, key=itemgetter(1, 2))
# For descending performance within department:
dept_performance_sorted = sorted(employees, key=lambda x: (x[1], -x[2]))

print("Department performance rankings:")
current_dept = None
for name, dept, score, hire_date in dept_performance_sorted:
    if dept != current_dept:
        print(f"\n{dept} Department:")
        current_dept = dept
    print(f"  {name}: {score}/100")

# DEFAULTDICT
from collections import defaultdict

books_data = [
    ("1984", "George Orwell", "Dystopian Fiction", 1949),
    ("Dune", "Frank Herbert", "Science Fiction", 1965),
    ("Pride and Prejudice", "Jane Austen", "Romance", 1813),
    ("The Hobbit", "J.R.R. Tolkien", "Fantasy", 1937),
    ("Foundation", "Isaac Asimov", "Science Fiction", 1951),
    ("Emma", "Jane Austen", "Romance", 1815)
]

# Create multiple indexes simultaneously
catalog = {
    'by_author': defaultdict(list),
    'by_genre': defaultdict(list),
    'by_decade': defaultdict(list)
}

for title, author, genre, year in books_data:
    catalog['by_author'][author].append((title, year))
    catalog['by_genre'][genre].append((title, author))
    catalog['by_decade'][year // 10 * 10].append((title, author))

# Query the catalog
print("Jane Austen books:", dict(catalog['by_author'])['Jane Austen'])
print("Science Fiction titles:", len(catalog['by_genre']['Science Fiction']))
print("1960s publications:", dict(catalog['by_decade']).get(1960, []))

# string.Template
from string import Template

report_template = Template("""
=== SYSTEM PERFORMANCE REPORT ===
Generated: $timestamp
Server: $server_name

CPU Usage: $cpu_usage%
Memory Usage: $memory_usage%
Disk Space: $disk_usage%

Active Connections: $active_connections
Error Rate: $error_rate%

${detailed_metrics}

Status: $overall_status
Next Check: $next_check_time
""")

# Simulate partial monitoring data (some sensors might be offline)
monitoring_data = {
    'timestamp': '2024-01-15 14:30:00',
    'server_name': 'web-server-01',
    'cpu_usage': '23.4',
    'memory_usage': '67.8',
    # Missing: disk_usage, active_connections, error_rate, detailed_metrics
    'overall_status': 'OPERATIONAL',
    'next_check_time': '15:30:00'
}

# Generate report with available data, leaving gaps for missing info
report = report_template.safe_substitute(monitoring_data)
print(report)
# Output shows available data filled in, missing variables left as $placeholders
print("\n" + "="*50)
print("Missing data can be filled in later:")
additional_data = {'disk_usage': '45.2', 'error_rate': '0.1'}
updated_report = Template(report).safe_substitute(additional_data)
print("Disk usage now shows:", "45.2%" in updated_report)
