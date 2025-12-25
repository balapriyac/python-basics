import logging

logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug('This is a debug message')
logger.info('Application started')
logger.warning('Disk space running low')
logger.error('Failed to connect to database')
logger.critical('System shutting down')

###
logger = logging.getLogger('payment_processor')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
logger.addHandler(handler)

def process_payment(user_id, amount):
    logger.debug(f'Starting payment processing for user {user_id}')

    if amount <= 0:
        logger.error(f'Invalid payment amount: {amount}')
        return False

    logger.info(f'Processing ${amount} payment for user {user_id}')

    if amount > 10000:
        logger.warning(f'Large transaction detected: ${amount}')

    try:
        # Simulate payment processing
        success = charge_card(user_id, amount)
        if success:
            logger.info(f'Payment successful for user {user_id}')
            return True
        else:
            logger.error(f'Payment failed for user {user_id}')
            return False
    except Exception as e:
        logger.critical(f'Payment system crashed: {e}', exc_info=True)
        return False

def charge_card(user_id, amount):
    # Simulated payment logic
    return True

process_payment(12345, 150.00)
process_payment(12345, 15000.00)

