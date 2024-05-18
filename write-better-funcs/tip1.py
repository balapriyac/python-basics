# fn. to analyze sales data, calculate sales metrics, and write it to a file
def analyze_and_report_sales(data, report_filename):
    total_sales = sum(item['price'] * item['quantity'] for item in data)
    average_sales = total_sales / len(data)
    
    with open(report_filename, 'w') as report_file:
        report_file.write(f"Total Sales: {total_sales}\n")
        report_file.write(f"Average Sales: {average_sales}\n")
    
    return total_sales, average_sales


# refactored into two funcs: one to calculate metrics and another to write sales report
def calculate_sales_metrics(data):
    total_sales = sum(item['price'] * item['quantity'] for item in data)
    average_sales = total_sales / len(data)
    return total_sales, average_sales

def write_sales_report(report_filename, total_sales, average_sales):
    with open(report_filename, 'w') as report_file:
        report_file.write(f"Total Sales: {total_sales}\n")
        report_file.write(f"Average Sales: {average_sales}\n")

# Usage
data = [{'price': 100, 'quantity': 2}, {'price': 200, 'quantity': 1}]
total_sales, average_sales = calculate_sales_metrics(data)
write_sales_report('sales_report.txt', total_sales, average_sales)
