import os

# Get an environment variable (raises KeyError if not found)
api_key = os.environ['API_KEY']

# Safer approach: get with a default value
database_host = os.environ.get('DATABASE_HOST', 'localhost')
database_port = os.environ.get('DATABASE_PORT', '5432')

print(f"Connecting to {database_host}:{database_port}")

# Set an environment variable
os.environ['APP_ENV'] = 'development'
os.environ['MAX_CONNECTIONS'] = '100'

# Verify it was set
print(f"Environment: {os.environ['APP_ENV']}")

# Delete an environment variable
if 'TEMP_VAR' in os.environ:
    del os.environ['TEMP_VAR']

