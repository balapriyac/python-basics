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

# logging exceptions
import json

logger = logging.getLogger('api_handler')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('errors.log')
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)
logger.addHandler(handler)

def fetch_user_data(user_id):
    logger.info(f'Fetching data for user {user_id}')

    try:
        # Simulate API call
        response = call_external_api(user_id)
        data = json.loads(response)
        logger.debug(f'Received data: {data}')
        return data
    except json.JSONDecodeError as e:
        logger.error(
            f'Failed to parse JSON for user {user_id}: {e}',
            exc_info=True
        )
        return None
    except ConnectionError as e:
        logger.error(
            f'Network error while fetching user {user_id}',
            exc_info=True
        )
        return None
    except Exception as e:
        logger.critical(
            f'Unexpected error in fetch_user_data: {e}',
            exc_info=True
        )
        raise

def call_external_api(user_id):
    # Simulated API response
    return '{"id": ' + str(user_id) + ', "name": "John"}'

fetch_user_data(123)

# from logger_config

from logger_config import setup_logger

logger = setup_logger(__name__)

def calculate_discount(price, discount_percent):
    logger.debug(f'Calculating discount: {price} * {discount_percent}%')
    
    if discount_percent < 0 or discount_percent > 100:
        logger.warning(f'Invalid discount percentage: {discount_percent}')
        discount_percent = max(0, min(100, discount_percent))
    
    discount = price * (discount_percent / 100)
    final_price = price - discount
    
    logger.info(f'Applied {discount_percent}% discount: ${price} -> ${final_price}')
    return final_price

calculate_discount(100, 20)
calculate_discount(100, 150)
