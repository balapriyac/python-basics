# instead of this
def process_sales_data(sales):
    highest_sale = sales[0]
    for sale in sales:
        if sale > highest_sale:
            highest_sale = sale
    
    total_sales = 0
    for sale in sales:
        total_sales += sale
    
    return highest_sale, total_sales, total_sales / len(sales)

# do this
def process_sales_data(sales):
    return max(sales), sum(sales), sum(sales) / len(sales)

# Instead of this
def get_premium_customer_emails(customers):
    premium_emails = []
    for customer in customers:
        if customer['membership_level'] == 'premium' and customer['active']:
            email = customer['email'].lower().strip()
            premium_emails.append(email)
    return premium_emails

# Do this
def get_premium_customer_emails(customers):
    return [
        customer['email'].lower().strip()
        for customer in customers
        if customer['membership_level'] == 'premium' and customer['active']
    ]

# Instead of this
def has_permission(user_id, permitted_users):
    # permitted_users is a list of user IDs
    for p_user in permitted_users:
        if p_user == user_id:
            return True
    return False

# Usage:
permitted_users = [1001, 1023, 1052, 1076, 1088, 1095, 1102, 1109]
print(has_permission(1088, permitted_users))  # True

# Do this
def has_permission(user_id, permitted_users):
    # permitted_users is now a set of user IDs
    return user_id in permitted_users

# Usage:
permitted_users = {1001, 1023, 1052, 1076, 1088, 1095, 1102, 1109}
print(has_permission(1088, permitted_users))  # True

# Instead of this
def find_errors(log_file):
    with open(log_file, 'r') as file:
        lines = file.readlines()
    
    error_messages = []
    for line in lines:
        if '[ERROR]' in line:
            timestamp = line.split('[ERROR]')[0].strip()
            message = line.split('[ERROR]')[1].strip()
            error_messages.append((timestamp, message))
    
    return error_messages
    
# Do this
def find_errors(log_file):
    with open(log_file, 'r') as file:
        for line in file:
            if '[ERROR]' in line:
                timestamp = line.split('[ERROR]')[0].strip()
                message = line.split('[ERROR]')[1].strip()
                yield (timestamp, message)

# Usage:
for timestamp, message in find_errors('application.log'):
    print(f"Error at {timestamp}: {message}")


import re
from datetime import datetime

def find_recent_errors(logs):
    recent_errors = []
    
    for log in logs:
        # This regex compilation happens on every iteration
        timestamp_pattern = re.compile(r'\[(.*?)\]')
        timestamp_match = timestamp_pattern.search(log)
        
        if timestamp_match and '[ERROR]' in log:
            # The datetime parsing happens on every iteration
            log_time = datetime.strptime(timestamp_match.group(1), '%Y-%m-%d %H:%M:%S')
            current_time = datetime.now()
            
            # Check if the log is from the last 24 hours
            time_diff = (current_time - log_time).total_seconds() / 3600
            if time_diff <= 24:
                recent_errors.append(log)
    
    return recent_errors

import re
from datetime import datetime

def find_recent_errors(logs):
    recent_errors = []
    
    # Compile the regex once
    timestamp_pattern = re.compile(r'\[(.*?)\]')
    # Get the current time once
    current_time = datetime.now()
    
    for log in logs:
        timestamp_match = timestamp_pattern.search(log)
        
        if timestamp_match and '[ERROR]' in log:
            log_time = datetime.strptime(timestamp_match.group(1), '%Y-%m-%d %H:%M:%S')
            
            # Check if the log is recent (last 24 hours)
            time_diff = (current_time - log_time).total_seconds() / 3600
            if time_diff <= 24:
                recent_errors.append(log)
    
    return recent_errors
