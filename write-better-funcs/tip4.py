# example fn. for processing transaction
def process_payment(transaction_id: int, amount: float, currency: str, description: str = None):
    print(f"Processing transaction {transaction_id}...")
    print(f"Amount: {amount} {currency}")
    if description:
        print(f"Description: {description}")

# Usage
process_payment(1234, 100.0, 'USD', 'Payment for services')

# enforce keyword-only arguments to minimize errors
# make the optional `description` arg keyword-only
def process_payment(transaction_id: int, amount: float, currency: str, *, description: str = None):
    print(f"Processing transaction {transaction_id}:")
    print(f"Amount: {amount} {currency}")
    if description:
        print(f"Description: {description}")

# Usage
process_payment(1234, 100.0, 'USD', description='Payment for services')
process_payment(5678, 150.0, 'EUR', 'Invoice payment') # throws error as we try to pass in more positional args than allowed!
