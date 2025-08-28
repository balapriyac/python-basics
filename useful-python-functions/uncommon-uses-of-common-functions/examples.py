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
