import logging
import json
from datetime import datetime, timezone
import os
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler


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

# Structured Logging with Context

class ContextLogger:
    """Logger wrapper that adds contextual information to all log messages"""

    def __init__(self, name, context=None):
        self.logger = logging.getLogger(name)
        self.context = context or {}

        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        # Check if handler already exists to avoid duplicate handlers
        if not any(isinstance(h, logging.StreamHandler) and h.formatter._fmt == '%(message)s' for h in self.logger.handlers):
            self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)

    def _format_message(self, message, level, extra_context=None):
        """Format message with context as JSON"""
        log_data = {
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'level': level,
            'message': message,
            'context': {**self.context, **(extra_context or {})}
        }
        return json.dumps(log_data)

    def debug(self, message, **kwargs):
        self.logger.debug(self._format_message(message, 'DEBUG', kwargs))

    def info(self, message, **kwargs):
        self.logger.info(self._format_message(message, 'INFO', kwargs))

    def warning(self, message, **kwargs):
        self.logger.warning(self._format_message(message, 'WARNING', kwargs))

    def error(self, message, **kwargs):
        self.logger.error(self._format_message(message, 'ERROR', kwargs))

def process_order(order_id, user_id):
    logger = ContextLogger(__name__, context={
        'order_id': order_id,
        'user_id': user_id
    })

    logger.info('Order processing started')

    try:
        items = fetch_order_items(order_id)
        logger.info('Items fetched', item_count=len(items))

        total = calculate_total(items)
        logger.info('Total calculated', total=total)

        if total > 1000:
            logger.warning('High value order', total=total, flagged=True)

        return True
    except Exception as e:
        logger.error('Order processing failed', error=str(e))
        return False

def fetch_order_items(order_id):
    return [{'id': 1, 'price': 50}, {'id': 2, 'price': 75}]

def calculate_total(items):
    return sum(item['price'] for item in items)

process_order('ORD-12345', 'USER-789')

# Rotating log files

def setup_rotating_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Size-based rotation: rotate when file reaches 10MB
    size_handler = RotatingFileHandler(
        'app_size_rotation.log',
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=5  # Keep 5 old files
    )
    size_handler.setLevel(logging.DEBUG)

    # Time-based rotation: rotate daily at midnight
    time_handler = TimedRotatingFileHandler(
        'app_time_rotation.log',
        when='midnight',
        interval=1,
        backupCount=7  # Keep 7 days
    )
    time_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    size_handler.setFormatter(formatter)
    time_handler.setFormatter(formatter)

    logger.addHandler(size_handler)
    logger.addHandler(time_handler)

    return logger


logger = setup_rotating_logger('rotating_app')

for i in range(1000):
    logger.info(f'Processing record {i}')
    logger.debug(f'Record {i} details: completed in {i * 0.1}ms')


# diff envs

def configure_environment_logger(app_name):
    """Configure logger based on environment"""
    environment = os.getenv('APP_ENV', 'development')
    
    logger = logging.getLogger(app_name)
    
    # Clear existing handlers
    logger.handlers = []
    
    if environment == 'development':
        # Development: verbose console output
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(levelname)s - %(name)s - %(funcName)s:%(lineno)d - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
    elif environment == 'staging':
        # Staging: detailed file logs + important console messages
        logger.setLevel(logging.DEBUG)
        
        file_handler = logging.FileHandler('staging.log')
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s'
        )
        file_handler.setFormatter(file_formatter)
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)
        console_formatter = logging.Formatter('%(levelname)s: %(message)s')
        console_handler.setFormatter(console_formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
    elif environment == 'production':
        # Production: structured logs, errors only to console
        logger.setLevel(logging.INFO)
        
        file_handler = logging.handlers.RotatingFileHandler(
            'production.log',
            maxBytes=50 * 1024 * 1024,  # 50 MB
            backupCount=10
        )
        file_handler.setLevel(logging.INFO)
        file_formatter = logging.Formatter(
            '{"timestamp": "%(asctime)s", "level": "%(levelname)s", '
            '"logger": "%(name)s", "message": "%(message)s"}'
        )
        file_handler.setFormatter(file_formatter)
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)
        console_formatter = logging.Formatter('%(levelname)s: %(message)s')
        console_handler.setFormatter(console_formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger
