import yaml

# Open and read the YAML file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Access the data
print(config['database']['host'])

# Your configuration data as Python dictionaries
config = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'name': 'myapp_db',
        'credentials': {
            'username': 'admin',
            'password': 'secret123'
        }
    },
    'server': {
        'host': '0.0.0.0',
        'port': 8000,
        'debug': True
    },
    'features': {
        'enable_cache': True,
        'cache_ttl': 3600
    }
}

# Write to a YAML file
with open('generated_config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)

# Configuration with lists
services_config = {
    'services': [
        {
            'name': 'auth-service',
            'url': 'http://auth.example.com',
            'timeout': 30
        },
        {
            'name': 'payment-service',
            'url': 'http://payment.example.com',
            'timeout': 60
        },
        {
            'name': 'notification-service',
            'url': 'http://notification.example.com',
            'timeout': 15
        }
    ],
    'retry_policy': {
        'max_attempts': 3,
        'backoff_seconds': 5
    }
}

# Write to file
with open('services.yaml', 'w') as file:
    yaml.dump(services_config, file, default_flow_style=False, sort_keys=False)

# Read it back
with open('services.yaml', 'r') as file:
    loaded_services = yaml.safe_load(file)

# Access list items
for service in loaded_services['services']:
    print(f"Service: {service['name']}, URL: {service['url']}")

import os

class ConfigManager:
    def __init__(self, config_dir='configs'):
        self.config_dir = config_dir
        self.config = {}

    def load_config(self, environment='development'):
        """Load configuration for a specific environment"""
        config_file = os.path.join(self.config_dir, f'{environment}.yaml')

        try:
            with open(config_file, 'r') as file:
                self.config = yaml.safe_load(file)
            print(f"✓ Loaded configuration for {environment}")
            return self.config
        except FileNotFoundError:
            print(f"✗ Configuration file not found: {config_file}")
            return None
        except yaml.YAMLError as e:
            print(f"✗ Error parsing YAML: {e}")
            return None

    def get(self, key_path, default=None):
        """Get a configuration value using dot notation"""
        keys = key_path.split('.')
        value = self.config

        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default

        return value

    def save_config(self, environment, config_data):
        """Save configuration to a file"""
        config_file = os.path.join(self.config_dir, f'{environment}.yaml')

        os.makedirs(self.config_dir, exist_ok=True)

        with open(config_file, 'w') as file:
            yaml.dump(config_data, file, default_flow_style=False)

        print(f"✓ Saved configuration for {environment}")


