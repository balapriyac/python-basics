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




