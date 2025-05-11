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
