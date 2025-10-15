
import configparser
from pathlib import Path



config = configparser.ConfigParser()
config.read('/content/app.ini')

# Access values from sections
db_host = config['database']['host']
db_port = config['database']['port']

print(f"Database: {db_host}:{db_port}")
print(f"Sections: {config.sections()}")


config = configparser.ConfigParser()
config.read('app.ini')

# Automatic type conversion
db_port = config.getint('database', 'port')
ssl_enabled = config.getboolean('database', 'ssl_enabled')

# With fallback defaults
max_retries = config.getint('database', 'max_retries', fallback=3)
timeout = config.getfloat('database', 'timeout', fallback=30.0)

print(f"Port: {db_port}, SSL: {ssl_enabled}")

class ConfigManager:
    def __init__(self, config_file='app.ini'):
        self.config = configparser.ConfigParser()

        if not Path(config_file).exists():
            raise FileNotFoundError(f"Config file not found: {config_file}")

        self.config.read(config_file)

    def get_database_config(self):
        db = self.config['database']
        return {
            'host': db.get('host'),
            'port': db.getint('port'),
            'username': db.get('username'),
            'password': db.get('password'),
            'pool_size': db.getint('pool_size', fallback=5)
        }

config = ConfigManager('app.ini')
db_config = config.get_database_config()
print(db_config)


config = configparser.ConfigParser()
config.read('app.ini')

# Get all options in a section as a dictionary
db_settings = dict(config['database'])
server_settings = dict(config['server'])

# Check if a section exists
if config.has_section('cache'):
    cache_enabled = config.getboolean('cache', 'enabled')
else:
    cache_enabled = False

print(f"Database settings: {db_settings}")
print(f"Caching enabled: {cache_enabled}")


config = configparser.ConfigParser()

# Add sections and values
config['database'] = {
    'host': 'localhost',
    'port': '5432',
    'username': 'myapp'
}

config['server'] = {
    'host': '0.0.0.0',
    'port': '8000',
    'debug': 'false'
}

# Write to file
with open('generated.ini', 'w') as configfile:
    config.write(configfile)

print("Configuration file created!")
