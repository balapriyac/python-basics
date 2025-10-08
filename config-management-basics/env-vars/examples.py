import os

# Get an environment variable (raises KeyError if not found)
api_key = os.environ['API_KEY']

# Safer approach: get with a default value
database_host = os.environ.get('DATABASE_HOST', 'localhost')
database_port = os.environ.get('DATABASE_PORT', '5432')

print(f"Connecting to {database_host}:{database_port}")

database_port = int(os.environ.get('DATABASE_PORT', '5432'))
max_connections = int(os.environ.get('MAX_CONNECTIONS', '10'))

total_capacity = database_port + max_connections  # Now this works with integers

debug_mode = os.environ.get('DEBUG', 'False').lower() in ('true', '1', 'yes')

# Set an environment variable
os.environ['APP_ENV'] = 'development'
os.environ['MAX_CONNECTIONS'] = '100'

# Verify it was set
print(f"Environment: {os.environ['APP_ENV']}")

# Delete an environment variable
if 'TEMP_VAR' in os.environ:
    del os.environ['TEMP_VAR']

class AppConfig:
    """Application configuration loaded from environment variables"""
    
    def __init__(self):
        # Required settings (will fail fast if missing)
        self.api_key = self._get_required('API_KEY')
        self.database_url = self._get_required('DATABASE_URL')
        
        # Optional settings with defaults
        self.debug = self._get_bool('DEBUG', False)
        self.port = self._get_int('PORT', 8000)
        self.log_level = os.environ.get('LOG_LEVEL', 'INFO')
        self.max_workers = self._get_int('MAX_WORKERS', 4)
        
    def _get_required(self, key):
        """Get a required environment variable or raise an error"""
        value = os.environ.get(key)
        if value is None:
            raise ValueError(f"Required environment variable '{key}' is not set")
        return value
    
    def _get_bool(self, key, default):
        """Convert environment variable to boolean"""
        value = os.environ.get(key)
        if value is None:
            return default
        return value.lower() in ('true', '1', 'yes', 'on')
    
    def _get_int(self, key, default):
        """Convert environment variable to integer"""
        value = os.environ.get(key)
        if value is None:
            return default
        try:
            return int(value)
        except ValueError:
            raise ValueError(f"Environment variable '{key}' must be an integer, got '{value}'")
    
    def __repr__(self):
        """Safe string representation (masks sensitive data)"""
        return (f"AppConfig(debug={self.debug}, port={self.port}, "
                f"log_level={self.log_level}, api_key={'*' * 8})")

config = AppConfig()
print(config)
print(f"Running on port {config.port}")
