class ConfigError(Exception):
    """Configuration-related errors"""
    pass

def load_database_config():
    try:
        with open('config/database.yaml') as f:
            # Imagine we're using PyYAML here
            return yaml.safe_load(f)
    except FileNotFoundError as e:
        raise ConfigError(
            "Database configuration file not found"
        ) from e
    except yaml.YAMLError as e:
        raise ConfigError(
            "Invalid database configuration format"
        ) from e

# Usage
try:
    config = load_database_config()
except ConfigError as e:
    print(f"Configuration error: {e}")
    print(f"Original error: {e.__cause__}")
  
