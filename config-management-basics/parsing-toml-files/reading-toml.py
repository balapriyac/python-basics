import tomllib

with open('config.toml', 'rb') as f:
    config = tomllib.load(f)

# Access values
app_title = config['title']
db_host = config['database']['host']
db_port = config['database']['port']

print(f"Application: {app_title}")
print(f"Database: {db_host}:{db_port}")
print(f"Config keys: {config.keys()}")

with open('config.toml', 'rb') as f:
    config = tomllib.load(f)

# Strings
app_title = config['title']

# Integers
db_port = config['database']['port']
cache_ttl = config['cache']['ttl']

# Booleans
debug_mode = config['server']['debug']
cache_enabled = config['cache']['enabled']

# Arrays (become Python lists)
databases = config['database']['databases']
allowed_hosts = config['server']['allowed_hosts']

print(f"Databases: {databases}")
print(f"Type of databases: {type(databases)}")
print(f"Debug mode: {debug_mode}, type: {type(debug_mode)}")

from pathlib import Path

class TOMLConfig:
    def __init__(self, config_file='config.toml'):
        self.config_file = Path(config_file)

        if not self.config_file.exists():
            raise FileNotFoundError(f"Config file not found: {config_file}")

        with open(self.config_file, 'rb') as f:
            self.config = tomllib.load(f)

    def get(self, key, default=None):
        """Get a top-level configuration value"""
        return self.config.get(key, default)

    def get_section(self, section):
        """Get an entire configuration section"""
        if section not in self.config:
            raise ValueError(f"Section '{section}' not found")
        return self.config[section]

config = TOMLConfig('config.toml')

# Get top-level values
app_title = config.get('title')
version = config.get('version')

# Get entire sections
db_config = config.get_section('database')
server_config = config.get_section('server')

print(f"{app_title} v{version}")
print(f"Database config: {db_config}")

# Sample nested TOML structure
toml_content = """
[database.primary]
host = "db1.example.com"
port = 5432

[database.replica]
host = "db2.example.com"
port = 5432

[api.v1]
enabled = true
rate_limit = 100

[api.v2]
enabled = false
rate_limit = 200
"""

config = tomllib.loads(toml_content)

# Access nested values
primary_host = config['database']['primary']['host']
v1_rate_limit = config['api']['v1']['rate_limit']

print(f"Primary DB: {primary_host}")
print(f"API v1 rate limit: {v1_rate_limit}")

def load_config_safe(config_file='config.toml'):
    try:
        with open(config_file, 'rb') as f:
            return tomllib.load(f)
    except FileNotFoundError:
        print(f"Config file {config_file} not found, using defaults")
        return {}
    except tomllib.TOMLDecodeError as e:
        print(f"Error parsing TOML: {e}")
        raise

config = load_config_safe('config.toml')

# Get with defaults
db_host = config.get('database', {}).get('host', 'localhost')
db_port = config.get('database', {}).get('port', 5432)
debug = config.get('server', {}).get('debug', False)

print(f"Database: {db_host}:{db_port}")
print(f"Debug: {debug}")


